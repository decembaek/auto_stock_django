import os
from pathlib import Path
import pandas as pd
import json
import requests
import time
from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta

import django
from django.db.models import Max

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from korea_stock.models import StockCodeModel, StockPriceHistory

from dotenv import load_dotenv

load_dotenv()
# env = environ.Env()


# 데이터 초기화
# StockPriceHistory.objects.filter(period="M").delete()
# exit()

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
    "FID_PERIOD_DIV_CODE": "M",
    "FID_ORG_ADJ_PRC": "0",
}


all_code = StockCodeModel.objects.all()

# time 모듈을 사용하여 현재 시간을 구하고, 이를 구조화된 시간 형태로 변환
current_time = time.localtime()

# 구조화된 시간을 사용하여 오늘 날짜를 '년-월-일' 형식의 문자열로 포맷
today_date = time.strftime("%Y%m%d", current_time)
print(today_date)

# print(today_date)

# # StockPriceHistory
# 최대 100건 까지 지만, 년 단위는 한 방에 될듯

# 데이터 저장 기준
period = "M"

# 현재 날짜 설정
today = datetime.now().strftime("%Y-%m-%d")
print(today)
# 종료 조건을 확인하기 위한 변수
all_data_up_to_date = True
# While 문으로 최신 날짜까지 DB 저장하기
# break 문 짜야할듯
while True:
    # 데이터가 이미 있으면, 그 다음달부터 데이터 가져오기
    for code in all_code:
        # print(code)
        code_num = code.code
        start_date = code.stock_open_date
        # print(start_date)

        stock_price_record_obj_date = StockPriceHistory.objects.filter(
            stock=code,
            period=period,
        ).aggregate(Max("date"))["date__max"]

        if stock_price_record_obj_date:
            if stock_price_record_obj_date.strftime("%Y-%m-%d") >= today:
                # 데이터가 이미 최신이면 다음 종목으로 넘어감
                print(f"Data for {code} is up to date.")
                continue
            # 마지막 날짜가 존재하는 경우, 해당 날짜 출력
            # print(f"Last stock price record for {code}: {stock_price_record_obj_date}")

            # DB에 값 있을경우 이어서 DB 저장하기 위한 코드
            start_date = stock_price_record_obj_date

            # 기존 날짜
            # original_date_str = start_date
            # original_date = datetime.strptime(start_date, "%Y-%m-%d")
            original_date = start_date

            # 100개월 후 계산
            months_later = 100
            target_date = original_date + relativedelta(months=+months_later)

            end_date_target = target_date.strftime("%Y%m%d")

        else:
            # 마지막 날짜가 존재하지 않는 경우, 즉 쿼리셋이 비어 있는 경우
            # print(f"No stock price records found for {code}")
            # 기존 날짜
            # original_date_str = start_date
            # original_date = datetime.strptime(start_date, "%Y-%m-%d")
            original_date = start_date

            # 100개월 후 계산
            months_later = 100
            target_date = original_date + relativedelta(months=+months_later)

            end_date_target = target_date.strftime("%Y%m%d")
        print(f"CODE {code_num} start {start_date} end {end_date_target}")
        # 데이터가 최신이 아닌 경우, all_data_up_to_date를 False로 설정
        all_data_up_to_date = False

        params["FID_INPUT_ISCD"] = code_num
        params["FID_INPUT_DATE_1"] = start_date  # 상장일, 또는 최신 저장일
        params["FID_INPUT_DATE_2"] = end_date_target  # 오늘 날짜, 또는 100일 더하기
        print(f"CODE {code_num} start {start_date} end {end_date_target}")
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
                period=period,  # 기간 단위 Y 년 단위 저장
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

    # 모든 종목에 대한 처리가 완료되면, all_data_up_to_date가 여전히 True면 루프 종료
    if all_data_up_to_date:
        break
    else:
        # 다음 반복을 위해 all_data_up_to_date를 다시 True로 설정
        all_data_up_to_date = True


## 마지막달 조회가 02-29로 나오고 현재 날짜 3월2일이라서 무한 루트돔, 방법 찾아보기
