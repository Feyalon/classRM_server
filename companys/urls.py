from django.urls import path
from .views import CompanysView

urlpatterns = [
    path('/', CompanysView.as_view())
]