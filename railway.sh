python manage.py migrate & gunicorn datamagnum.wsgi & celery -A datamagnum worker --uid 999 --pool=solo -l INFO &
celery -A datamagnum beat -l INFO 