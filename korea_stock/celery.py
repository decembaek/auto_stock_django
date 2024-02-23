# celery.py
import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

app = Celery("stock_auto_project_django")
# 문자열을 사용해서 Celery가 config를 설정하도록 합니다. namespace='CELERY'는
# 모든 Celery 관련 설정 키가 'CELERY_'로 시작해야 함을 의미합니다.
app.config_from_object("django.conf:settings", namespace="CELERY")
# Django 앱의 tasks.py에서 task를 자동으로 찾습니다.
app.autodiscover_tasks()
