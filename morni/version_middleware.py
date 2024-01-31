from django.http import HttpResponsePermanentRedirect
from .settings import CURRENT_VERSION

class ApiVersionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/api/') and not request.path.startswith('/api/v'):
            # Redirect to the default version (v1)
            new_path = '/api/{}/{}'.format(CURRENT_VERSION, request.path[len('/api/'):])
            return HttpResponsePermanentRedirect(new_path)

        response = self.get_response(request)
        return response
