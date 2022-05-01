import numpy as np
import pandas as pd

tokenid = "eyJraWQiOiJOY3prOTNVY1hqYmtEN2NHQWFYN0NMaXZWTytGRkxhejQ0cUJLc0FFK3o4PSIsImFsZyI6IlJTMjU2In0.eyJvcmlnaW5fanRpIjoiNDcyNGVlMDEtMGRmMi00ODgyLTk3ZGItMTJlNjA4NmI5NDE0Iiwic3ViIjoiOWQ1YmMwNWYtMWJhYy00Y2E4LWE0NDYtZGU3NzNlNGM1MzNlIiwiYXVkIjoiMmliYzNxMjMxbWhhZGd0M2hqbjY2YTBncHMiLCJldmVudF9pZCI6IjkzNmUyOTJlLWNmYmYtNGM4Yi1iZTc3LTE2ZmYyN2NjMTA3NyIsInRva2VuX3VzZSI6ImlkIiwiYXV0aF90aW1lIjoxNjUwNzI0MjQ5LCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAuYXAtbm9ydGhlYXN0LTEuYW1hem9uYXdzLmNvbVwvYXAtbm9ydGhlYXN0LTFfOTVORWxvamVpIiwiY29nbml0bzp1c2VybmFtZSI6IjB4NWNhYUNmQWFERjdBNGQzYTIwMkU3ZEVhNjExMWM1QzhiYzIyMWRBZiIsImV4cCI6MTY1MDgxMDY0OSwiaWF0IjoxNjUwNzI0MjQ5LCJqdGkiOiI3NDFmYjM4MS02MTliLTQzZGQtYjlmMS1hMGNhOGRjYjBkMjEifQ.ctNVlTwY66b6CsEFwVFmEFSI2FS52ZrVlQH6ucQ-wXrniwQnrLCfainf9VEt2P6BBaHe4RBZk5MF8m0JSfvd2U8Px2PbrbfxZJoeScnz1j6pJ3Jc5dDJCKCmJTN3zu3mNVZlSshOK94QAnDDSmcE5h_cjq7xYKzfMFkYsGv0bHJya6FVAw58X2y6iRokgD106fetfK1Cnjsn_JLqTtImnzvQz9-mQJbSod9VBE-TViuTlGzhdyxBQGr7eFXQvQtx8Xj6vdLIKti2qE_1vaJA7z28dt197Eh-ZTklHu6wJmmroKyxWgr0TufhZouXNDg_X8FLj0UEufhckDA_pJrNtg"

import requests
import json

token = tokenid

headers = {'Authorization': 'Bearer {}'.format(token)}
r = requests.get("https://api.jpx-jquants.com/v1/listed/info", headers=headers)
# r.json()
data_dict = r.json()
stock_list = pd.DataFrame(data_dict["info"])

r = requests.get("https://api.jpx-jquants.com/v1/listed/sections", headers=headers)
stock_sections = r.json()
data_dict = r.json()
stock_sections = pd.DataFrame(data_dict["sections"])
stock_sections = stock_sections.rename(columns={"SectorId" : "SectorCode"})

r = requests.get("https://api.jpx-jquants.com/v1/fins/announcement", headers=headers)
r.json()
data_dict = r.json()
stock_anno = pd.DataFrame(data_dict["announcement"])

stock_list = pd.merge(stock_list, stock_sections, on = "SectorCode")
stock_list = pd.merge(stock_list, stock_anno, on="Code", how="right")

columns_name = ['Local Code', 'Effective Date', 'CompanyNameFull', 'MarketCode', 'CompanyName_x', 'Name (English)', 'SectorCode', 'SectorName_x', 'Date', 'CompanyName_y', 'FiscalYear', 'SectorName_y', 'FiscalQuarter', 'Section/Products']
