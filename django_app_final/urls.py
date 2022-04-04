"""django_app_final URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from booking import views as booking_views
from users import views as users_views
import admin_app.views as admin_views

"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', users_views.signup, name='signup'),
    path('', users_views.signin, name='signin'),
    path('home/', users_views.home, name='home'),
    path('signout/', users_views.signout, name='signout'),
    path('library/', booking_views.library, name='library'),
    path('library/level/', booking_views.level, name='level'),
    path('seat/', booking_views.seat, name='seat'),
    path('date/', booking_views.date, name='date'),
    path('start_time/', booking_views.start_time, name='start_time'),
    path('end_time/', booking_views.end_time, name='end_time'),
    path('all_bookings/', booking_views.all_bookings, name='all_bookings'),
]
"""
