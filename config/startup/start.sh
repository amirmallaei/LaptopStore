python manage.py makemigrations &&
python manage.py migrate &&
celery -A config.celery worker -l INFO -B & 
python manage.py runserver 0.0.0.0:8000