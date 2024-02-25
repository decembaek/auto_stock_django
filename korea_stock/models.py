from django.db import models

from common.models import CommonModel


# Create your models here.


# 테마코드
# 테마명
# 표준산업분류코드
# 004 반도체/반도체장비	029460
class KSICCodeModel(models.Model):
    theme_code = models.CharField(default="", max_length=100)  # 테마코드
    theme_name = models.CharField(default="", max_length=200)  # 테마명
    ksic_code = models.CharField(default="", max_length=100)  # 표준산업분류코드


# 업종코드   업종명
# 1001	01KOSDAQ
class KisSectorModel(models.Model):
    sector_code = models.CharField(
        default="", max_length=50, primary_key=True
    )  # 업종 코드
    sector_name = models.CharField(default="", max_length=200)  # 업종명


# 주식 종목 코드 모델
class StockCodeModel(models.Model):
    standard_code = models.CharField(default="", max_length=50)  # 표준코드
    code = models.CharField(default="", max_length=50, primary_key=True)  # 단축코드
    name = models.CharField(default="", max_length=100)  # 한글 종목명
    stock_name = models.CharField(default="", max_length=100)  # 한글 종목약명
    en_name = models.CharField(default="", max_length=100)  # 영문 종목명
    stock_open_date = models.DateField()  # 상장일
    market = models.CharField(default="", max_length=50)  # 시장 구분
    stock_kind = models.CharField(default="", max_length=30)  # 증권 구분
    affiliated = models.CharField(default="", max_length=30)  # 소속부
    stock_type = models.CharField(default="", max_length=30)  # 주식종류
    face_value = models.DecimalField(max_digits=10, decimal_places=2)  # 액면가
    total_stock_count = models.DecimalField(
        max_digits=20, decimal_places=2
    )  # 상장주식수


