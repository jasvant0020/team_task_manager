web: bash -c "python manage.py migrate && python manage.py collectstatic --noinput && gunicorn project.wsgi --workers 1 --threads 2 --timeout 120"
