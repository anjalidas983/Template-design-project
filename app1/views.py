from django.shortcuts import render
from app1.models import place,Team

# Create your views here.
def index(request):
    b=place.objects.all()
    t=Team.objects.all()
    return render(request,'index.html',{'b':b,'t':t})

def contact(request):
    return render(request,'contact.html')