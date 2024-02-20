"""
# 테마코드
# 테마명
# 표준산업분류코드

데이터 넣기

"""

import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

import pandas as pd
from korea_stock.models import KSICCodeModel


def load_data_from_excel(excel_path):
    # Excel 파일 읽기
    df = pd.read_excel(excel_path, engine="openpyxl")

    # 데이터프레임의 각 행을 반복 처리
    for _, row in df.iterrows():
        # row["엑셀 위 데이터"]
        # face_value = row["face_value"]
        print(row)
        KSICCodeModel.objects.create(
            theme_code=row["theme_code"],
            theme_name=row["theme_name"],
            ksic_code=row["ksic_code"],
        )


# Excel 파일 경로
excel_path = "data/theme_code.xlsx"

load_data_from_excel(excel_path)
