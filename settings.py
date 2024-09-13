ALLOWED_HOSTS = ['djangokhatri.onrender.com', 'www.djangokhatri.onrender.com']
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('SECRET_KEY', 'your-default-secret-key')
DEBUG = os.getenv('DEBUG', 'False') == 'True'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME', 'mydatabase'),
        'USER': os.getenv('DB_USER', 'mydatabaseuser'),
        'PASSWORD': os.getenv('DB_PASSWORD', 'mypassword'),
        'HOST': os.getenv('DB_HOST', 'localhost'),
        'PORT': os.getenv('DB_PORT', '5432'),
    }
}
