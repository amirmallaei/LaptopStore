python manage.py makemigrations user&&
python manage.py migrate user &&
celery -A config.celery worker -l INFO -B & 
python manage.py runserver 0.0.0.0:8000