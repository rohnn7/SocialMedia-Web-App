from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

#UserCreationForm is the form creating new user, CreateView calls this only while registering user
#this same as we used to create a form, just a technique is different
class UserCreateForm(UserCreationForm):
    class Meta:
        fields = ('username', 'email', 'password1', 'password2')
        model = get_user_model() #. This method will return the currently active
        # user model – the custom user model if one is specified, or User(builtin) otherwise.

    #This method tells in form in <label> what would be the value of it
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label='Enter Usename'
        self.fields['email'].label='Enter Email Address'
