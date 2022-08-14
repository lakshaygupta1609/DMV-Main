from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime

class contact_db(models.Model):
    email = models.CharField(max_length=30)
    desc = models.TextField()
    date = models.DateTimeField()
    support_type = models.CharField(max_length=30, default= 'Help')
    title = models.CharField(max_length=30, default='Help')

    def __str__(self):
        return self.title

class view_license_db(models.Model):
    license_choices=(('Learner', 'Learner'), ('Two-Wheeler', 'Two-Wheeler'), ('Four-Wheeler', 'Four-Wheeler'))
    citizenship = models.CharField(max_length=30)
    license_type = models.CharField(max_length=30,choices=license_choices)
    expiry_date = models.DateField()

class apply_licenses_db(models.Model):
    license_types=(('Learner', 'Learner'), ('Two-Wheeler', 'Two-Wheeler'), ('Four-Wheeler', 'Four-Wheeler'))
    name = models.CharField(max_length=30)
    citizenship = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    application_date = models.DateTimeField()
    applicant_email = models.CharField(max_length=30)
    license_type = models.CharField(max_length=30)
    exam_datetime=models.CharField(max_length=30)

class branch_db(models.Model):
    location=models.CharField(max_length=30)
    branch_name = models.CharField(max_length=30)
    hours = models.CharField(max_length=30)

class exam_db(models.Model):
    branch_name=models.CharField(max_length=30, default='-')
    location=models.CharField(max_length=30)
    exam_date = models.DateField(default=datetime.date.today)
    exam_time = models.TimeField(default=datetime.time(00, 00))

class exam_result_db(models.Model):
    citizenship=models.CharField(max_length=10, default='1234567890')
    exam_choices=(('Passed', 'Passed'),('Failed', 'Failed'))
    exam_result=models.CharField(max_length=10, choices=exam_choices, default='Failed')
    location=models.CharField(max_length=30)
    exam_time = models.DateTimeField()
    exam_type_choices=(('Written','Written'),('Practical','Practical'))
    exam_type=models.CharField(max_length=10,default='Written', choices=exam_type_choices)

class law_db(models.Model):
    pdf_link = models.CharField(max_length=256)
    law_name=models.CharField(max_length=30)
    law_date=models.DateTimeField()

class vehicle_db(models.Model):
    vehicle_types=(('Two-Wheeler', 'Two-Wheeler'), ('Four-Wheeler', 'Four-Wheeler'), ('Many-Wheeler', 'Many-Wheeler'))
    vehicle_model = models.CharField(max_length=30)
    citizenship = models.CharField(max_length=30, default='1234567890')
    vehicle_type = models.CharField(max_length=15,choices=vehicle_types, default='Two-Wheeler')
    license_plate = models.CharField(max_length=30)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    citizenship = models.CharField(max_length=30, default="1234567890")

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class traffic_offence_db(models.Model):
    fee_status_choice=(('Unpaid','Unpaid'),('Paid','Paid'))
    citizenship = models.CharField(max_length=30)
    offence_type=models.CharField(max_length=30)
    due_fine=models.CharField(max_length=30)
    offence_date=models.DateTimeField()
    offence_location=models.CharField(max_length=30)
    officer_name=models.CharField(max_length=30, default=' ')
    fee_status=models.CharField(max_length=30,choices=fee_status_choice, default='Unpaid')


