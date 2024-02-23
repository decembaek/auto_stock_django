from celery import shared_task, Celery

app = Celery("tasks", broker="redis://localhost:6379/0")


@shared_task
def my_task():
    # 비동기로 수행할 작업을 작성합니다.
    print("Hello Task")


@app.task
def add(x, y):
    return x + y
