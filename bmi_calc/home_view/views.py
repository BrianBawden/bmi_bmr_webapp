from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request, *args, **kwargs):
    # return HttpResponse("Welcome")
    return render(request, 'bmi_home.html', {})

def bmr_calc(request, *args, **kwargs):
    return render(request, "BMR.html", {})

def bmi_calc(request, *args, **kwargs):
    return render(request, "BMI.html", {})