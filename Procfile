release: python3 manage.py migrate --run-syncdb
release: python3 manage.py migrate
release: python3 makemigrations
release: python3 migrate blog
release: python3 migrate users
web: gunicorn tutorialdjango.wsgi; --log-file -.
