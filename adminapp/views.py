from django.shortcuts import render
from django.http import JsonResponse
from .models import User_detail
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import Userdetails_serializer,get_user_Data,remove_event_data_Serializer,event_data_Serializer,register_event_data_Serializer,eventdetails_serializer,get_event_Data,remove_event_Data
from django.utils import timezone
from django.contrib.auth.hashers import check_password
# Create your views here.
from user.serializers import * 
from rest_framework_simplejwt.tokens import RefreshToken
from event_management.settings import SECRET_KEY
from rest_framework.decorators import api_view
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.backends import BaseBackend
from .models import User_detail,create_event
from rest_framework.permissions import AllowAny
import jwt
class Create_user(APIView):
    def post(self, request):
        try:
            user_data=request.data
            user_data["is_active"]=1
            user_data["created_date"]=timezone.now()
            user_data["updated_date"]=timezone.now()
            email=User_detail.objects.filter(email=user_data["email"])
            if email.exists():
                return Response({"status":False,"msg":"Email Already Available In Our Database"}, status=400)
            phone_number=User_detail.objects.filter(phone_number=user_data["phone_number"])
            if phone_number.exists():
                return Response({"status":False,"msg":"Phone Number Already Available In Our Database"}, status=400)
            serializer = Userdetails_serializer(data=user_data)
            if serializer.is_valid():
                serializer.save()
                return Response({"status":True,"msg":"Data Added Successfully"}, status=200)
            return Response(serializer.errors, status=400)
        except Exception as e:
            return Response({"status":False,"msg":str(e)}, status=500)

