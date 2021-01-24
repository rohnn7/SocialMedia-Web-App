from django.contrib import admin
from . import models
# Register your models here.

#this class will, in admin interface when we go to group model
#because of this class we will able to see both model and edit simultaneously
class GroupMemberInline(admin.TabularInline):
    model = models.GroupMember

admin.site.register(models.Group)
