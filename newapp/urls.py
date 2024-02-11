from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import UserView

urlpatterns = [
    path(
        "users/", UserView.as_view({"get": "list", "post": "create"}), name="user-list"
    ),
    path(
        "users/<int:pk>/",
        UserView.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}),
        name="user-detail",
    ),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
