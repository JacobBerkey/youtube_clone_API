SECRET_KEY = 'django-insecure-ccgk9(vrf9cu!t=ajtqz7yq=!!fszlk#q&*iswq^=5tfws519k'

DATABASES = {
    'default': {
        'ENGINE': 'mysqlconnector.django',
        'NAME': 'youtube_clone_api',
        'USER': 'root',
        'PASSWORD': 'toor',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True
        }
    }
}