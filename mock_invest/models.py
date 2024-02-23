from django.db import models
from django.conf import settings
from common.models import CommonModel
from tournament.models import Tournament

from korea_stock.models import StockCodeModel


# 모의투자 계좌
class MockInvestAccount(CommonModel):
    tournament = models.ForeignKey(
        Tournament, on_delete=models.CASCADE, null=True, blank=True
    )  # 토너먼트
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # 유저
    account_name = models.CharField(max_length=100)  # 계좌 이름
    initial_balance = models.DecimalField(
        max_digits=20, decimal_places=2, editable=False
    )  # 시작 금액
    current_balance = models.DecimalField(max_digits=20, decimal_places=2)  # 최근 금액


# 주식 포지션
class StockPostion(CommonModel):
    account = models.ForeignKey(
        MockInvestAccount, on_delete=models.CASCADE
    )  # 모의투자 계좌
    stock = models.ForeignKey(StockCodeModel, on_delete=models.CASCADE)  # 주식 코드
    stock_counts = models.PositiveIntegerField()  # 보유 주식 계수
    average_buy_price = models.DecimalField(
        max_digits=20, decimal_places=2
    )  # 주식 평균 매입가격


# 주식 거래 발생
class Transaction(CommonModel):
    TRANSACTION_TYPE_CHOICES = [
        ("BUY", "BUY"),
        ("SELL", "SELL"),
    ]
    account = models.ForeignKey(
        MockInvestAccount, on_delete=models.CASCADE
    )  # 모의투자 계좌
    stock = models.ForeignKey(StockCodeModel, on_delete=models.CASCADE)  # 주식 코드
    transaction_type = models.CharField(
        max_length=4, choices=TRANSACTION_TYPE_CHOICES
    )  # 매수, 매도 여부
    quantity = models.PositiveIntegerField()  # 거래된 주식의 수량
    price_per_share = models.DecimalField(
        max_digits=20, decimal_places=2
    )  # 주당 거래 가격