# 주식 기본 정보 모델
class StockInfoModel(models.Model):
    stock_code = models.ForeignKey(StockCodeModel, on_delete=models.CASCADE, null=True)
    tr_id = models.CharField(default="", max_length=100)  # 요청한 tr_id
    rt_cd = models.CharField(default="", max_length=2)  # 성공여부
    msg_cd = models.CharField(default="", max_length=20)  # 응답코드
    msg1 = models.CharField(default="", max_length=150)  # 응답 메세지
    # output = models.TextField(default="")  # 응답 상세1
    pdno = models.CharField(default="", max_length=100)  # 상품번호
    prdt_type_cd = models.CharField(default="", max_length=20)  # 상품유형코드
    mket_id_cd = models.CharField(default="", max_length=20)  # 시장 ID 코드
    scty_grp_id_cd = models.CharField(default="", max_length=20)  # 증권그룹ID 코드
    excg_dvsn_cd = models.CharField(default="", max_length=20)  # 거래소구분코드
    setl_mmdd = models.CharField(default="", max_length=10)  # 결산월일
    lstg_stqt = models.CharField(default="", max_length=50)  # 상장주수
    lstg_cptl_amt = models.CharField(default="", max_length=50)  # 상장 자본 금액
    cpta = models.CharField(default="", max_length=50)  # 자본금
    papr = models.CharField(default="", max_length=50)  # 액면가
    issu_pric = models.CharField(default="", max_length=50)  # 발행가격
    kospi200_item_yn = models.CharField(
        default="", max_length=50
    )  # 코스피 200 종목 여부
    scts_mket_lstg_dt = models.CharField(
        default="", max_length=50
    )  # 유가증권시장상장일자
    scts_mket_lstg_abol_dt = models.CharField(
        default="", max_length=50
    )  # 유가증권시장 상장폐지 일자
    kosdaq_mket_lstg_dt = models.CharField(
        default="", max_length=50
    )  # 코스닥 시장 상장 일자
    kosdaq_mket_lstg_abol_dt = models.CharField(
        default="", max_length=50
    )  # 코스닥 시장 상장 폐지 일자
    frbd_mket_lstg_dt = models.CharField(
        default="", max_length=50
    )  # 프리보드시장 상장일자
    frbd_mket_lstg_abol_dt = models.CharField(
        default="", max_length=50
    )  # 프로비도시장 상장폐지 일자
    reits_kind_cd = models.CharField(default="", max_length=50)  # 리츠종류코드
    etf_dvsn_cd = models.CharField(default="", max_length=50)  # ETF구분코드
    oilf_fund_yn = models.CharField(default="", max_length=50)  # 유전펀드여부
    idx_bztp_lcls_cd = models.CharField(
        default="", max_length=50
    )  # 지수업종대부류 코드
    idx_bztp_mcls_cd = models.CharField(
        default="", max_length=50
    )  # 지수업종중분류 코드
    idx_bztp_scls_cd = models.CharField(
        default="", max_length=50
    )  # 지수업종소분류 코드
    stck_kind_cd = models.CharField(default="", max_length=50)  # 주식종류코드
    mfnd_opng_dt = models.CharField(default="", max_length=50)  # 뮤추얼펀드 개시일자
    mfnd_end_dt = models.CharField(default="", max_length=50)  # 뮤추얼펀드 종료일자
    dpsi_erlm_cncl_dt = models.CharField(default="", max_length=50)  # 예탁등록취소 일자
    etf_cu_qty = models.CharField(default="", max_length=50)  # ETFCU 수량
    prdt_name = models.CharField(default="", max_length=100)  # 상품명
    prdt_name120 = models.CharField(default="", max_length=300)  # 상품명 120
    prdt_abrv_name = models.CharField(default="", max_length=200)  # 상품약어명
    std_pdno = models.CharField(default="", max_length=50)  # 표준상품번호
    prdt_eng_name = models.CharField(default="", max_length=100)  # 상품영문명
    prdt_eng_name120 = models.CharField(default="", max_length=300)  # 상품영문명120
    prdt_eng_abrv_name = models.CharField(default="", max_length=100)  # 상품영문약어명
    dpsi_aptm_erlm_yn = models.CharField(default="", max_length=10)  # 예탁지정등록여부
    etf_txtn_type_cd = models.CharField(default="", max_length=100)  # ETF 과세유형코드
    etf_type_cd = models.CharField(default="", max_length=100)  # ETF 유형코드
    lstg_abol_dt = models.CharField(default="", max_length=10)  # 상장폐지일자
    nwst_odst_dvsn_cd = models.CharField(
        default="", max_length=100
    )  # 신주구주구분 코드
    sbst_pric = models.CharField(default="", max_length=100)  # 대용가격
    thco_sbst_pric = models.CharField(default="", max_length=100)  # 당사 대용가격
    thco_sbst_pric_chng_dt = models.CharField(
        default="", max_length=100
    )  # 당사 대용가격 변경일자
    tr_stop_yn = models.CharField(default="", max_length=100)  # 거래 정지여부
    admn_item_yn = models.CharField(default="", max_length=100)  # 관리종목여부
    thdt_clpr = models.CharField(default="", max_length=100)  # 당일종가
    bfdy_clpr = models.CharField(default="", max_length=100)  # 전일종가
    clpr_chng_dt = models.CharField(default="", max_length=100)  # 종가변경일자
    std_idst_clsf_cd = models.CharField(default="", max_length=100)  # 표준산업분류코드
    sstd_idst_clsf_code = models.ForeignKey(
        KSICCodeModel, on_delete=models.CASCADE, null=True
    )  # 표준산업분류코드 FK
    std_idst_clsf_cd_name = models.CharField(
        default="", max_length=300
    )  # 표준산업분류 코드명
    idx_bztp_lcls_cd_name = models.CharField(
        default="", max_length=200
    )  # 지수업종대분류 코드명
    idx_bztp_mcls_cd_name = models.CharField(
        default="", max_length=200
    )  # 지수업종중분류 코드명
    idx_bztp_scls_cd_name = models.CharField(
        default="", max_length=200
    )  # 지수업종소분류 코드명
    ocr_no = models.CharField(default="", max_length=10)  # OCR 번호
    crfd_item_yn = models.CharField(default="", max_length=10)  # 크라우드펀딩 종목여부
    elec_scty_yn = models.CharField(default="", max_length=10)  # 전자증권여부
    updated_at = models.DateTimeField(auto_now=True)  # update time


class StockPriceRealtimeModel(CommonModel):
    pass


# class StockPriceHistory(models.Model):
#     stock = models.ForeignKey(
#         "StockCodeModel", on_delete=models.CASCADE, related_name="price_history"
#     )
#     date = models.DateField()
#     open_price = models.DecimalField(max_digits=10, decimal_places=2)
#     high_price = models.DecimalField(max_digits=10, decimal_places=2)
#     low_price = models.DecimalField(max_digits=10, decimal_places=2)
#     close_price = models.DecimalField(max_digits=10, decimal_places=2)
#     volume = models.BigIntegerField()

#     class Meta:
#         indexes = [
#             models.Index(fields=["date"]),
#         ]
#         unique_together = ("stock", "date")

#     def __str__(self):
#         return f"{self.stock} on {self.date}"
