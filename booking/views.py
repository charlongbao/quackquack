from django.shortcuts import render

# Create your views here.

from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from flask import session
from .forms import *
from .models import *

# Create your views here.

def library(request):
    form = LibraryForm()
    context = {"form1":form}
    
    if request.method == 'POST':
        f = LibraryForm(request.POST)
        if f.is_valid():
            request.session["library"] = request.POST.get("library")
            request.session["level"]  = request.POST.get("level")
            request.session["date"]  = request.POST.get("date")
            request.session["start_time"]  = request.POST.get("start_time")
            request.session["end_time"]  = request.POST.get("end_time")
            return redirect('seat')            
                
    return render(request, "book_seat_details.html", context)

def level(request):
    form = LibraryForm(request.GET)
    #context = {"form":form}
    return HttpResponse(form["level"])

def date(request):
    form = LibraryForm(request.GET)
    #context = {"form":form}
    return HttpResponse(form["date"])

def start_time(request):
    form = LibraryForm(request.GET)
    #context = {"form":form}
    return HttpResponse(form["start_time"])

def end_time(request):
    form = LibraryForm(request.GET)
    #context = {"form":form}
    return HttpResponse(form["end_time"])

def seat(request):
    lb = request.session["library"]
    lv = request.session["level"]
    day = request.session["date"]
    start = request.session["start_time"]
    end = request.session["end_time"]
    
    s1 = Q(start_time__lte = start)
    s2 = Q(end_time__gt = start)

    e1 = Q(start_time__lt = end)
    e2 = Q(end_time__gte = end)

    a1 = Q(start_time__gte = start)
    a2 = Q(end_time__lte = end)

    os = Occupied.objects.filter((a1&a2) | (e1&e2) | (s1&s2), level = lv, book_date = day)
    s = Seat.objects.filter(~Q(seat_id__in=[i.seat for i in os]), level=lv).values_list("seat_id", "seat_id")

    form2 = SeatForm(seat_choices = s)
    print(lb, lv, day, start, end)
    
    if request.method == 'POST':
        s = SeatForm(request.POST, seat_choices = s)
        
        if s.is_valid():
            st = request.POST.get("seats")
            Occupied.objects.create(
                matric_no = request.user.username,
                library = Library.objects.get(library_id=lb),
                level = Level.objects.get(level_id=lv),
                seat = Seat.objects.get(seat_id=st),
                book_date = day,
                start_time = start,
                end_time = end
            )
            return redirect("all_bookings")
            
    return render(request, "book_seat.html", {"form2":form2, "library":lb, "level":lv, "day":day, "start":start, "end":end})


def all_bookings(request):
    user = request.user.username
    user_bookings = Occupied.objects.filter(matric_no = user).values("occupied_id", "library", "level", "seat", "book_date", "start_time", "end_time")
    
    if request.method == 'POST':
        record = Occupied.objects.get(occupied_id = request.POST.get('Next'))
        record.delete()
        print(request.POST.get('Next'))
        
    return render(request, 'all_bookings.html', {"query":user_bookings})
