
from rest_framework import serializers
from rest_framework.serializers import ReadOnlyField
from .models import Company
from users.models import User

class company_serializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"

    