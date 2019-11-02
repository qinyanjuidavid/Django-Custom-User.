from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from accounts.forms import RegisterForm


def home(request):
    context={

    }
    return render(request,'accounts/home.html',context)

def register(request):
    if request.method=="POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=RegisterForm()
    context={
    'form':form
    }
    return render(request,'accounts/register.html',context)
