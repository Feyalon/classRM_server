
from django.contrib import admin
from django.urls import path, include, re_path
from users import urls as user_urls
from schedule import urls as schedule_urls
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from leads import urls as leads_urls
from companys import urls as companys_urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include(user_urls)),
    path('api/companys', include(companys_urls)),
    path('api/leads/', include(leads_urls))
]
