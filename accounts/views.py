from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import get_user_model,authenticate,login,logout
from django.contrib import messages
from django.views import View

from .forms import (
    UserCreationForm,UserUpdateForm,LoginForm,ProfileForm
)
from .mixins import (
    LoginRequiredMixin,LogoutRequiredMixin
)

User = get_user_model()

class RegisterView(LogoutRequiredMixin,View):
    def get(self,request):
        form = UserCreationForm()
        return render(request,'accounts/register.html',{'form':form})

    def post(self,request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Your registration was successfully.")
            return redirect('accounts:login')
        messages.error(request,"Your data was invalid.")
        return render(request,'accounts/register.html',{'form':form})
    
class LoginView(LogoutRequiredMixin,View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'accounts/login.html',{'form':form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request,user)
                messages.success(request,"You successfully loged in.")
                return redirect('/')
            messages.error(request,'Your username or password is invalid.')
            return render(request,'accounts/login.html',{'form':form})
        messages.error(request,'Your username or password is invalid.')
        return render(request,'accounts/login.html',{'form':form})

class ProfileView(LoginRequiredMixin,View):
    def get(self, request):
        form = ProfileForm(instance=request.user)
        return render(request,'accounts/profile.html',{'form':form})

class ProfileUpdateView(LoginRequiredMixin,View):
    def get(self, request):
        form = UserUpdateForm(instance=request.user)
        return render(request,'accounts/profile_update.html',{'form':form})
    
    def post(self, request):
        form = UserUpdateForm(instance=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Your profile successfully updated.')
            return redirect('accounts:profile')
        messages.error(request,'Your data was invalid.')
        return render(request,'accounts/profile_update.html',{'form':form})

