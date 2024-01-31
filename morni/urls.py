from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views

main_patterns = [
    path('admin/', admin.site.urls),
    path('api/v1/login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/login/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]

from services.v1 import urls as services_v1_urls
version_1_patterns = [
    path('api/v1/services/', include(services_v1_urls)),
]

urlpatterns = main_patterns + version_1_patterns
