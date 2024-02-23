from django.conf import settings
from django.db import models

from common.models import CommonModel


# 토너먼트
class Tournament(CommonModel):
    name = models.CharField(max_length=100)  # 토너먼트 대회 이름
    description = models.TextField(null=True, blank=True)  # 대회 설명
    tournament_balance = models.DecimalField(
        max_digits=20, decimal_places=2, editable=False
    )  # 대회 소유 금액
    month_period = models.PositiveIntegerField(default=1)  # 대회 기간 (달 단위)
    start_date = models.DateField()  # 대회 시작날
    end_date = models.DateField()  # 대회 종료날
    is_active = models.BooleanField(default=True)  # 대회 종료 여부 True시 진행 중


class Participant(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)  # 토너먼트
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # 유저
    rank = models.PositiveIntegerField(null=True, blank=True)  # 참가자 순위
    score = models.DecimalField(
        max_digits=20, decimal_places=2, null=True, blank=True
    )  # 최종 모의투자 금액
