from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from django.forms import model_to_dict
from .models import Company
from users.models import User
from .serializers import company_serializer
import jwt, datetime
# Create your views here.
class CompanysView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')
        
        if not token:
            raise AuthenticationFailed('Unauthenticated!')
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')
        user = User.objects.filter(id=payload['id']).first()
        companys = Company.objects.filter(user=user)
        return Response({'company': company_serializer(companys, many=True).data})
    def post(self, request):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('Unauthenticated!')
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')
        user = User.objects.filter(id=payload['id']).first()
        
        company_new = Company.objects.create(
            user = user,
            name = request.data['name'],
            address = request.data['address'],
            city = request.data['city'],
            state = request.data['state'],
            country = request.data['country'],
            zipcode = request.data['zipcode'],
            phone = request.data['phone'],
            email = request.data['email'],
            website = request.data['website'],
            description = request.data['description']
        )
        company_new.save()
        return Response({'company': company_serializer(company_new).data})