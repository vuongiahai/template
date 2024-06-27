# run_task.py
import os
from celery import Celery

# Đặt biến môi trường để Celery có thể tìm thấy cấu hình Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pos.settings')

# Tạo đối tượng Celery và cấu hình, không cần autodiscover_tasks() ở đây
app = Celery('pos')
app.config_from_object('django.conf:settings', namespace='CELERY')

if __name__ == '__main__':
    # Import task cần chạy
    from pos.tasks import add
    
    # Gọi task
    result = add.delay(4, 5)
    print(f"Task ID: {result.id}")
