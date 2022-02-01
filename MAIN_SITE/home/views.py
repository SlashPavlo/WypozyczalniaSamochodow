from django.shortcuts import render
from .forms import RegistrationForm, LoginForm
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.base import View
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from .models import AutoShare

def setHome(request):
    queryset = AutoShare.objects.all()
    context = {'cars': queryset}
    return render(request, 'home/index.html', context)



class Registration(View):
    def get(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST or None)
        context = {'form': form}
        return render(request, 'home/registration.html',context)

    def post(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST or None)
        if form.is_valid():
            new_user = form.save(commit=False)
            username = form.cleaned_data['username']
            new_user.username = username

            new_user.save()
            new_user.set_password(form.cleaned_data['password'])

            new_user.save()
            user = authenticate(username = username, password=form.cleaned_data['password'])
            login(request, user)
            return HttpResponseRedirect('/')
        context = {'form': form}
        return render(request, 'home/registration.html', context)

class LoginView(View):

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST or None)
        context = {'form': form}
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username = username, password = password)

            if user:
                login(request, user)
                return HttpResponseRedirect("/")
        return render(request, 'home/login.html', context )

    def get(self, request, *args, **kwargs):
        form = LoginForm(request.POST or None)
        context = {'form': form}

        return render(request, 'home/login.html', context)
