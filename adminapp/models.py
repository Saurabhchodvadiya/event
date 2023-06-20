from django.db import models


class  User_details(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField()
    date_of_birth = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    first_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=20, blank=True)
    created_date = models.DateField(max_length=20, blank=True)
    updated_date = models.DateField(max_length=20, blank=True)
    is_active = models.BooleanField(default=1)
    is_admin = models.BooleanField(default=0)

class  User_detail(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField()
    date_of_birth = models.DateField(null=False, blank=True)
    password=   models.CharField(max_length=500,null=False)
    phone_number = models.CharField(max_length=20, blank=True)
    first_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=20, blank=True)
    created_date = models.DateTimeField(max_length=20, blank=True)
    updated_date = models.DateTimeField(max_length=20, blank=True)
    is_active = models.BooleanField(default=1)
    is_admin = models.BooleanField(default=0)


class create_event(models.Model):
    id = models.AutoField(primary_key=True)
    event_name=models.CharField(max_length=100,blank=False)
    start_Date=models.DateField(blank=False)
    end_Date=models.DateField(blank=False)
    total_participants = models.CharField(max_length=100)
    starting_time=models.TimeField(max_length=100,blank=False)
    ending_time=models.TimeField(max_length=100,blank=False)
    registered_participants=models.CharField(max_length=100, blank=True)
    # organizer_id = models.CharField(max_length=20, blank=True)
    organizer_id = models.ForeignKey(User_detail, on_delete=models.CASCADE)
    created_date = models.DateTimeField(max_length=20, blank=True)
    updated_date = models.DateTimeField(max_length=20, blank=True)
    is_active = models.BooleanField(default=1)
    updated_By_id= models.CharField(max_length=100,blank=True)
    deleted_By_id= models.CharField(max_length=100,blank=True)


