release: python3 manage.py migrate --run-syncdb
release: python3 manage.py migrate
release: python3 makemigrations
release: python3 manage.py migrate blog
release: python3 manage.py migrate blog
web: gunicorn tutorialdjango.wsgi; --log-file -.
