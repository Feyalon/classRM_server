from django.shortcuts import render
from .models import Leads
from rest_framework.views import APIView
from rest_framework.response import Response
from django.forms import model_to_dict
from rest_framework.exceptions import AuthenticationFailed
from users.models import User
from companys.models import Company
import jwt, datetime
from .serializers import leads_serializer
class leads_list(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')
        
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')
        if not token:
            raise AuthenticationFailed('Unauthenticated!')
        user = User.objects.filter(id=payload['id']).first()
        lst = Leads.objects.filter(user=user)
        return Response({'leads': leads_serializer(lst, many=True).data})
    def post(self, request):
        token = request.COOKIES.get('jwt')
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')
        
        company_id = request.data['company_id']
        print(company_id)
        user = User.objects.filter(id=payload['id']).first()
        company = Company.objects.filter(user=user)
        company_capital = company[company_id]
        print(company_capital)
        print(company)
        if not token:
            raise AuthenticationFailed('Unauthenticated!')
        user_new = Leads.objects.create(
            user = user,
            name = request.data['name'],
            email = request.data['email'],
            phone = request.data['phone'],
            message = request.data['message'],
            age = request.data['age'],
            date_birthday = request.data['date_birthday'],
            newsletter = request.data['newsletter'],
            auto_letter = request.data['auto_letter'],
            company_name = company_capital
        )
        user_new.save()
        return Response({'leads': model_to_dict(user_new)})