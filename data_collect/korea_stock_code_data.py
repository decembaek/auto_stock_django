"""
kospi, kosdap 종목 정보 데이터 넣기 

"""

import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

import pandas as pd
from korea_stock.models import StockCodeModel


def load_data_from_excel(excel_path):
    # Excel 파일 읽기
    df = pd.read_excel(excel_path, engine="openpyxl")

    # 데이터프레임의 각 행을 반복 처리
    for _, row in df.iterrows():
        print("CODE", row["code"])
        # date = row["stock_open_date"]
        # date.split("/")
        face_value = row["face_value"]
        if face_value == "무액면":
            face_value = 0
        StockCodeModel.objects.create(
            standard_code=row["standard_code"],
            code=row["code"],
            name=row["name"],
            stock_name=row["stock_name"],
            en_name=row["en_name"],
            stock_open_date=row["stock_open_date"].replace("/", "-"),
            market=row["market"],
            stock_kind=row["stock_kind"],
            affiliated=row["affiliated"],
            stock_type=row["stock_type"],
            face_value=face_value,
            total_stock_count=row["total_stock_count"],
        )


# Excel 파일 경로
excel_path = "data/stock_data.xlsx"

load_data_from_excel(excel_path)
