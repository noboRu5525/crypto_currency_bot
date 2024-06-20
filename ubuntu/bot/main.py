# 自動売買ボットのコード
import os
import ccxt
from pprint import pprint
from datetime import datetime
import requests
import time
import pandas as pd
import numpy as np
import talib as ta


# .envファイルからアクセスキーとシークレットキーを取得
access_key = os.getenv('ACCESS_KEY')
secret_key = os.getenv('SECRET_KEY')

# 取引所の指定
cc = ccxt.coincheck({
    'apiKey': access_key,
    'secret': secret_key,
})

URL = 'https://coincheck.com/api/rate/btc_jpy'

######################## CoincheckのPublic APIにアクセスする関数 ########################

# ティッカー 各種最新情報を取得
def ticker():
    url = 'https://coincheck.com/api/ticker'
    info = requests.get(url).json()
    return info
# 全取引履歴 最新の取引履歴を取得
def trades():
    url = 'https://coincheck.com/api/trades'
    params = {'pair': 'btc_jpy'}
    info = requests.get(url, params).json()
    return info
# 板情報 asks:売り bids:書い
def order_books():
    url = 'https://coincheck.com/api/order_books'
    info = requests.get(url).json()
    return info
# レート取得 取引所の注文を元にレートを算出
# 買い
def buy_rate():
    url = 'https://coincheck.com/api/exchange/orders/rate'
    params = {'order_type':'buy','pair':'btc_jpy', 'amount': '0.01'}
    info = requests.get(url, params).json()
    return info
# 売り
def sell_rate():
    url = 'https://coincheck.com/api/exchange/orders/rate'
    params = {'order_type':'sell','pair':'btc_jpy', 'amount': '0.01'}
    info = requests.get(url, params).json()
    return info
# 基準レート取得
def base_rate():
    url = 'https://coincheck.com/api/rate/btc_jpy'
    info = requests.get(url).json()
    return info
# ステータス取得
# 2024/3/27から使えるみたい
def exchange_status():
    url = 'https://coincheck.com/api/exchange_status'
    info = requests.get(url).json()
    return info

######################## CoincheckのPrivate APIにアクセスする関数 ########################
# 新規注文 保留

# 取引履歴 最近の取引履歴を参照 保留
def transactions():
    url = 'https://coincheck.com/api/exchange/orders/transactions'
    info = requests.get(url).json()
    return info
# 口座残高の照会
def balance():
    info = cc.fetch_balance()
    return info
# 注文状況のデータ取得
def fetch_open_orders():
    info = cc.fetch_open_orders(
    symbol = "BTC/JPY",
    params = { "product_code" : "FX_BTC_JPY" }
    )
    return info
# 約定状況の確認
def my_trades():
    info = cc.fetch_my_trades(symbol='BTC/JPY')
    return info

# ポジション 買い:0 売り:1
position = 0
# 最後に約定したレート
last_rate = 0

# csvファイルの読み込み
# df = pd.read_csv('./data/btc.csv', index_col=0)s

while True:
    # coincheck = requests.get(URL).json()
    # rate = float(coincheck['rate'])
    # print(coincheck['rate'])

    # ratio = rate / rate_tmp

    # if rate > rate_tmp:
    #     print('Up : ' + str(ratio))
    # elif rate < rate_tmp:
    #     print('down : ' + str(ratio))
    # rate_tmp = rate

    a = buy_rate()
    pprint('買い'+ a['rate'])
    b = sell_rate()
    pprint('売り'+ b['rate'])
    c = base_rate()
    pprint('基準' + c['rate'])
    # pprint(exchange_status())
    # pprint(my_trades())
    d = ticker()
    print(d['last'])

    time.sleep(1)