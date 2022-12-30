from celery import shared_task


@shared_task
def debug_task(x):
    print(f"print x : {x}")
