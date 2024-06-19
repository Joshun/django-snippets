# Add the following to settings.py:

class DisableCSRF:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user_agent = request.headers.get('user-agent', '')
        if user_agent.startswith('insomnia') or user_agent.startswith('PostmanRuntime') or user_agent.startswith('curl'):
            setattr(request, '_dont_enforce_csrf_checks', True)
        response = self.get_response(request)
        return response


if DEBUG:
    # INSTALLED_APPS = INSTALLED_APPS + ['debug_toolbar']
    # debug_toolbar's middleware wants to be first
    # MIDDLEWARE = ['debug_toolbar.middleware.DebugToolbarMiddleware'] + MIDDLEWARE

    MIDDLEWARE = ['djproject.settings.web_interface.DisableCSRF'] + MIDDLEWARE
