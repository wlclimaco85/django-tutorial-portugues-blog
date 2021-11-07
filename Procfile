
release: python3 manage.py migrate
release: python3 manage.py makemigrations 
release: python3 manage.py migrate
web: gunicorn tutorialdjango.wsgi; --log-file -.