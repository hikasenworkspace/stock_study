## RSAの仕組み
- 数学的なこと : https://qiita.com/YutaKase6/items/cd9e26d723809dc85928
- この人の良いよ : https://qiita.com/angel_p_57
## SSHの仕組み
- とりあえずこれ読む : https://rat.cis.k.hosei.ac.jp/article/rat/linuxliteracy/2005/ssh.html
- SSHが使用する暗号技術のリスト : https://www.alaxala.com/jp/techinfo/archive/manual/AX3660S/HTML/12_1_L/CFGUIDE/0210.HTM
- 特にRSAの使い方 : https://milestone-of-se.nesuke.com/sv-advanced/digicert/public-private-key/

# blockchainの仕組み
- 論文について
  - 簡単な日本語での[まとめ](https://www.ogis-ri.co.jp/otc/hiroba/technical/bitcoinpaper/)
  - 電子コインの問題点 (TTPの場合)
    - 偽造 
      - 本物に見えるコインを勝手に作ること。
      - 対策：デジタル署名を用いて、コインの発行場所を検証できるようにする
      - **論文を読んでも、厳密に偽造に対して強そうには見えない？**

    - 多重使用
      - 同じコインを繰り返し使うこと
      - 対策：コインのデータベースを管理する。一度使用されたら、もう使用できないようにするなど。
  - ブロックチェーンにおけるタイムスタンプについて
    - タイムスタンプとは、事実証明のためにその出来事が発生したタイミングを記録する仕組みのことを指します。例えば、現実世界では事実証明のために領収書などに記載されている日時もタイムスタンプの役割を果たしています。
    - コンピューター上のタイムスタンプを用いる場合
      - 定時間は各々のノードに設定されている時間。
      - 個人がコンピューターの設定時間を変えることで強固な事実証明が行われる可能性を大幅に下げる結果になってしまうという大きな弱点があり
    - 中央集権的タイムスタンプ
      - 中央のサーバーが１つの時間軸を設定することで、基準となる時刻を中央以外は改ざん不可能にし、上記のような個人による改ざんを防ごうという考え
      - 中央集権なので、ブロックチェーンの理念に反する
    - ブロックチェーンでは？
     - 分散化されたブロックチェーンでは、相対的な前後関係を証明さえできれば良いという考えです。
     - ハッシュの鎖を作り、確実な前後関係を築く。
  
  - POW
    - しかし、このハッシュの鎖はどの様に正しいと証明するのだろう？（途中で改ざんされている場合変なところがわかるが、そもそも一貫性のある嘘のハッシュの鎖を発行してしまっている可能性は？) 
    - ラウンドとマークルツリーを用いたタイムスタンプの場合は、定期的に新聞にラウンド・バリュー(ハッシュ)を発行することで、発行後は、最新のラウンドバリュー以前のデータを改ざんすることができなくなる。(おそらく発行する前は可能)。要するに、あとから改ざんできる余地がなくなるということ。
    - 上の方法は２つ問題を持つ？ 1. TTP(新聞)が必要 2. そもそも、発行元が受け付けないとかできる？
    - ブロックチェーンのPOWはネットワークに散らばる複数のノードがそれぞれ一斉にワークを開始する(ナンスを調べる)
    - 一つのノードでも目的のハッシュ（ナンスとも言える）を見つけたら、PoW一回分が終了
    - 理念：改ざんするとハッシュが変わるのでナンスを計算し直す必要がある。
    - 疑問
      - 全員で分ける理由. 全員で分けるだけで、改ざんできなくなるのでは？
      - 迷惑メールの箇所を読むこと。この例だと、

        > プライシング関数は迷惑メールを抑止しているだけで、それ以外には役に立つことをしていない (no useful purpose) と言うのです。

        と書かれている。
      
    - 結局コストがかかってしまう？電力コストなど 
    - それらさまざまな意見やブロックチェーン・プロジェクトを評価・検討するためには、**コストとともに、そのコストを支払って実現されること**はなんなのかもきちんと理解する必要があるでしょう。
    - 二重使用対策を行うため、各ノードがトランザクションのたったひとつの順番に合意できるような仕組みをとる。
    - PoW はコンセンサスアルゴリズム (consensus algorithm, 合意形成アルゴリズム) の一種である
    - しかし、今回見たとおり、PoW はブロックを生成する速さを一定に保つものであり、それだけで合意に至るものではありません
    - PoW は、コンセンサスアルゴリズムで用いられる技術要素、と言った方がより適切でしょう。ビットコインの合意形成の仕組みを「ナカモト・コンセンサス (Nakamoto Consensus)」と呼んで、PoW と明確に区別することもあります。
  
  - ethereum Wiki
    - https://github.com/ethereum/wiki/wiki/%5BJapanese%5D-White-Paper

  - bitcoin script
    - https://academy.binance.com/ja/articles/an-introduction-to-bitcoin-script
  - ### attacks
    - #### Transaction Malleability
      - https://qiita.com/nagmnt/items/81e7166e6ecdf2224665 は手を動かして理解できる
        -~~変更するのは、scriptsig なのでは？~~ 普通にscripsigを変更していました。
      - これを行うためには秘密鍵が必要？
        - 必要ない。scriptSigは、典型的には`<sig> <pubKey>`の形をとっているが、この`<sig>`は、scriptSigを除くトランザクションのハッシから生成される。生成にprivatekeyが必要。しかしながら、ScriptSigの変更は`<sig>`を変更する以外でも変更可能。例えば` OP_NOP <sig> <pubKey>`とするなど。
      - この変更を加えて再送信することで同じ内容の別のTXIDを持ったトランザクションがブロードキャストされ、それがブロックに入ってしまえば変更不可能
      - 仮に送信者が全てをTXIDで管理していたとすると、あたかも送ったトランザクションが何らかの理由で承認されなかったと勘違いされる。
      - **SegWit**によって解決可能

  - ### Bitcoin address

  - 二者間取引(ペイメントチャネル)
    - MultiSigを用いる
      - 複数の署名がないと使えないトランザクション？アカウント？
      -m 個の秘密鍵の内，n 個の秘密鍵を使用することで UTXO をアンロックするようなマルチシグネチャのことを m-of-n マルチシグと呼ぶ．今回は2-of-2まるちしぐを使用
    1. Funding Transactionを作る
    2. Refund Transactionを作る
    3. AからBにFunding Transactionを送り、署名してブロックチェーンに記録する.

  - ### Ethereum
    - https://qiita.com/kagami-r0927/items/d73492e3a9207c8345dc がめっちゃわかりやすい。
    - Ethereum アカウント
      - nonce 、各トランザクションの処理が一度きりであることを確約するためのカウンター
      - アカウントの現在の ether balance
      - アカウントの contract code （もし存在すれば）
      - アカウントの storage （デフォルトは空）

      Ether はトランザクション手数料を支払うために使用されます。 一般的に、アカウントには二つの種類があります。 秘密鍵により管理される EOA (externally owned accounts) と自身のコントラクトコードにより管理される contract (contract account) です。 EOA はコードを持たず、EOA からトランザクションを生成し署名することによって メッセージ を送ることができます。contract では、メッセージを受信した時はいつも保持コードをアクティベートし、内部ストレージを読み書き可能にし、メッセージを送信するもしくは新しいコントラクトを作る、といった内容のことが順番に実行されます。
      ここで言うコントラクトとは、特定のコードを実行し、自身の ether 残高と、なんども使う変数を把握するのに必要な key/value ストレージ を直接管理する権限を持っている、ということに注意してください。

    - メッセージ と トランザクション


      
  - ### Smart Contract
    - 

  - ## 発表
    ### - 電子コインの問題点
      - Tampering(改ざん)
        ハッキングして残高を変更する
      - コインの偽造
        自信でvalid-lookingな電子コインを発行し、それを他人に渡す。相手が間違いに気が付かなければ、そのまま取引が成立し、商品を受け取れる。
        相手は、いざ電子コインを使おうとした時にわかる。これは実際の現金での偽造と同じ仕組み
      - 多重使用
        電子コインというなの電子情報ならではの概念。同じコインを別々の人に支払うこと。
      - 支払い証明
        取引を行なった証明を誰が行うか？
    - ### TTPが存在する場合の問題点の解決法。
      - TTPが存在する場合、取引は右の図のようになる。
        - アリスが電子コインを銀行から引き出す。（現金と同等の価値）
        - アリスはボブに電子コインを支払う
        - ボブは銀行に受け取った電子コインを預けることで、残高が増える。
      - もし銀行がこの取引の過程全てを管理していれば、二重支払いは起こり得ない。
      - 銀行のセキュリティ対策が十分であれば、データの改竄は怒らない
    - ### 電子署名を用いた偽造対策
      - １万円札にはいくつもの仕掛けが施されていて、そのどれもが国立印刷局によって発行されていることを証明している
      - 電子コインの場合は、電子署名を電子コインに添付することで、この電子コインを発行した組織が、 銀行（TTP）であることを証明できる。

    - ### TTPを利用する問題点
      - New Trusted Third Parties are Costly and Risky
      - Existing Trusted Third Parties are Valuable
        - Almost all people blindly trusting  Companies like Visa, Dun and Bradstreet, Underwriter's Laboratories.
        - Of course, I use visa but I didn't care about their credibility.
        - Even though these organizations often have many flaws and weaknesses, these institutions are with us for a long time. 
      - Personal Property Has Not and Should Not Depend On TTPs
        - we should store our personal properties by ourselves. 
      - Cost of transaction 
        - for example, we pay fee for international transaction. and another example is the Cost when restaurant try to import the credit card payment.
      - Risk of server down. 
        - TTP need to ensure that server never down or in an unstable state during the deployment process.
        - This is called zero-downtime.
    - ### develop decentralized system
      - 中心的なアイデアは、全ての権力と情報を中央に集めるのではなく、peer to peerで管理するシステム。
      - このシステムは、クライアント(nodeあるいわpeer)は誰も信用しない。が、このシステムのことは信用する。
      - And all peers will be audited by the peers 

    - ### Distribute ledger across Peers
      - さとしの提案したモデルは、これまでの全ての台帳を全ピアーで共有し、完全に分権でかつ、permisson lessなもの。
      - ここで言う全ての台帳とは、全peerの台帳となる。
      - Thus, new node downloads the entire ledger history.
        - Actually, when I tried to join the node, it take a day to download all history.
      - This models are strong again the many risks such as data loss, data coruption, and tampering.

    - ### Definition of the coin
      - 今から、どのような仕組みなのかを確認する。
      - さとしは、ビットコインを、トランザクションの連鎖として定義した。
      - 100コイン使うためには、以前に別の人から100コイン以上のコインを受け取ってなければならない。
  

      


      
- 電子署名として、ECDSA を利用　[詳しい説明](https://qiita.com/angel_p_57/items/355eec5b5547ac122607#%E3%82%B3%E3%83%B3%E3%82%B9%E3%83%88%E3%83%A9%E3%82%AF%E3%82%BF-initialize)
- 