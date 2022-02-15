from django.urls import path
from .apiView import LoginAPIView, RegisterUser, BlacklistTokenAdding
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/login/', LoginAPIView.as_view(), name='login_user'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/logout/blacklist/', BlacklistTokenAdding.as_view(), name='blacklist'),
    path('api/register/', RegisterUser.as_view(), name="register_new_user"),
]