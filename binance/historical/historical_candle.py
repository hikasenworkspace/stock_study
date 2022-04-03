# import sys
import os
from argparse import ArgumentTypeError
import pandas as pd
from enums import *
from utility import download_file, get_all_symbols, get_parser, get_start_end_date_objects, convert_to_date_object, \
    get_path, match_date_regex, get_destination_dir


class hist_candle():

    def __init__(self, trading_type, symbols, intervals, dates,
                 start_date = None, end_date = None, folder = None, checksum = 0):
        
        assert trading_type in TRADING_TYPE
        self.tt = trading_type
        self.all_symbols = get_all_symbols(self.tt)
        assert set(symbols) <= set(self.all_symbols)
        self.symbols = symbols
        self.n_symbols = len(self.symbols)
        assert type(dates) == list and type(dates[0]) == str 
        
        if type(intervals) == str:
            intervals = [intervals]
        assert set(intervals) <= set(INTERVALS)
        self.intervals = intervals
        self.dates = []
        for date_ in dates:
            self.dates.append(match_date_regex(date_))
        
        if folder is not None:
            store_directory = os.path.dirname(os.path.realpath(__file__))
            folder = os.path.join(store_directory, folder)
            if not os.path.exists(folder):
                print(f"path '{folder}' doesn't exsists")
                raise ArgumentTypeError
        self.folder = folder

        if start_date and end_date:
            self.date_range = start_date + " " + end_date

        if not start_date:
            self.start_date = START_DATE
        else:
            self.start_date = match_date_regex(start_date)
            self.start_date = convert_to_date_object(self.start_date)

        if not end_date:
            self.end_date = END_DATE
        else:
            self.end_date = match_date_regex(end_date)
            self.end_date = convert_to_date_object(self.end_date)

        assert checksum in [0,1]
        self.checksum = checksum
        self.csv_symbol_name = []

    def download_daily(self, extract = False, printout = True):
        current = 0
        date_range = None
        print("Found {} symbols".format(self.n_symbols)) if printout else None

        self.csv_symbol_name = []
        for symbol in self.symbols:
            print("[{}/{}] - start download daily {} trades ".format(current+1, self.n_symbols, symbol))
            for interval in self.intervals:
                for date_ in self.dates:
                    current_date = convert_to_date_object(date_)
                    if current_date >= self.start_date and current_date <= self.end_date:
                        path = get_path(self.tt, "klines", "daily", symbol, interval)
                        file_name = "{}-{}-{}.zip".format(symbol.upper(), interval, date_)
                        ext_file_name = "{}-{}-{}.csv".format(symbol.upper(), interval, date_)
                        download_file(path, file_name, ext_file_name, date_range, self.folder,
                                    extract=extract, po = printout)
                        if self.checksum == 1:
                            checksum_path = get_path(self.tt, "trades", "daily", symbol)
                            checksum_file_name = "{}-trades-{}.zip.CHECKSUM".format(symbol.upper(), date_)
                            checksum_ext_file_name = "{}-trades-{}.CHECKSUM.csv".format(symbol.upper(), date_)
                            download_file(checksum_path, checksum_file_name, checksum_ext_file_name ,date_range, self.folder, 
                                        extract = False, po = printout)

                current += 1
    
    def dataframe(self):
        columns_name = ["Open time","Open","High","Low","Close","Volume","Close time","Quote asset volume","Number of trades","Taker buy base asset volume","Taker buy quote asset volume","Ignore"]
        dataframes = {}
        self.download_daily(extract = True, printout=False)
        current = 0
        date_range = None
        for symbol in self.symbols:
            for interval in self.intervals:
                for date_ in self.dates:
                    current_date = convert_to_date_object(date_)
                    if current_date >= self.start_date and current_date <= self.end_date:
                        path = get_path(self.tt, "klines", "daily", symbol, interval)
                        file_name = "{}-{}-{}.zip".format(symbol.upper(), interval, date_)
                        ext_file_name = "{}-{}-{}.csv".format(symbol.upper(), interval, date_)
                        if self.folder:
                            path = os.path.join(self.folder, path)
                        if date_range:
                            date_range = date_range.replace(" ","_")
                            path = os.path.join(path, date_range)
                        csv_save_path = get_destination_dir(os.path.join(path, ext_file_name), None)
                df = pd.read_csv(csv_save_path, names=columns_name, index_col='Open time')
                df.index = pd.to_datetime(df.index / 1e3, unit='s')
                dataframes[symbol + "-" + interval] = df
        return dataframes
