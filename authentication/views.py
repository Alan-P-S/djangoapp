from django.shortcuts import render,redirect
from authentication.form import LoginForm,SignupForm
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


def signup_page(request):
    if request.method=="POST":
        sg_form = SignupForm(request.POST)
        if sg_form.is_valid():
            sg_form.save()
            return redirect("/login")
    else:
        sg_form = SignupForm()
        context = {'form':sg_form}
        return render(request,'signup.html',context)
