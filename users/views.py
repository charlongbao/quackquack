from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from booking.models import *
from flask import session
from django.db import connection
from django.db.models import Count

# Create your views here.
def signup(request):
    form = UserRegistrationForm(request.POST or None)
    
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            print("VALID")
            form.save()
            student_id = form.cleaned_data['username']
            messages.success(request, f'Account successfully created for {student_id}!')
            return redirect('signin')
        
        else:
            print("INVALID")
            messages.info(request, 'invalid registration details')
    
    context = {'form':form}
    return render(request, 'register.html', context)


def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, "Username or password is incorrect")
         
    return render(request, 'login.html', {})


def signout(request):
    logout(request)
    messages.success(request, ("You have successfully logged out!"))
    return render(request, 'logout.html', {})


def home(request):
    d = AllSeats()
    
    if request.method == 'POST':
        d = AllSeats(request.POST)
        
        if d.is_valid():
            date = request.POST.get('date')
            cursor = connection.cursor()
            cursor.execute("""
                select library_id, level_id, coalesce(occ, 0) as occupied, total
                from (select library_id, level_id, count(seat_id) as total from seat group by 1,2) a
                left join (select library_id, level_id, count(distinct seat_id) as occ from occupied where book_date = %s group by 1,2) b using(library_id, level_id)
                order by 1, 2
            """ , [date])
            
            occupancy = cursor.fetchall()
            CLB = filter(lambda x: x[0] == 'CLB', occupancy)
            WSLB = filter(lambda x: x[0] == 'WSLB', occupancy)
            KKL = filter(lambda x: x[0] == 'KKL', occupancy)
            HSSL = filter(lambda x: x[0] == 'HSSL', occupancy)
            MDL = filter(lambda x: x[0] == 'MDL', occupancy)
            MSL = filter(lambda x: x[0] == 'MSL', occupancy)
            SCL = filter(lambda x: x[0] == 'SCL', occupancy)
            YNCL = filter(lambda x: x[0] == 'YNCL', occupancy)

            return render(request, 'home.html', {"CLB":list(CLB), "WSLB":list(WSLB), "KKL":list(KKL),
                                                  'HSSL': list(HSSL), 'MDL': list(MDL), 'MSL': list(MSL),
                                                  'SCL': list(SCL), 'YNCL': list(YNCL)})

    return render(request, 'home.html', {"form":d})



from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from booking.models import *
from flask import session
from django.db import connection
from django.db.models import Count

# Create your views here.
def signup(request):
    form = UserRegistrationForm(request.POST or None)
    
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            print("VALID")
            form.save()
            student_id = form.cleaned_data['username']
            messages.success(request, f'Account successfully created for {student_id}!')
            return redirect('signin')
        
        else:
            print("INVALID")
            messages.info(request, 'invalid registration details')
    
    context = {'form':form}
    return render(request, 'register.html', context)


def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, "Username or password is incorrect")
         
    return render(request, 'login.html', {})


def signout(request):
    logout(request)
    messages.success(request, ("You have successfully logged out!"))
    return render(request, 'logout.html', {})


def home(request):
    d = AllSeats()
    
    if request.method == 'POST':
        d = AllSeats(request.POST)
        
        if d.is_valid():
            date = request.POST.get('date')
            cursor = connection.cursor()
            cursor.execute("""
                select library_id, level_id, coalesce(occ, 0) as occupied, total
                from (select library_id, level_id, count(seat_id) as total from seat group by 1,2) a
                left join (select library_id, level_id, count(distinct seat_id) as occ from occupied where book_date = %s group by 1,2) b using(library_id, level_id)
                order by 1, 2
            """ , [date])
            
            occupancy = cursor.fetchall()
            CLB = filter(lambda x: x[0] == 'CLB', occupancy)
            WSLB = filter(lambda x: x[0] == 'WSLB', occupancy)
            KKL = filter(lambda x: x[0] == 'KKL', occupancy)
            HSSL = filter(lambda x: x[0] == 'HSSL', occupancy)
            MDL = filter(lambda x: x[0] == 'MDL', occupancy)
            MSL = filter(lambda x: x[0] == 'MSL', occupancy)
            SCL = filter(lambda x: x[0] == 'SCL', occupancy)
            YNCL = filter(lambda x: x[0] == 'YNCL', occupancy)

            return render(request, 'home.html', {"CLB":list(CLB), "WSLB":list(WSLB), "KKL":list(KKL),
                                                  'HSSL': list(HSSL), 'MDL': list(MDL), 'MSL': list(MSL),
                                                  'SCL': list(SCL), 'YNCL': list(YNCL)})

    return render(request, 'home.html', {"form":d})



