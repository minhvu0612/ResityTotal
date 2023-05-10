# api/resity_api/serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import RegistationCenterAdmin, Owner, Car, RegistationDoc

class RegistationCenterAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistationCenterAdmin
        fields = ["center_name", "area", "city"]

class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = ["fullname", "password", "email", "phone", "indenty", "birthday", "accommodation", "place_of_birth"]

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ["type", "producer", "code", "registation_day", "plate", "registation_area", "uses", "owner_id"]

class RegistationDocSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistationDoc
        fields = ["code", "start_day", "end_day", "car_id", "center_id"]

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "email"]