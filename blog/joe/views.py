from django.shortcuts import render,HttpResponseRedirect 
from .models import User
from joe.forms import StudentRegisteration

# Create your views here.
def home(request):
    if request.method == 'POST':
        fm=StudentRegisteration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            regi= User(name=nm, email=em,password=pw)
            regi.save()
            fm=StudentRegisteration()
    else:
        fm=StudentRegisteration()
    stfu= User.objects.all()
    return render(request, 'index.html',{'forms':fm, 'fu':stfu})
def delete(request,id):
    if request.method == 'POST':
        dlt=User.objects.get(pk=id)
        dlt.delete()
        return HttpResponseRedirect("/")
def update(request,id):
    if request.method == "POST":
        up=User.objects.get(pk=id)
        fm=StudentRegisteration(request.POST, instance=up)
        if fm.is_valid():
            fm.save()
    else:
        up=User.objects.get(pk=id)
        fm=StudentRegisteration(instance=up)
    return render(request, 'update.html', {'forms':fm})
