from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm,CustomUserChangeForm
from django.contrib.auth.views import PasswordChangeView
from allauth.account.views import SignupView

'''
class CustomUserCreationView(generic.CreateView):
    form_class= CustomUserCreationForm
    template_name='accounts/signup.html'
    success_url=reverse_lazy('login')
'''

class AccountSignupView(SignupView):
    # Signup View extended

    # change template's name and path
    template_name = "account/signup.html"
    form_class= CustomUserCreationForm
    success_url=reverse_lazy('home')

    # You can also override some other methods of SignupView
    # Like below:
    # def form_valid(self, form):
    #     ...
    #
    # def get_context_data(self, **kwargs):
    #     ...


account_signup_view = AccountSignupView.as_view()

class UserEditView(generic.UpdateView):
    form_class= CustomUserChangeForm
    template_name='account/edit_profile.html'
    success_url=reverse_lazy('home')

    def get_object(self):
        return self.request.user
