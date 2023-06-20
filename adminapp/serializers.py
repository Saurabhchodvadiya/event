from rest_framework import serializers
from .models import User_detail,create_event
import re
from utils.pattern import mobile_no,email,bod,name,password
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from user.models import *
class Userdetails_serializer(serializers.ModelSerializer):
    class Meta:
        model = User_detail
        fields = '__all__'
    def validate(self, data):
        # Perform validation that requires multiple fields
        if not re.match(mobile_no, data['phone_number']):
 
            raise serializers.ValidationError("Invalid phone number")
        if not re.match(email, data['email']):
 
            raise serializers.ValidationError("Invalid Email")
        # if not re.match(bod, data['date_of_birth']):
 
        #     raise serializers.ValidationError("Invalid phone number")
        if not re.match(name, data['first_name']):
 
            raise serializers.ValidationError("Invalid First Name")
        if not re.match(name, data['last_name']):
 
            raise serializers.ValidationError("Invalid Last Name")
        if not re.match(password, data['password']):
 
            raise serializers.ValidationError("Invalid Last Name")
        else:
            data['password']=make_password(data['password'])
        return data


from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.id
        # Add more custom claims if needed

        return token
    

class eventdetails_serializer(serializers.ModelSerializer):
    class Meta:
        model = create_event
        fields = '__all__'
    def validate(self, data):
        # Perform validation that requires multiple fields
        if str(data['start_Date'])>str(data['end_Date']):
            raise serializers.ValidationError("Invalid Start and End Date")

        
        return data
    
class get_event_Data(serializers.ModelSerializer):
    class Meta:
        model = create_event
        fields = '__all__'

class remove_event_Data(serializers.ModelSerializer):
    class Meta:
        model = create_event
        fields = ['is_active']


class get_user_Data(serializers.ModelSerializer):
    class Meta:
        model = User_detail
        fields = '__all__'


class event_data_Serializer(serializers.ModelSerializer):
    class Meta:
        model = create_event
        fields = '__all__'
        depth = 1


class register_event_data_Serializer(serializers.ModelSerializer):
    class Meta:
        model = register_event
        fields ='__all__'
        depth = 1


class remove_event_data_Serializer(serializers.ModelSerializer):
    class Meta:
        model = register_event
        fields =['is_active']
        