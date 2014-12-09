from .base import *

DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dee5f8d4q9lu6u',
        'USER' : 'rydrhratkcssoo',
        'PASSWORD' : '8tmxtWDpPKC_fbw1IFXDNfbmeD',
        'HOST' : 'ec2-54-197-240-180.compute-1.amazonaws.com',
        'PORT' : '5432',
    }
}

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR.child('static')]
STATIC_ROOT = 'staticfiles'

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