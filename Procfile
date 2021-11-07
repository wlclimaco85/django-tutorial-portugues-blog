release: python3 manage.py migrate --run-syncdb
release: python3 manage.py migrate
release: python3 makemigrations
web: gunicorn tutorialdjango.wsgi; --log-file -.
