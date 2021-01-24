from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from . import forms
# Create your views here.

#This class is inherit from CreateView but note that it dont have model = User
# because the form we created automatically inserts the data into User model on clicking submit
class SignUp(CreateView):
    form_class = forms.UserCreateForm # Connect the views.py to form.py, and that form connects User Model
    success_url = reverse_lazy('login') # tells to redirect to login after hitting signup
    template_name = 'accounts/signup.html' #specifying the name if template
