from django.shortcuts import render, redirect
from .models import Command

def home(request):

    if not request.user.is_authenticated:
        return redirect("login-user")
    
    context ={}
 
    # add the dictionary during initialization
    context["dataset"] = Command.objects.all()
    return render(request, "index.html", context)


def de(request,pk):
    if not request.user.is_authenticated:
        return redirect("login-user")
    context = {}
    context['object'] = Command.objects.get(id=pk)
    return render(request,'details.html',context)

