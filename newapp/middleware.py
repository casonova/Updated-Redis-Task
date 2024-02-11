from django.core.cache import cache
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer


class UserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            user = request.user
            user_groups = user.groups.all()
            request_key = (
                f"user {user.username} request_count"
            )
            request_count = cache.get(request_key)
            
            print(request_key)
            print(request_count)

            if request_count is None:
                cache.set(request_key, 0, 60)
                request_count = 0

            request_limit = 0

            for group in user_groups:
                if group.name == "Gold":
                    request_limit = 10
                    break
                elif group.name == "Bronze":
                    request_limit = 5
                    break
                elif group.name == "Silver":
                    request_limit = 2
                    break
                   
            if request_count < request_limit:
                cache.set(request_key, request_count + 1, 60)
            else:
                response_data = {"msg": "Too many requests, you are blocked"}
                renderer = JSONRenderer()
                rendered_response = renderer.render(response_data)
                return HttpResponse(
                    rendered_response, content_type="application/json", status=429
                )

        response = self.get_response(request)
        return response
