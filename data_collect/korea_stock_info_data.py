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
from korea_stock.models import StockInfoModel, KSICCodeModel, StockCodeModel

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
    "authorization": "Bearer " + ACCESS_TOKEN,
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
    res = requests.get(
        REAL_URL_BASE + STOCK_INFO_URL,
        headers=headers,
        params=params,
        timeout=10,
    )
    result = res.json()
    print(code_num)
    output = result["output"]
    ksic = output["std_idst_clsf_cd"]
    print(ksic)
    try:
        ksic_model = KSICCodeModel.objects.get(ksic_code=ksic)
    except:
        ksic_model = None
    print(ksic_model)
    StockInfoModel.objects.create(
        stock_code=code,
        tr_id="CTPF1002R",
        rt_cd=result["rt_cd"],
        msg_cd=result["msg_cd"],
        msg1=result["msg1"],
        # output
        pdno=output["pdno"],
        prdt_type_cd=output["prdt_type_cd"],
        mket_id_cd=output["mket_id_cd"],
        scty_grp_id_cd=output["scty_grp_id_cd"],
        excg_dvsn_cd=output["excg_dvsn_cd"],
        setl_mmdd=output["setl_mmdd"],
        lstg_stqt=output["lstg_stqt"],
        lstg_cptl_amt=output["lstg_cptl_amt"],
        cpta=output["cpta"],
        papr=output["papr"],
        issu_pric=output["issu_pric"],
        kospi200_item_yn=output["kospi200_item_yn"],
        scts_mket_lstg_dt=output["scts_mket_lstg_dt"],
        scts_mket_lstg_abol_dt=output["scts_mket_lstg_abol_dt"],
        kosdaq_mket_lstg_dt=output["kosdaq_mket_lstg_dt"],
        kosdaq_mket_lstg_abol_dt=output["kosdaq_mket_lstg_abol_dt"],
        frbd_mket_lstg_dt=output["frbd_mket_lstg_dt"],
        frbd_mket_lstg_abol_dt=output["frbd_mket_lstg_abol_dt"],
        reits_kind_cd=output["reits_kind_cd"],
        etf_dvsn_cd=output["etf_dvsn_cd"],
        oilf_fund_yn=output["oilf_fund_yn"],
        idx_bztp_lcls_cd=output["idx_bztp_lcls_cd"],
        idx_bztp_mcls_cd=output["idx_bztp_mcls_cd"],
        idx_bztp_scls_cd=output["idx_bztp_scls_cd"],
        stck_kind_cd=output["stck_kind_cd"],
        mfnd_opng_dt=output["mfnd_opng_dt"],
        mfnd_end_dt=output["mfnd_end_dt"],
        dpsi_erlm_cncl_dt=output["dpsi_erlm_cncl_dt"],
        etf_cu_qty=output["etf_cu_qty"],
        prdt_name=output["prdt_name"],
        prdt_name120=output["prdt_name120"],
        prdt_abrv_name=output["prdt_abrv_name"],
        std_pdno=output["std_pdno"],
        prdt_eng_name=output["prdt_eng_name"],
        prdt_eng_name120=output["prdt_eng_name120"],
        prdt_eng_abrv_name=output["prdt_eng_abrv_name"],
        dpsi_aptm_erlm_yn=output["dpsi_aptm_erlm_yn"],
        etf_txtn_type_cd=output["etf_txtn_type_cd"],
        etf_type_cd=output["etf_type_cd"],
        lstg_abol_dt=output["lstg_abol_dt"],
        nwst_odst_dvsn_cd=output["nwst_odst_dvsn_cd"],
        sbst_pric=output["sbst_pric"],
        thco_sbst_pric=output["thco_sbst_pric"],
        thco_sbst_pric_chng_dt=output["thco_sbst_pric_chng_dt"],
        tr_stop_yn=output["tr_stop_yn"],
        admn_item_yn=output["admn_item_yn"],
        thdt_clpr=output["thdt_clpr"],
        bfdy_clpr=output["bfdy_clpr"],
        clpr_chng_dt=output["clpr_chng_dt"],
        std_idst_clsf_cd=output["std_idst_clsf_cd"],
        sstd_idst_clsf_code=ksic_model,  # FKey
        std_idst_clsf_cd_name=output["std_idst_clsf_cd_name"],
        idx_bztp_lcls_cd_name=output["idx_bztp_lcls_cd_name"],
        idx_bztp_mcls_cd_name=output["idx_bztp_mcls_cd_name"],
        idx_bztp_scls_cd_name=output["idx_bztp_scls_cd_name"],
        ocr_no=output["ocr_no"],
        crfd_item_yn=output["crfd_item_yn"],
        elec_scty_yn=output["elec_scty_yn"],
    )
    print("complete")
