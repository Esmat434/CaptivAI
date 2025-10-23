from django.shortcuts import redirect,render
from django.contrib.auth.mixins import AccessMixin

class LoginRequiredMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return render(request,"contentai/landing.html")
        return super().dispatch(request, *args, **kwargs)

class LogoutRequiredMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        return super().dispatch(request, *args, **kwargs)