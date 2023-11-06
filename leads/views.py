from django.shortcuts import render
from .models import Leads
from rest_framework.views import APIView
from rest_framework.response import Response
from django.forms import model_to_dict
from rest_framework.exceptions import AuthenticationFailed

class leads_list(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('Unauthenticated!')
        lst = Leads.objects.all().values()
        return Response({'leads': list(lst)})
    def post(self, request):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('Unauthenticated!')
        user_new = Leads.objects.create(
            name = request.data['name'],
            email = request.data['email'],
            phone = request.data['phone'],
            message = request.data['message'],
            age = request.data['age'],
            date_birthday = request.data['date_birthday'],
            newsletter = request.data['newsletter'],
            auto_letter = request.data['auto_letter'],
        )
        user_new.save()
        return Response({'users': model_to_dict(user_new)})