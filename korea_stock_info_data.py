"""
kospi, kosdap 종목 정보 info 데이터 넣기 

"""

import os
from pathlib import Path
import django

# 시크릿 키 숨기기 django-environ
# Django-environ 설치하고 사용하기 !
import environ

import pandas as pd
from korea_stock.models import StockCodeModel

from dotenv import load_dotenv

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

load_dotenv()
env = environ.Env()

TEST_KEY = os.environ.get("TEST_APP_KEY")
TEST_SECRET = os.environ.get("TEST_APP_SECRET")
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# environ.Env.read_env(f"{BASE_DIR}/.env")
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))
all_code = StockCodeModel.objects.all()

for code in all_code:
    code_num = code.code
    print(code_num)
