from django.db import models

from common.models import CommonModel


# Create your models here.
class StockCodeModel(models.Model):
    standard_code = models.CharField(default="", max_length=50)
    code = models.CharField(default="", max_length=50, primary_key=True)
    name = models.CharField(default="", max_length=100)
    stock_name = models.CharField(default="", max_length=100)
    en_name = models.CharField(default="", max_length=100)
    stock_open_date = models.DateField()
    market = models.CharField(default="", max_length=50)
    stock_kind = models.CharField(default="", max_length=30)
    affiliated = models.CharField(default="", max_length=30)
    stock_type = models.CharField(default="", max_length=30)
    face_value = models.DecimalField(max_digits=10, decimal_places=2)
    total_stock_count = models.DecimalField(max_digits=20, decimal_places=2)


class StockInfoModel(models.Model):
    pass


class StockPriceRealtimeModel(CommonModel):
    pass
