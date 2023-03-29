from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.views import generic, View

from users.forms import RegistrationForm


class HomeView(View):
    def get(self, request):
        return render(request, 'users/home.html')


class RegistrationView(generic.CreateView):
    form_class = RegistrationForm
    success_url = reverse_lazy('login')
    template_name = 'users/registration.html'


class LoginView(View):
    form_class = AuthenticationForm
    template_name = 'users/login.html'

    def get(self, request):
        form = AuthenticationForm()
        return render(request, self.template_name, {'login_form': form})

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password'))
            if user is not None:
                login(request, user)
                messages.info(request, 'Login successful')
                return redirect('records')
        messages.error(request, 'Invalid username or password')
        return render(request, self.template_name, {'login_form': form})
