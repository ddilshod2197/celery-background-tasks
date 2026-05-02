from celery import Celery
from celery.schedules import crontab

# Celery obyekti yaratish
app = Celery('tasks', broker='amqp://guest:guest@localhost//')

# Fon vazifa (background task) yaratish
@app.task
def send_email(subject, message, recipient):
    # Email yuborish uchun funksiya (masalan, smtplib yoki yuboruvchi xizmatidan foydalanish)
    # Bu yerda email yuborish uchun funksiya yozilmagan, lekin siz uni o'zgartirishingiz mumkin
    print(f"Email yuborildi: {subject} {message} {recipient}")

# Fon vazifa (background task) yaratish
@app.task
def update_database():
    # Mijozlar bazasini yangilash uchun funksiya (masalan, SQLAlchemy yoki Django ORM)
    # Bu yerda mijozlar bazasini yangilash uchun funksiya yozilmagan, lekin siz uni o'zgartirishingiz mumkin
    print("Mijozlar bazasi yangilandi")

# Fon vazifa (background task) yaratish
@app.task
def clean_cache():
    # Cache o'chirish uchun funksiya (masalan, Redis yoki Memcached)
    # Bu yerda cache o'chirish uchun funksiya yozilmagan, lekin siz uni o'zgartirishingiz mumkin
    print("Cache o'chirildi")

# Fon vazifa (background task) yaratish
@app.task
def schedule_tasks():
    # Fon vazifalarni takvimga qo'yish uchun funksiya
    app.conf.beat_schedule = {
        'send-email-every-minute': {
            'task': 'send_email',
            'schedule': crontab(minute='*/1'),  # Har bir daqiqa email yuborish
        },
        'update-database-every-hour': {
            'task': 'update_database',
            'schedule': crontab(hour='*/1'),  # Har bir soat mijozlar bazasini yangilash
        },
        'clean-cache-every-day': {
            'task': 'clean_cache',
            'schedule': crontab(hour='0', minute='0'),  # Kechasi 00:00 da cache o'chirish
        },
    }

# Fon vazifa (background task) boshqarish
if __name__ == '__main__':
    app.start()
```

Bu kodda, Celery obyekti yaratiladi va fon vazifalar yaratiladi. Fon vazifalar takvimga qo'yiladi va har bir vazifa bir necha daqiqa, soat yoki kunda boshqariladi.
