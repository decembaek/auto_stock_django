"""
kospi, kosdap 종목 정보 info 데이터 넣기 

"""

import os
from pathlib import Path
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()
# 시크릿 키 숨기기 django-environ
# Django-environ 설치하고 사용하기 !
# import environ

import pandas as pd
from korea_stock.models import StockCodeModel

from dotenv import load_dotenv

load_dotenv()
# env = environ.Env()
import json
import requests
import time

# TEST_KEY = os.environ.get("TEST_APP_KEY")
# TEST_SECRET = os.environ.get("TEST_APP_SECRET")
APP_KEY = os.environ.get("APP_KEY")
APP_SECRET = os.environ.get("APP_SECRET")
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

REAL_URL_BASE = "https://openapi.koreainvestment.com:9443"
# TEST_URL_BASE = "https://openapivts.koreainvestment.com:29443"

REALTIME_WEBSOCKET_URL = "/oauth2/Approval"
# HASH_KEY_URL = "/uapi/hashkey"
TOKEN_URL = "/oauth2/tokenP"
# PRICE_NOW_URL = "/uapi/domestic-stock/v1/quotations/inquire-price"
STOCK_INFO_URL = "/uapi/domestic-stock/v1/quotations/search-stock-info"

json_headers = {"content-type": "application/json"}
token_body = {
    "grant_type": "client_credentials",
    "appkey": APP_KEY,
    "appsecret": APP_SECRET,
}

# TOKEN 발급이 필요하면 True로 하기
token_bool = False

if token_bool:
    token_res = requests.post(
        REAL_URL_BASE + TOKEN_URL,
        headers=json_headers,
        data=json.dumps(token_body),
        # timeout 요청 시간 제한
        timeout=10,
    )

    ACCESS_TOKEN = token_res.json()["access_token"]
    # JSON 파일로 저장
    with open("ACCESS_TOKEN.json", "w") as json_file:
        json.dump({"ACCESS_TOKEN": ACCESS_TOKEN}, json_file, indent=4)
else:
    with open("ACCESS_TOKEN.json", "r") as json_file:
        data = json.load(json_file)
        ACCESS_TOKEN = data["ACCESS_TOKEN"]

print(ACCESS_TOKEN)

headers = {
    "content-type": "application/json",
    "authorization": ACCESS_TOKEN,
    "appkey": APP_KEY,
    "appsecret": APP_SECRET,
    "tr_id": "CTPF1002R",
    "custtype": "P",
}
params = {
    "PRDT_TYPE_CD": "300",
    "PDNO": None,
}

all_code = StockCodeModel.objects.all()

for code in all_code:
    code_num = code.code
    params["PDNO"] = code_num
    # res = requests.get(
    #     REAL_URL_BASE + STOCK_INFO_URL,
    #     headers=headers,
    #     params=params,
    #     timeout=10,
    # )
    # print(type(code_num))
