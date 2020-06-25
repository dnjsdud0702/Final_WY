from django.contrib import admin
from django.urls import path, include
from chart import views                                     # !!!

urlpatterns = [
    path('covid_19/',
         views.covid_19, name='covid_19'),
    path('covid_recoverd/',
         views.covid_recoverd, name='covid_recoverd'),
    path('covid_death/',
         views.covid_death, name='covid_death'),
    path('',views.home,name='home'),
    path('admin/', admin.site.urls),
]