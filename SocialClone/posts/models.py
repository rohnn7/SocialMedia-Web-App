from django.db import models
from django.urls import reverse
from django.conf import settings
#misaka is a way to generate the html for a text through markdown,
#So in message field or content field it will generate the html for them
#misaka is the markdown library
import misaka
from groups.models import Group
from django.contrib.auth import get_user_model
from django.urls import reverse
# Create your models here.
User = get_user_model()

class Post(models.Model):
    user = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    message = models.TextField()
    message_html = models.TextField(editable=False)
    group = models.ForeignKey(Group, related_name='post', null=True,blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.message

    def save(self,*args, **kwargs):
        self.message_html = misaka.html(self.message)#this will convert the description into html format
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('posts:single', kwargs={'username':self.user.username, 'pk':self.pk})

    class Meta:
        ordering = ['-created_at']
        unique_together = ['user', 'message']#since a message will be unique to a user
