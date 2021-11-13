from DjangoWebApp.models import Bug
from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):

    return render(request,"djangoWebApp/home.html")

def about(request):

    return render(request,"djangoWebApp/about.html")

    
def contact(request):

    return render(request,"djangoWebApp/contact.html")

def banner(request):

    return render(request, "{% static '/images/banner.jpg' %}")

    
def bugs(request):
    bugs=Bug.objects.all()
    return render(request, "djangoWebApp/bugs.html", {"bugs":bugs})