import environ

from tutorialdjango.settings.base import *

env = environ.Env()

DEBUG = env.bool("DEBUG", true)

SECRET_KEY = env("SECRET_KEY")

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")

DATABASES = {
    "default": env.db(),
}
