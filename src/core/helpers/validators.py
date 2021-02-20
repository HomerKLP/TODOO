BASE_MODULE = 'django.contrib.auth.password_validation'

DEFAULT_VALIDATORS = (
    {
        'NAME': f'{BASE_MODULE}.UserAttributeSimilarityValidator'
    }, {
        'NAME': f'{BASE_MODULE}.MinimumLengthValidator'
    }, {
        'NAME': f'{BASE_MODULE}.CommonPasswordValidator',
    }, {
        'NAME': f'{BASE_MODULE}.NumericPasswordValidator',
    }
)