@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')

    try:
        user = User_detail.objects.filter(email=email)
        if  user.exists()==False:
            return Response({'status':False,
                             'msg':"Data not found"
            }, status=400)
        user=user.first()
        if check_password(password, user.password):
            refresh = RefreshToken.for_user(user)
            return Response({'status':True,
                             'msg':"Login Sucessfully",
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        else:
            return Response({'status':False,
                             'msg':"Invalid password"
            }, status=400)
    except Exception  as e:
        return Response({"status":False,"msg":str(e)}, status=500)
    
@api_view(['POST'])
def convert_refresh_token(request):
    try:
        refresh_token = request.data.get('refresh_token')

        if refresh_token:
            refresh = RefreshToken(refresh_token)
            access_token = refresh.access_token
            return Response({"status":True,'access_token': str(access_token)})
        else:
            return Response({"status":False,"msg":'Invalid refresh token.'}, status=400)

    except Exception  as e:
        return Response({"status":False,"msg":str(e)}, status=500)

class CustomUserBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            user = User_detail.objects.get(email=email)
            if user.check_password(password):
                return user
        except User_detail.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User_detail.objects.get(pk=user_id)
        except User_detail.DoesNotExist:
            return None

# @api_view(['post'])
# @permission_classes((AllowAny,))
# def create_event(request):
#     token = request.META.get('HTTP_AUTHORIZATION').split(' ')[1]
#     payload = dict(jwt.decode(jwt=token, key=SECRET_KEY, algorithms=['HS256']))
#     user = User_detail.objects.filter(id=payload["user_id"],is_active=1,is_admin=1)
#     if user.exists()==False:
#         return Response({'status':False,
#                              'msg':"Data not found"
#             }, status=400)

#     else:
#         user_data=request.data
#         user_data["is_active"]=1
#         user_data["created_date"]=timezone.now()
#         user_data["updated_date"]=timezone.now()
#         user_data["organizer_id"]=payload["user_id"]
#         user_data["registered_participants"]=None
#         serializer = eventdetails_serializer(data=user_data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"status":True,"msg":"Data Added Successfully"}, status=200)
#         return Response(serializer.errors, status=400)


@api_view(['post'])
@permission_classes((AllowAny,))
def create_event_Api(request):
    try:
        status, payload=decode_function(request)
        if status==False:
            return Response({'status':False,
                                'msg':"Data not found"
                }, status=400)

        else:
            user_data=request.data
            user_data["is_active"]=1
            user_data["created_date"]=timezone.now()
            user_data["updated_date"]=timezone.now()
            user_data["organizer_id"]=payload["user_id"]
            user_data["registered_participants"]=0
            serializer = eventdetails_serializer(data=user_data)
            if serializer.is_valid():
                serializer.save()
                return Response({"status":True,"msg":"Data Added Successfully"}, status=200)
            return Response(serializer.errors, status=400)
    except Exception  as e:
        return Response({"status":False,"msg":str(e)}, status=500)
    

def decode_function(request):
    token = request.META.get('HTTP_AUTHORIZATION').split(' ')[1]
    payload = dict(jwt.decode(jwt=token, key=SECRET_KEY, algorithms=['HS256']))
    user = User_detail.objects.filter(id=payload["user_id"],is_active=1,is_admin=1)
    if user.exists()==False:
        return False,payload
    else:
        return True,payload

@api_view(['get'])
@permission_classes((AllowAny,))
def get_all_event(request):
    try:
        status, payload=decode_function(request)
        if status==False:
            return Response({'status':False,
                                'msg':"Data not found"
                }, status=400)

        else:
            user = create_event.objects.filter(is_active=1)
            serializer = get_event_Data(user.all(),many=True)
            serialized_data = serializer.data
            return Response({'status':True,
                                'msg':"Data Recived Successfully","data":serialized_data})
    except Exception  as e:
        return Response({"status":False,"msg":str(e)}, status=500)
@api_view(['get'])
@permission_classes((AllowAny,))
def get_event_by_id(request,id):
    try:
        token = request.META.get('HTTP_AUTHORIZATION').split(' ')[1]
        payload = dict(jwt.decode(jwt=token, key=SECRET_KEY, algorithms=['HS256']))
        user = User_detail.objects.filter(id=payload["user_id"],is_active=1)
        if user.exists()==False:
            return Response({'status':False,
                                'msg':"Data not found"
                }, status=400)

        else:
      
            user = create_event.objects.get(is_active=1,id=id)
            
            serializer = get_event_Data(user, many=False)
            
                
            serialized_data = serializer.data
            return Response({'status':True,
                                'msg':"Data Recived Successfully","data":serialized_data})
        # return Response(serialized_data)
    except Exception  as e:
        return Response({"status":False,"msg":str(e)}, status=500)
    
@api_view(['get'])
@permission_classes((AllowAny,))
def get_event_by_user_id(request,id):
    try:
        token = request.META.get('HTTP_AUTHORIZATION').split(' ')[1]
        payload = dict(jwt.decode(jwt=token, key=SECRET_KEY, algorithms=['HS256']))
        user = User_detail.objects.filter(id=payload["user_id"],is_active=1)
        if user.exists()==False:
            return Response({'status':False,
                                'msg':"Data not found"
                }, status=400)

        else:
            
            user = create_event.objects.filter(is_active=1,organizer_id=id)
            
            serializer = get_event_Data(user.all(), many=True)
            
                
            serialized_data = serializer.data
            return Response({'status':True,
                                'msg':"Data Recived Successfully","data":serialized_data})
    except Exception  as e:
        return Response({"status":False,"msg":str(e)}, status=500)

# from .models import YourModel

def update_model_instance(instance, data_dict):
    for key, value in data_dict.items():
        setattr(instance, key, value)
    instance.save()


@api_view(['put'])
@permission_classes((AllowAny,))
def update_event_by_id(request,id):
    try:
        status, payload=decode_function(request)
        if status==False:
            return Response({'status':False,
                                'msg':"Data not found"
                }, status=400)

        else:
            # import pdb
            # pdb.set_trace()
            # 
            event = create_event.objects.filter(is_active=1,id=id)
            if event.exists()==False:
                
                return Response({'status':False,
                                    'msg':"Data not found"
                    }, status=400)
            data=request.data
            event=event.first()
            # event = create_event.objects.get(is_active=1,id=id)
            for k,v  in list(data.items()):
                if v is None:
                    del request[k]
            data['updated_date'] =timezone.now()
            data['updated_By_id'] =payload["user_id"]
            if data["total_participants"]:
                data['registered_participants'] =int(data["total_participants"])-int(event.registered_participants)
                if data['registered_participants']<0:
                    return Response({'status':False,
                                    'msg':"You can't change max participate number"
                    }, status=400)

            # df = pd.DataFrame([company_data])
            # final_df = compare_data_with_db(df, company_data['company_code'])
            # if final_df.empty:
            #     response = {
            #         "status": 400,
            #         "msg": "Company Name or ISIN code may be duplicate",
            #         "data": "please check name and ISIN code"
            #     }
            #     return JsonResponse(response, status=200, safe=False)
            # company_data = final_df.to_dict("records")[0]

            update_model_instance(event, data)
            
            return Response({'status':True,
                             'msg':"Data Updated Successfully"})
    except Exception  as e:
        return Response({"status":False,"msg":str(e)}, status=500)




@api_view(['put'])
@permission_classes((AllowAny,))
def remove_event_by_id(request,id):
    try:
        status, payload=decode_function(request)
        if status==False:
            return Response({'status':False,
                                'msg':"Data not found"
                }, status=400)

        else:
            events = create_event.objects.filter(is_active=1,id=id)
            if events.exists()==False:
                
                return Response({'status':False,
                                    'msg':"Data not found"
                    }, status=400)
            user = events.first()
            data={"is_active":0,"deleted_By_id":payload["user_id"]}
            if user:
                # remove_serializer = remove_event_Data(user)
                security_serializer = remove_event_Data(
                user, data=data)
            if security_serializer.is_valid():
                security_serializer.save()
            return Response({'status':True,
                             'msg':"Data Removed Successfully"})
    except Exception  as e:
        return Response({"status":False,"msg":str(e)}, status=500)
    

@api_view(['put'])
@permission_classes((AllowAny,))
def remove_event_by_id(request,id):
    try:
        status, payload=decode_function(request)
        if status==False:
            return Response({'status':False,
                                'msg':"Data not found"
                }, status=400)

        else:
            events = create_event.objects.filter(is_active=1,id=id)
            if events.exists()==False:
                
                return Response({'status':False,
                                    'msg':"Data not found"
                    }, status=400)
            user = events.first()
            data={"is_active":0,"deleted_By_id":payload["user_id"]}
            if user:
                # remove_serializer = remove_event_Data(user)
                security_serializer = remove_event_Data(
                user, data=data)
            if security_serializer.is_valid():
                security_serializer.save()
            return Response({'status':True,
                             'msg':"Data Removed Successfully"})
    except Exception  as e:
        return Response({"status":False,"msg":str(e)}, status=500)
    

   
@api_view(['get'])
@permission_classes((AllowAny,))
def get_all_user(request):
    try:
        status, payload=decode_function(request)
        if status==False:
            return Response({'status':False,
                                'msg':"Data not found"
                }, status=400)

        else:
            
            user = User_detail.objects.filter(is_active=1,is_admin=0)
            
            serializer = get_user_Data(user.all(), many=True)
            
                
            serialized_data = serializer.data
            return Response({'status':True,
                                'msg':"Data Recived Successfully","data":serialized_data})
    except Exception  as e:
        return Response({"status":False,"msg":str(e)}, status=500)
    

@api_view(['get'])
@permission_classes((AllowAny,))
def get_user_id(request,id):
    try:
        status, payload=decode_function(request)
        if status==False:
            return Response({'status':False,
                                'msg':"Data not found"
                }, status=400)

        else:
            
            user = User_detail.objects.filter(id=id,is_active=1,is_admin=0)
            
            serializer = get_user_Data(user.all(), many=True)
            
                
            serialized_data = serializer.data
            return Response({'status':True,
                                'msg':"Data Recived Successfully","data":serialized_data})
    except Exception  as e:
        return Response({"status":False,"msg":str(e)}, status=500)
from django.db.models import Prefetch   
from django.core import serializers
@api_view(['get'])
@permission_classes((AllowAny,))
def get_user_detail_by_event(request,id):
    try:
        status, payload=decode_function(request)
        if status==False:
            return Response({'status':False,
                                'msg':"Data not found"
                }, status=400)

        else:
            
            # user = create_event.objects.select_related('register_event')
            result = create_event.objects.select_related('organizer_id').filter(id=id)
            
            serializer = event_data_Serializer(result.all(), many=True)
            
                
            serialized_data = serializer.data
            return Response({'status':True,
                                'msg':"Data Recived Successfully","data":serialized_data})
                
            # serialized_data = serializer.data
           
    except Exception  as e:
        return Response({"status":False,"msg":str(e)}, status=500)
from user.models import register_event
@api_view(['get'])
@permission_classes((AllowAny,))
def get_participated_user_detail_by_event(request,id):
    try:
        status, payload=decode_function(request)
        if status==False:
            return Response({'status':False,
                                'msg':"Data not found"
                }, status=400)

        else:
            
            # user = create_event.objects.select_related('register_event')
            result = register_event.objects.select_related('event_id').filter(event_id__id=id)
            
            serializer = register_event_data_Serializer(result.all(), many=True)
            
                
            serialized_data = serializer.data
            return Response({'status':True,
                                'msg':"Data Recived Successfully","data":serialized_data})
                
            # serialized_data = serializer.data
           
    except Exception  as e:
        return Response({"status":False,"msg":str(e)}, status=500)
    

from user.models import register_event
@api_view(['get'])
@permission_classes((AllowAny,))
def user_participated_event(request,id):
    try:
        status, payload=decode_function(request)
        if status==False:
            return Response({'status':False,
                                'msg':"Data not found"
                }, status=400)

        else:
            
            # user = create_event.objects.select_related('register_event')
            result = register_event.objects.select_related('user_id').filter(user_id__id=id)
            
            serializer = register_event_data_Serializer(result.all(), many=True)
            
                
            serialized_data = serializer.data
            return Response({'status':True,
                                'msg':"Data Recived Successfully","data":serialized_data})
                
            # serialized_data = serializer.data
           
    except Exception  as e:
        return Response({"status":False,"msg":str(e)}, status=500)
    
# select a.snapshot_date,a.fund_id,a.SEC_NUM_OF_SHARE,a.SEC_MARKET_VALUE,a.SEC_WEIGHT,a.SEC_COUPON_RATE,a.SECURITY_ID,a.TABLE_FLAG,
# b.SECURITY_UNITS,
# b.PAR_VALUE,
# b.SECURITY_ISSUSERCOND_DESC,
# b.SECURITY_ISSUSERCOND_ISSUERCAT,
# b.LONG_SHORT_POSITION,
# b.NOTIONAL_AMOUNT,
# b.NUMBER_OF_SHARE_CONTRACT,
# b.FITCH_LONG_RATING,
# b.FITCH_SHORT_RATING,
# b.MOODYS_LONG_RATING,
# b.MOODYS_SHORT_RATING,
# b.SANDP_LONG_RATING,
# b.SANDP_SHORT_RATING,
# b.YIELDSEC_AS_OF_REPORTING_DATE
# from DPA_FDP_DEV_V2.FUNDTRANS_ASREPORTEDHOLDING b
# inner join  DPA_FDP_DEV_V2.SECMASTER_STANDARDPENDING a on a.fund_id=b.fund_id and a.snapshot_date=b.snapshot_date and a.import_file_id=b.import_file_id and a.holding_type=b.data_type
# where b.import_file_id=3346995




@api_view(['put'])
@permission_classes((AllowAny,))
def remove_user_from_event(request,id):
    try:
        status, payload=decode_function(request)
        if status==False:
            return Response({'status':False,
                                'msg':"Data not found"
                }, status=400)

        else:
            user_data=request.data
            
            event_data=create_event.objects.filter(id=user_data["event_id"],is_active=1)
            register_Event_data=register_event.objects.filter(user_id=id,event_id=user_data["event_id"],is_active=1)
            if  register_Event_data.exists() ==False:
                return Response({'status':False,
                                'msg':"user_is_not_available"
                }, status=400)
            if event_data.exists()==False:
                return Response({'status':False,
                                'msg':"Event Not Found"
                }, status=400)

           
            user = event_data.first()
           
            for k,v  in list(user_data.items()):
                if v is None:
                    del user_data[k]
            participants_number=int(user.registered_participants)-1
            
            data={"registered_participants":participants_number}
            security_serializer = update_participant_serializer(
            user, data=data)
            if security_serializer.is_valid():
                security_serializer.save()
            data={"is_active":0}
            if user:
                # remove_serializer = remove_event_Data(user)
                security_serializer = remove_event_data_Serializer(
                user, data=data)
            if security_serializer.is_valid():
                security_serializer.save()
          
                return Response({'status':True,
                                    'msg':"User Removed Successfully"
                    }) 
            return Response(security_serializer.errors, status=400)
            
        
    except Exception  as e:
        return Response({"status":False,"msg":str(e)}, status=500)