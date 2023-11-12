
from rest_framework import serializers
from rest_framework.serializers import ReadOnlyField
from .models import Leads
from users.models import User
class leads_serializer(serializers.ModelSerializer):
    class Meta:
        model = Leads
        fields = "__all__"