from django.urls import path
from .views import schedule_list

urlpatterns = [
    path('list/', schedule_list.as_view())
]
