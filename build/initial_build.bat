

rmdir quick_django_db_venv /S /Q

call python -m venv quick_django_db_venv
call quick_django_db_venv\Scripts\activate

call pip install -r requirements.txt


cd quick_django_db

REM echo from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@admin.com', '353e@$3245%#', first_name='admin', last_name='admin') | python manage.py shell

call python manage.py makemigrations
call python manage.py migrate

call python manage.py createsuperuser

call python manage.py runserver 127.0.0.1:8000
