from django.db import models
#A slug is a short label for something, containing only letters, numbers, underscores or hyphens.
#A "slug" is a way of generating a valid URL, generally using data already obtained.
#which means it will help generating a url by clearing up white spaces
from django.utils.text import slugify
#misaka is a way to generate the html for a text through markdown,
#So in message field or content field it will generate the html for them
#misaka is the markdown library
import misaka
from django.contrib.auth import get_user_model
from django import template
from django.urls import reverse
# Create your models here.

User = get_user_model() #Assign User varible the current user model active
register = template.Library()

class Group(models.Model):
    name = models.CharField(max_length= 255, unique=True)
    slug = models.SlugField(allow_unicode=True, unique=True)
    description = models.TextField(blank=True, default='')
    description_html = models.TextField(editable=False, default='',blank=True)
    members = models.ManyToManyField(User, through='GroupMember')
    #ManyToManyField needs a table(class) to manage the two table have relation,
    #in that new table both table's pk will be fk
    #django provides builtn class when ManyToManyField is there but its recommendable
    #to declare it explicitly and tell django by 'through' keyword
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name) #this will convert the name of group in slug format
        self.description_html = misaka.html(self.description) #this will convert the description into html format
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('groups:single', kwargs={'slug':self.slug})

    class Meta:
        ordering = ['name']


#this class is for managing ManyToManyField in Group
class GroupMember(models.Model):
    group = models.ForeignKey(Group, related_name='membership', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='groupsforuser', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ('group', 'user') #compoud key relation, i.e no matter what there will be unique combination of these two
