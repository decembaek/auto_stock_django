"""
## 업종섹터코드

"""

import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

import pandas as pd
from korea_stock.models import KisSectorModel


def load_data_from_excel(excel_path):
    # Excel 파일 읽기
    df = pd.read_excel(excel_path, engine="openpyxl")

    # 데이터프레임의 각 행을 반복 처리
    for _, row in df.iterrows():
        # row["엑셀 위 데이터"]
        # face_value = row["face_value"]
        print(row)
        KisSectorModel.objects.create(
            sector_code=row["sector_code"],
            sector_name=row["sector_name"],
        )


# Excel 파일 경로
excel_path = "data/idxcode.xlsx"

load_data_from_excel(excel_path)
