from .base import *

DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'Discusiones',
        'USER' : 'cursodjango',
        'PASSWORD' : '123',
        'HOST' : 'localhost',
        'PORT' : '5432',
    }
}

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR.child('static')]

SOCIAL_AUTH_FACEBOOK_KEY = '1010466688980093'
SOCIAL_AUTH_FACEBOOK_SECRET = 'df673bf66276aa0cff6b85a7697395cd'

SOCIAL_AUTH_TWITTER_KEY = '0KC68MgQRRFGik5eNSSIhKrZy'
SOCIAL_AUTH_TWITTER_SECRET = 'Msfh1YslH1LL2q91P2cemPvIHm5MdUFKNT82Yqvz5KKBReHv4m'

MANDRILL_API_KEY = 'CmyN_ELx1JSKaEEm5qWv0A'


CACHES = {
	'default' : {
		'BACKEND' : 'redis_cache.RedisCache',
		#'LOCATION' : 'grideye.redistogo.com:10097',
		'LOCATION' : 'localhost:6379',
		'OPTIONS' : {
			'DB' : 1,
			#'PASSWORD' : 'asdas6d87sf6tsd8f',
		}
	}
}