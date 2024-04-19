from rest_framework.authentication import TokenAuthentication
from django.utils import timezone


class CustomAuthentication(TokenAuthentication):
    def authenticate(self, request):
        if "token" in request.query_params and "HTTP_AUTHORIZATION" not in request.META:
            auth_token = request.query_params.get("token")
            token = self.authenticate_credentials(auth_token)
        else:
            token = super().authenticate(request)

        if token is None:
            return None

        user, token = token
        token.created = timezone.now()
        token.save()

        user.last_login = timezone.now()
        user.save()

        return user, token
