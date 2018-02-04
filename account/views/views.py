from django.shortcuts import render
from django.contrib.auth import logout
from django.urls import reverse,reverse_lazy
from django.http import HttpResponseRedirect

from django.contrib.auth.decorators import login_required
def edit(request):
    pass

def forget_password(request):
    pass

@login_required(login_url=reverse_lazy('login'))
def logout(request):
    logout(request)
    return HttpResponseRedirect(reverse(''))