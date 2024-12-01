from django.utils.deprecation import MiddlewareMixin

class AdminSessionMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path.startswith('/admin/'):
            # Set admin session configuration
            request.META['session_cookie_name'] = 'admin_sessionid'
            request.META['session_engine'] = 'django.contrib.sessions.backends.cache'
        else:
            # Set default API session configuration
            request.META['session_cookie_name'] = 'api_sessionid'
            request.META['session_engine'] = 'django.contrib.sessions.backends.db'
