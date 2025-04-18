from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import(
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
    TokenBlacklistView
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api_1_3.urls')),
    path('api_admin/', include('api_admin.urls')),
    path('auth/', include('api_auth.urls')),
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
    path('api/token/verify/', TokenVerifyView.as_view()),
    path('api/token/blacklist/', TokenBlacklistView.as_view()),


]
