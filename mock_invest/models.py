from django.db import models
from django.conf import settings
from common.models import CommonModel


# Create your models here.
# 모의투자 계좌
class MockInvestAccount(CommonModel):
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


# from django.db import models
# from django.conf import settings

# class MockInvestmentAccount(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='investment_accounts')
#     account_name = models.CharField(max_length=100)
#     initial_balance = models.DecimalField(max_digits=15, decimal_places=2)
#     current_balance = models.DecimalField(max_digits=15, decimal_places=2)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return f"{self.account_name} - {self.user.username}"

# class StockPosition(models.Model):
#     account = models.ForeignKey(MockInvestmentAccount, on_delete=models.CASCADE, related_name='positions')
#     stock = models.ForeignKey('StockCodeModel', on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField()
#     average_buy_price = models.DecimalField(max_digits=10, decimal_places=2)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return f"{self.stock.stock_code} - {self.quantity} shares"

# class Transaction(models.Model):
#     TRANSACTION_TYPE_CHOICES = [
#         ('BUY', 'Buy'),
#         ('SELL', 'Sell'),
#     ]

#     account = models.ForeignKey(MockInvestmentAccount, on_delete=models.CASCADE, related_name='transactions')
#     stock = models.ForeignKey('StockCodeModel', on_delete=models.CASCADE)
#     transaction_type = models.CharField(max_length=4, choices=TRANSACTION_TYPE_CHOICES)
#     quantity = models.PositiveIntegerField()
#     price_per_share = models.DecimalField(max_digits=10, decimal_places=2)
#     transaction_date = models.DateTimeField()
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.transaction_type} - {self.stock.stock_code} - {self.quantity} shares"
