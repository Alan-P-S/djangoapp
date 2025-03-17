from django.shortcuts import render,redirect
from authentication.form import LoginForm
from django.contrib.auth import authenticate,login
from django.contrib import messages
# Create your views here.


def login_page(request):
    if request.method=="GET":
        form = LoginForm()
        context = {
        'form':form
        }
        return render(request,'login.html',context)

    else:
        form=LoginForm(request.POST)
        if form.is_valid():
            username= form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                return redirect("/students")
    messages.error(request,f'Invalid username or password')
    context = {'form':form}
    return render(request,'login.html',context)
