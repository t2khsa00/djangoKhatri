ALLOWED_HOSTS = ['djangokhatri.onrender.com', 'www.djangokhatri.onrender.com']

import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY', 'default-secret-key')
DEBUG = os.getenv('DEBUG', 'False') == 'True'
