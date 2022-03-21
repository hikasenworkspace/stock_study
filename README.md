## Hikasen Workspace
- ### Member
  - #### ラル
    - 経歴：工学部
  - #### ポンタ
    - 経歴：物理学
  - #### スパマキ
    - 経歴：物理学
- ### GitHub
  - Link: https://github.com/MKrbm/stock_study
  - 共有内容
    - 議事録
    - コード

- ### Milestone
  - by April
    - データ収集のパイプライン
    - よわよわボットの運用開始
      - Market Orderができるくらい
      - 暗号通貨/株のトレード
  - by October
    - バックテスト環境
      - 手数料
      - Approx. スリップ
  - by December
    - つよつよボットの運用開始
  
- ### Pipeline Scheme
  - Data collection using Binance API
  - Develop models locally using Binance data
  - Test models on QuantConnect IDE

- ### Material
  - 金融系の基礎知識を復習/勉強
    - Website
      - [QuantConnect](https://www.quantconnect.com/tutorials/tutorial-series/introduction-to-financial-python)
        - [Bootcamp](https://www.quantconnect.com/learning)
        - [Tutorial](https://www.quantconnect.com/tutorials/tutorial-series/introduction)
      - [Japan Exchange Group](https://www.jpx.co.jp/)
        - [Signate](https://quest.signate.jp/quests/10058)
        - [J-Quants](https://japanexchangegroup.github.io/J-Quants-Tutorial/)
    - 書籍  
      - [Advances in Financial Machine Learning (AFML)](https://www.oreilly.com/library/view/advances-in-financial/9781119482086/)

- ### Datasets
  - Website
    - [Quandl](https://data.nasdaq.com/) (about [API](https://data.nasdaq.com/tools/api))

- ### Helpful Recourses
  - [Git Workflow](https://nvie.com/posts/a-successful-git-branching-model/)

## TODO
- [ ] Binance/Bitflyerの取引用アカウントを作る（スパマキ、ぽんた）
- [ ] 実際に手動取引して、肌感覚を掴む（スパマキ、ぽんた）
- [ ] QuantConnect Bootcamp（ラル）


## 議事録
- [02/19/2022](02192022.md)
- [02/25/2022](02252022.md)


## environment preparation

### docker

- change directory to `.devcontainer` by

        cd .devcontainer

- compose docker file with 

        docker-compose up -d

- run `docker exec -it <container_name> bash` to enter interactive shell

- `<container_name>` can be checked through `docker ps -n <n>`, where it shows `<n>` last created containers.

### python

- change directory to `.devcontainer` by

        cd .devcontainer

- create conda environment 

        conda env create -f environment.yml -n <env_name>

- activate environment

        conda activate <env_name>