from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from homepage.models import contact_db, view_license_db, apply_licenses_db, branch_db, exam_result_db, exam_db, law_db, vehicle_db, Profile, traffic_offence_db
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def homepage(request):
    return render(request,'homepage.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        email=request.POST.get('email')
        desc=request.POST.get('desc')
        support_type = request.POST.get('support_type')
        title = request.POST.get('title')
        contact = contact_db(desc=desc, email=email, date=datetime.now(), support_type=support_type, title=title)
        contact.save()
        messages.success(request, 'Your message has been sent.')

    return render(request, 'contact.html')

def user_login(request):
    if request.method == 'POST':
        login_email=request.POST.get('email')
        login_password=request.POST.get('password')

        user=authenticate(username=login_email, password=login_password)

        if user is not None:
            login(request, user)
            messages.success(request, "Successfully logged in!")
            return redirect('/')
        else:
            messages.warning(request,"Invalid credentials.")
            return redirect('/')

    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    messages.success(request,"Successfully logged out.")

    return redirect('/')

def register(request):
    if request.method == 'POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        citizenship=request.POST.get('citizenship')

        myuser=User.objects.create_user(email, email, password)
        myuser.first_name=first_name
        myuser.last_name=last_name
        myuser.profile.citizenship=citizenship
        myuser.save()
        messages.success(request, 'You can log in now.')
    
        return redirect('/')
    else:
        return redirect('/')

def apply_license(request):
    if request.user.is_authenticated:
        exams=exam_db.objects.all()
        context={'exams':exams}

        if request.method== 'POST':
            citizenship=request.user.profile.citizenship
            name=request.user.first_name+' '+request.user.last_name
            location=request.POST.get('location')
            exam_datetime=(request.POST.get('exam_datetime'))
            license_type=request.POST.get('license_type')
            email = request.user.email

            application = apply_licenses_db(exam_datetime=exam_datetime, citizenship=citizenship, name=name, application_date=datetime.now(), license_type=license_type, location=location, applicant_email=email)
            application.save()
            messages.success(request, 'Your application has been received! Please come to your exam location at the selected time.')

    else:
        messages.warning(request, 'Please log in first!')
        return redirect('/')
    return render(request, 'apply_license.html', context)

def check_license(request):
    if request.user.is_authenticated:
        current_citizenship=request.user.profile.citizenship

        licenses= view_license_db.objects.filter(citizenship=current_citizenship)

        context ={'licenses': licenses}
        return render(request,'check_license.html', context)

    else:
        messages.warning(request, 'Please log in first!')
        return redirect('/')

def check_exam(request):
    if request.user.is_authenticated:
        current_citizenship=request.user.profile.citizenship
        results=exam_result_db.objects.filter(citizenship=current_citizenship).order_by('exam_time')

        context={'results': results}

        return render(request,"check_exam.html",context)


    else:
        messages.warning(request, 'Please log in first!')
        return redirect('/')
    return render(request, 'check_exam.html')

def laws(request):
    laws=law_db.objects.all().order_by('law_date')
    context={'laws': laws}
    return render(request, 'laws.html', context)

def exam_dates(request):

    exam_dates=exam_db.objects.all().order_by('exam_date')
    context={'exams':exam_dates}
    return render(request,'exam_dates.html', context)

def registered_vehicles(request):
    if request.user.is_authenticated:
        current_citizenship=request.user.profile.citizenship
        vehicles = vehicle_db.objects.filter(citizenship=current_citizenship).order_by('vehicle_type')

        context={'vehicles':vehicles}

        return render(request, 'registered_vehicles.html', context)


    else:
        messages.warning(request, 'Please log in first!')
        return redirect('/')

def branches(request):

    branches = branch_db.objects.all()
    context={'branches':branches}

    return render(request,"branches.html", context)

def traffic_offences(request):
    if request.user.is_authenticated:
        current_citizenship=request.user.profile.citizenship

        traffic_offences= traffic_offence_db.objects.filter(citizenship=current_citizenship).order_by('offence_date')

        context ={'offences': traffic_offences}
        return render(request,'traffic_offences.html', context)

    else:
        messages.warning(request, 'Please log in first!')
        return redirect('/')