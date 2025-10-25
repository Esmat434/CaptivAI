from django.shortcuts import render
from django.views import View

from accounts.mixins import (
    LoginRequiredMixin
)
# Create your views here.

class DashboardView(LoginRequiredMixin,View):
    def get(self,request):
        return render(request,'contentai/dashboard.html')