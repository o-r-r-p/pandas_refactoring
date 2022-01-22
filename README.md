## ディレクトリ構成
pandas_refactoring
├── README.md
├── before_black_main.py (The script is main.py before using black)
├── poetry.lock
├── pyproject.toml
├── tests
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-38.pyc
│   │   ├── test_calculate.cpython-38-pytest-6.2.5.pyc
│   │   ├── test_pandas_refactoring.cpython-38-pytest-6.2.5.pyc
│   │   ├── test_preprocessing.cpython-38-pytest-6.2.5.pyc
│   │   └── test_work.cpython-38-pytest-6.2.5.pyc
│   ├── test_calculate.py (This is the module for the test in calculate.py)
│   ├── test_preprocessing.py (This is the module for the test in preprocessing.py)
│   └── test_work.py
└── work
    ├── Monthly_data.csv (The file is the one requested in this assignment)
    ├── __init__.py
    ├── __pycache__
    │   ├── __init__.cpython-38.pyc
    │   ├── calculate.cpython-38.pyc
    │   └── preprocessing.cpython-38.pyc
    ├── calculate.py
    ├── data
    │   ├── climate_precip.csv
    │   └── climate_temp.csv
    ├── main.py
    └── preprocessing.py

## 課題にどう取り組んだか
### 取り組んだ手順

#### 手順1. 課題の理解
##### pyproject.toml, main.py, poetry.lock, dataが与えられ、main.pyの課題についての記述とdataを実際にハンドリングすることで課題の概要を掴んだ。その際にpoetry, black, pytestについては環境構築、コード整形、関数のテストに用いられることを知った。

#### 手順2. poetryによる仮想環境構築
##### poetryによる仮想環境を構築したあと、poetry.lockの内容を構築した環境にインストール

#### 手順3. リファクタリング
##### "誰が読んでも理解しやすいコード"を意識しながらリファクタリングした。入れ子になっていてわかりにくいコードに対してはcalculate, preprocessingの2つのモジュールを作成した。   関数名や変数名についてはなるべく汎用的な名前を回避し、多少長くなっても理解しやすさ優先した。コメントについてはコメントを見れば何をしているコードか理解できるように編集した。

#### 手順4. pytestを用いてユニットテストを実施
##### pytestを実行し、作成した関数に対してテストを行った。想定される返り値と整合しないときはエラーとなり、修正した。

#### 手順5. blackによるコード整形
##### blackにより各スクリプトをPEP8に従い整形。black実行前後のコードを比較した。

## 苦労した点
### リファクタリングについて
##### "リファクタリングはコードの可読性を高め、理解しやすくすること"というざっくりとした理解と、一度読んだ”リーダブルコード"の知識を思い出しながら本課題をスタートした。リファクタリングで