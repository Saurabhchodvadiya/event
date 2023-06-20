from rest_framework import serializers
from .models import register_event
from adminapp.models import create_event
import re
from utils.pattern import mobile_no,email,bod,name,password
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
class register_event_serializer(serializers.ModelSerializer):
    class Meta:
        model = register_event
        fields = '__all__'
class update_participant_serializer(serializers.ModelSerializer):
    class Meta:
        model = create_event
        fields = ['registered_participants']