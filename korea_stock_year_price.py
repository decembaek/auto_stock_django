import os
from pathlib import Path
import django
import pandas as pd

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from dotenv import load_dotenv

load_dotenv()
# env = environ.Env()
import json
import requests
import time

from korea_stock.models import StockCodeModel, StockPriceHistory

APP_KEY = os.environ.get("APP_KEY")
APP_SECRET = os.environ.get("APP_SECRET")
TEST_APP_KEY = os.environ.get("TEST_APP_KEY")
TEST_APP_SECRET = os.environ.get("TEST_APP_SECRET")
# Build paths inside the project like this: BASE_DIR / 'subdir'.
REAL_URL_BASE = "https://openapi.koreainvestment.com:9443"
TEST_URL_BASE = "https://openapivts.koreainvestment.com:29443"

REALTIME_WEBSOCKET_URL = "/oauth2/Approval"
TOKEN_URL = "/oauth2/tokenP"
PRICE_URL = "/uapi/domestic-stock/v1/quotations/inquire-daily-itemchartprice"

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


headers = {
    "content-type": "application/json",
    "authorization": "Bearer " + ACCESS_TOKEN,
    "appkey": APP_KEY,
    "appsecret": APP_SECRET,
    "tr_id": "FHKST03010100",
}

stock_code = None
start_date = None
end_date = None

params = {
    "FID_COND_MRKT_DIV_CODE": "J",
    "FID_INPUT_ISCD": stock_code,
    "FID_INPUT_DATE_1": start_date,
    "FID_INPUT_DATE_2": end_date,
    "FID_PERIOD_DIV_CODE": "Y",
    "FID_ORG_ADJ_PRC": "0",
}


all_code = StockCodeModel.objects.all()

# time 모듈을 사용하여 현재 시간을 구하고, 이를 구조화된 시간 형태로 변환
current_time = time.localtime()

# 구조화된 시간을 사용하여 오늘 날짜를 '년-월-일' 형식의 문자열로 포맷
today_date = time.strftime("%Y%m%d", current_time)

# print(today_date)

# # StockPriceHistory
# 최대 100건 까지 지만, 년 단위는 한 방에 될듯
for code in all_code:
    code_num = code.code
    start_date = code.stock_open_date
    params["FID_INPUT_ISCD"] = code_num
    params["FID_INPUT_DATE_1"] = start_date  # 상장일
    params["FID_INPUT_DATE_2"] = today_date  # 오늘 날짜

    res = requests.get(
        REAL_URL_BASE + PRICE_URL,
        headers=headers,
        params=params,
        timeout=10,
    )
    result = res.json()
    output2 = result["output2"]
    for output in output2:
        date = output["stck_bsop_date"]
        year = date[0:4]
        month = date[4:6]
        day = date[6:8]
        format_date = f"{year}-{month}-{day}"
        StockPriceHistory.objects.create(
            stock=code,  # 종목코드
            period="Y",  # 기간 단위 Y 년 단위 저장
            date=format_date,  # 날짜 yyyy-mm-dd
            # time="", # 시간 년 단위라 빈칸으로 데이터 삽입
            open_price=output["stck_oprc"],
            close_price=output["stck_clpr"],
            high_price=output["stck_hgpr"],
            low_price=output["stck_lwpr"],
            volume=output["acml_vol"],
            accumulate_money=output["acml_tr_pbmn"],
            flng_cls_code=output["flng_cls_code"],
            prtt_rate=output["prtt_rate"],
            mod_yn=output["mod_yn"],
            prdy_vrss_sign=output["prdy_vrss_sign"],
            prdy_vrss=output["prdy_vrss"],
            revl_issu_reas=output["revl_issu_reas"],
        )
    # break  # 일단 종목 1개만 저장하기
