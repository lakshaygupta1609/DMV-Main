from django.contrib import admin
from django.urls import path
from homepage.models import contact_db, view_license_db, apply_licenses_db, branch_db, exam_result_db, exam_db, law_db, vehicle_db, Profile, traffic_offence_db
from homepage import views 

urlpatterns = [
    path('',views.homepage, name='homepage'),
    path('about', views.about, name='about'),
    path('contact',views.contact, name='contact'),
    path('user_login', views.user_login, name='user_login'),
    path('register', views.register, name='register'),
    path('user_logout', views.user_logout, name="user_logout"),
    path('apply_license', views.apply_license, name='apply_license'),
    path('branches', views.branches, name='branches'),
    path('check_exam', views.check_exam, name='check_exam'),
    path('check_license', views.check_license, name='check_license'),
    path('exam_dates', views.exam_dates, name='exam_dates'),
    path('laws', views.laws, name='laws'),
    path('registered_vehicles', views.registered_vehicles, name='registered_vehicles'),
    path('traffic_offences', views.traffic_offences, name='traffic_offences'),
    path('check_license', views.check_license,name='check_license')


]
