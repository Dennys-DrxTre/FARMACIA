from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

MYSQL = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Project',
        'USER': 'root',
        'PASSWORD': 'R04m1l*',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

SQLITE3 = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}