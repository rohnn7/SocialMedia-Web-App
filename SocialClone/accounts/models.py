from django.db import models
from django.contrib import auth
# Create your models here.

# this class will inherit from built in user model
# also will inherit from permissionmixin which give a particular user a particular permission
#example as admin i can add the post to the the database through ui i Create
class User(auth.models.User,auth.models.PermissionsMixin):

    def __str__(self):
        # for @username representation like any social media platform
        return "@{}".format(self.username)
