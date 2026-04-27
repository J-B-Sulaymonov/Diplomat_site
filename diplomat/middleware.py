from django.conf import settings

class ForceDefaultLanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        language_cookie_name = getattr(settings, 'LANGUAGE_COOKIE_NAME', 'django_language')
        if 'HTTP_ACCEPT_LANGUAGE' in request.META and not request.COOKIES.get(language_cookie_name):
            # If the user hasn't explicitly set a language preference (no cookie)
            # we remove the browser's preference to force use of settings.LANGUAGE_CODE
            del request.META['HTTP_ACCEPT_LANGUAGE']
        
        return self.get_response(request)
