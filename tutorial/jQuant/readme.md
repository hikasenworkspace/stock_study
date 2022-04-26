### About dataset

- https://japanexchangegroup.github.io/J-Quants-Tutorial/


- 財務三表の見方 https://money-bu-jpx.com/news/article022723/

- #### stock_list
  stock_listは、銘柄の名前や業種区分などの基本情報が含まれています。発行済株式数は、会社が発行することをあらかじめ定款に定めている株式数（授権株式数）のうち、会社が既に発行した株式数のことです。発行済株式数と株価とかけ合わせて時価総額を計算することができます。時価総額は企業価値を評価する際に用いられる重要な指標です。

  - prediction_target : bool 
    
    予測対象銘柄. Trueの時は予測対象となる？Flaseだったら無視して良い.

  - Section/Products : object

    市場・商品区分(株式市場). 'First Section (Domestic)' 'Second Section(Domestic)'  'JASDAQ(Standard / Domestic)' 'Mothers (Domestic)' の４つを持つ。詳しくは[pdf](files/J_kouhyou.pdf)を参照。　基本的には何らかのコンセプトを元に、区分訳する。(単にクライアント向けにカテゴライズしているだけ？)

  - 業種区分情報
    
    マーケットにおける業種別の平均などを計算する時に役立つ情報です。33業種は証券コード協議会が定めており、17業種はTOPIX-17シリーズとして「投資利便性を考慮して17業種に再編したもの」TOPIX（東証株価指数）

    - 33 Sector(Code)

      銘柄の33業種区分(コード)
      
    - 33 Sector(name)

      銘柄の33業種区分(名前)

      > 業種別分類項目」は､10の大分類の下に33の中分類があり､通常「業種」といった場合は、建設業、食料品、電気機器など、この中分類を指すことが一般的です。東京証券取引所では、同協議会の定める業種を採用し、業種別株価指数等を公表しているため、東証33業種と呼ばれることもあります。
      
    - 銘柄の17業種区分


    33 凝縮分は
    
    ['Construction' 'Foods' 'Services' 'Information & Communication''Retail Trade' 'Wholesale Trade' 'Real Estate' 'Textiles and Apparels' 'Pharmaceutical' 'Chemicals' 'Glass and Ceramics Products' 'Iron and Steel' 'Nonferrous Metals' 'Other Products' 'Metal Products' 'Machinery' 'Electric Appliances' 'Transportation Equipment' 'Insurance' 'Precision Instruments' 'Banks' 'Other Financing Business' 'Land Transportation'] 

    17 は

    ['CONSTRUCTION & MATERIALS ' 'FOODS ' 'IT & SERVICES, OTHERS ' 'RETAIL TRADE ' 'COMMERCIAL & WHOLESALE TRADE ' 'REAL ESTATE ' 'RAW MATERIALS & CHEMICALS ' 'PHARMACEUTICAL ' 'STEEL & NONFERROUS METALS ' 'MACHINERY ' 'ELECTRIC APPLIANCES & PRECISION INSTRUMENTS ' 'AUTOMOBILES & TRANSPORTATION EQUIPMENT ' 'FINANCIALS （EX BANKS） ' 'BANKS ' 'TRANSPORTATION & LOGISTICS '] 

    となっている。

  - Size

    > TOPIXニューインデックスシリーズは、TOPIX（東証株価指数）を規模（時価総額・流動性）で区分した株価指数です。

    時価総額、流動性の高さに応じて、区分がされている。上から順に、 Core 30, Large 70, Mid 400, Small　となる。

    ['TOPIX Small 2' 'TOPIX Small 1' 'TOPIX Mid400' '-' 'TOPIX Core30'  'TOPIX Large70'] の６つ


  - Equity Quote 
    資本見積もり？

    - IssuedShareEquityQuote AccountingStandard　

      会計基準　会計基準 単独:NonConsolidated、連結国内:ConsolidatedJP、連結SEC:ConsolidatedUS、連結IFRS:ConsolidatedIFRS　の３種類.

      - 日本会計基準、米国会計規準、国際会計基準（IFRS）の３種類がある。
      
      - 連結決算とは？

        > 連結決算とは、親会社だけでなく、国内・海外子会社および関連会社を含めたグループ全体の決算方法のことです。連結決算では、企業グループ全体の貸借対照表や損益計算書を連結財務諸表として公開しています。
      
        あるいわ
        > 連結決算は、子会社などの業績も合計して出した決算結果です。グループ全体としての経営状態がわかります。
        >
        > 単独決算は、その株式会社だけの業績をまとめた決算です。子会社に頼って業績がいいのかどうか、連結決算と比較することでわかります。

      - おそらく、どの会計基準に則っているかを表している項目。

    - IssuedShareEquityQuote IssuedShare

      > 発行済株式数は、会社が発行することをあらかじめ定款に定めている株式数（授権株式数）のうち、会社が既に発行した株式数のことです。発行済株式数と株価とかけ合わせて時価総額を計算することができます。時価総額は企業価値を評価する際に用いられる重要な指標です。

  - #### 株価情報 : stock_price

    > stock_priceには各銘柄の各日付の始値や終値などの株価情報が記録されています。テクニカル分析などで終値ベースの分析を実施する場合は、ExchangeOfficialCloseを利用します。ここでいうテクニカル分析というのは、マーケットデータから計算される指標に基づいた分析のことです。また、終値ベースの分析とは、マーケットデータの中でも、終値のみを用いた分析を表しています。

    株価情報は、「株式分割」や「株式併合」(Kaggleでいうstock splitのこと)が発生した際に生じる株価の変動を、株式数の変化率に応じて調整されています。

    特徴量の定義によっては、その日付時点で実際に取引された株価や出来高を取得したい場合がありますが、その場合は累積調整係数を使用して

    `[調整前株価] = [調整済株価] * [累積調整係数] 及び [調整前出来高] = [調整済出来高] / [累積調整係数]`

    - **Kaggleでは、調整前出来高のみ表示されている**

    - 株式配合は考慮されていない

    - マーケットが開いている日に取引が成立しなかった銘柄は、売買高が0となり、四本値 (始値、高値、安値、終値) 全てが0と表示されます。

    > - stock_priceのデータは、そのデータに含まれている最新日付時点で累積調整係数1となるように調整されます。調整済み株価についても同様に過去に遡って更新されます。 

      つまり、分割や併合が怒らなかったとした時の価格が表示されていると考えてよい？

    - Local Code : 銘柄コード 

      説明不要？

    - EndOfDayQuote ExchangeOfficialClose

      取引所公式終値。最終の特別気配または最終気配を含む終値. EndOfDayQuote Closeと何が違う？
      > 公式終値とは、先物取引の全限月において夜間取引の終了後に金融取が算出する値です。

      限月とは？
      > 先物・オプション取引は取引できる期限毎に商品が分かれており、取引できる期限の月を「限月」といいます。 また、特定の限月を対象とする商品は「～月限（ぎり）」と呼ばれており、たとえば3月を限月とする商品は「3月限（さんがつぎり）」といいます。

      つまり、先物取引を考慮したその日の終値？のこと
  

  ### kaggleのデータセットをJquantsに対応させる

  - stock_list
    - 会計基準がない？
  
  - stock_fin
    - やはり、会計基準はない？

      - TypeOfDocumentにそれらしいものはあるけど、おそらく違う。
      