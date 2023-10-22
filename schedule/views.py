from django.shortcuts import render
from rest_framework import generics
from .models import Schedule
from rest_framework.views import APIView
from rest_framework.response import Response
from django.forms import model_to_dict

# Create your views here.
class schedule_list(APIView):
    def get(self, request):
        lst = Schedule.objects.all().values()
        return Response({'users': list(lst)})