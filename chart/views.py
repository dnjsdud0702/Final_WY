from django.shortcuts import render
from .models import Covid
from django.db.models import Sum, Q

def home(request):
    return render(request,'home.html')
def covid_19(request):
   # dataset = Covid.objects \
    #    .values('Country') \
     #   .annotate(
      #  confirmed_sum=Sum('confirmed',
       #               filter=('Country=US'))\

        #.order_by('Country'))
    return render(request, 'covid_19.html')
def covid_recoverd(request):

    return render(request, 'covid_recoverd.html')
def covid_death(request):

    return render(request, 'covid_death.html')