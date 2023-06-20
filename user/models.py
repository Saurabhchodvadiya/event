from django.db import models
from adminapp.models import *
# Create your models here.
class register_event(models.Model):
    id = models.AutoField(primary_key=True)
    event_id = models.ForeignKey(create_event, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User_detail, on_delete=models.CASCADE)
    created_date = models.DateTimeField(max_length=20, blank=True)
    updated_date = models.DateTimeField(max_length=20, blank=True)
    is_active = models.BooleanField(default=1)
    updated_By_id= models.CharField(max_length=100,blank=True)
    deleted_By_id= models.CharField(max_length=100,blank=True)