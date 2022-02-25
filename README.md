# Pandas refactoring
- refactor work/main.py
- propose and write unit testing using Pytest

## Document
- work配下にリファクタリングを行ったmain.py, および関数のスクリプトを配置 
- work/data配下に使用したcsvファイルを配置 
- test配下にpytestにより実行されるスクリプトを配置

## Install
`git clone git@github.com:o-r-r-p/pandas_refactoring.git`   
`cd pandas_refactoring`

## Environment setting
`poetry shell`  
`poetry install`

## Test implementation
`cd tests`  
`pytest`

## 課題にどう取り組んだか
### 取り組んだ手順
#### 手順1. 課題の理解
pyproject.toml, main.py, poetry.lock, dataが与えられ、main.pyの課題についての記述とdataを実際にハンドリングすることで課題の概要を掴んだ。その際にpoetry, black, pytestについては環境構築、コード整形、関数のテストに用いられることを知った。

#### 手順2. poetryによる仮想環境構築
poetryによる仮想環境を構築したあと、poetry.lockの内容を構築した環境にインストール

#### 手順3. リファクタリング
"誰が読んでも理解しやすいコード"を意識しながらリファクタリングした。入れ子になっていてわかりにくいコードに対しては動作別にそれぞれcalculate, preprocessingの2つのモジュールを作成した。関数名や変数名についてはなるべく汎用的な名前を回避し、多少長くなっても理解しやすさを優先した。コメントについてはコメントを見れば何をしているコードか理解できるように編集した。

#### 手順4. pytestを用いてユニットテストを実施
pytestを実行し、作成した関数に対してテストを行った。想定される返り値と整合しないときはエラーとなり、意図する返り値になるように修正した。  
また、@pytest.fixtureを用い、テスト内で使用されるデータフレームや変数をまとめた。

#### 手順5. blackによるコード整形
テスト完了後、blackにより各コードを整形。black実行前後のコードを比較した。

## 苦労した点
### リファクタリングについて
"リファクタリングはコードの可読性を高め、理解しやすくすること"というざっくりとした理解と、一度読んだ”リーダブルコード"の内容を思い出しながら本課題をスタートした。リファクタリングを行う上で意識したことは以下の通りである。

 １. 関数を用いて1つ1つの処理に分解した　  
 ２. 関数名、変数名から処理を推測しやすくした　　
 
１については入れ子になっている処理、forループを用いている処理を中心に関数で処理を分解した。複数の処理が混同していると可読性の低下やエラーが出たときにコードの特定に時間がかかると考え実行した。また関数作成の際には、１つの関数につき１つの処理となるようにした。実際に、相関係数の計算と出力するコードを切り分けることで、修正も容易になると考えた。一方で簡潔な処理（read_csv、mergeなど）については独自の関数による可読性の低下を避け、コメントで処理内容の補完を行った。  
２については関数名、変数名それぞれに対して処理との整合性を取ることでコードの可読性が向上し、理解しやすくなると考えて実行した。実際に　「"inner_join" -> "precip_temp_one_station"」のように変数名を変更し、結合したデータフレームを明示的に示した。

### pytestについて
テストコード実装の意図としては”想定した返り値と整合性がとれているか確認するため”、程度のざっくりした理解であった。Google検索で調べながら着実に１つ１つテストコードを完成させた。その中でテスト実装する変数やデータフレームを関数ごとに定義すると、コードが煩雑になると感じたため、テスト関数における前処理を切り出せるfixtureを使用する工夫も行った。  
## 所感
環境構築、コード整形、テストコードについては理解の浅い部分であった。しかし、本課題を通してネット情報を参考にしながら、環境構築やテスト実装を行うことでもう一段理解が深まったと感じている。特に今回使用したpoetry, black, pytestはいずれも比較的新しいツールのようで、venvやPythonのコーディング規則、unittestとの比較や再確認をしながら、それぞれ実装した。これまでPython, 機械学習, 統計など独学で学ぶことが多かったが、技術の進歩が速い分野において自らキャッチアップし、スキルを高めていく必要性を改めて感じた。 
