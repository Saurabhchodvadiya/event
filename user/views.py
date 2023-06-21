from django.shortcuts import render
from django.shortcuts import render
from django.http import JsonResponse
from .models import User_detail
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from django.utils import timezone
from django.contrib.auth.hashers import check_password
# Create your views here.
from rest_framework_simplejwt.tokens import RefreshToken
from event_management.settings import SECRET_KEY
from rest_framework.decorators import api_view
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.backends import BaseBackend
from adminapp.models import User_detail,create_event
from rest_framework.permissions import AllowAny
import jwt
from datetime import datetime,date


@api_view(['post'])
@permission_classes((AllowAny,))
def register_user_event_Api(request):
    try:
        token = request.META.get('HTTP_AUTHORIZATION').split(' ')[1]
        payload = dict(jwt.decode(jwt=token, key=SECRET_KEY, algorithms=['HS256']))
        user = User_detail.objects.filter(id=payload["user_id"],is_active=1)
        if user.exists()==False:
            return Response({'status':False,
                                'msg':"Data not found"
                }, status=400)

        else:
            user_data=request.data
            event_data=create_event.objects.filter(id=user_data["event_id"],is_active=1)
            register_Event_data=register_event.objects.filter(user_id=payload["user_id"],event_id=user_data["event_id"],is_active=1)
            if register_Event_data.exists():
                return Response({'status':False,
                                'msg':"You are already participated in this event"
                }, status=400)
            if event_data.exists()==False:
                return Response({'status':False,
                                'msg':"Event Not Found"
                }, status=400)

           
            user = event_data.first()
            if str(user.start_Date)<str(date.today()):
                return Response({'status':False,
                                'msg':"Registration is closed"
                }, status=400)

            participants_number=int(user.registered_participants)+1
            data={"registered_participants":participants_number}
            if participants_number>int(user.total_participants):
                return Response({'status':False,
                                'msg':"Contest is full"
                }, status=400)
            if user:
                # remove_serializer = remove_event_Data(user)
                security_serializer = update_participant_serializer(
                user, data=data)
            if security_serializer.is_valid():
                security_serializer.save()
            user_data["created_date"]=timezone.now()
            user_data["updated_date"]=timezone.now()
            user_data["user_id"]=payload["user_id"]
            user_data["is_active"]=1

            
            serializer = register_event_serializer(data=user_data)
            if serializer.is_valid():
                serializer.save()
                return Response({"status":True,"msg":"Data Added Successfully"}, status=200)
            return Response(serializer.errors, status=400)
    except Exception  as e:
        return Response({"status":False,"msg":str(e)}, status=500)
    

