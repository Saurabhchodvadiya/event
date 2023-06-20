
from django.urls import path,include
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('',Create_user.as_view(),name='Create_user' ),
    path('login',login,name='login' ),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
     path('api/token/convert/', convert_refresh_token, name='convert_refresh_token'),
     path('create_event', create_event_Api, name='create_event'),
     path('get_all_event', get_all_event, name='get_all_event'),
     path('get-event-by-id/<int:id>/', get_event_by_id, name='get_event_by_id'),
     path('get-event-by-user-id/<int:id>/', get_event_by_user_id, name='get_event_by_user_id'),
     path('update-event-by-id/<int:id>/', update_event_by_id, name='update_event_by_id'),
     path('remove-event-by-id/<int:id>/', remove_event_by_id, name='remove_event_by_id'),
        path('get-all-user', get_all_user, name='get_all_user'),
        path('get-user-id/<int:id>/', get_user_id, name='get_user_id'),
         path('get_user_detail_by_event/<int:id>/', get_user_detail_by_event, name='get_user_detail_by_event'),
                  path('get_participated_user_detail_by_event/<int:id>/', get_participated_user_detail_by_event, name='get_participated_user_detail_by_event'),
                  path('user_participated_event/<int:id>/', user_participated_event, name='user_participated_event'),
                                    path('remove_user_from_event/<int:id>/', remove_user_from_event, name='remove_user_from_event'),
]
