from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import Http404
from django.views import generic
from braces.views import SelectRelatedMixin
from . import models, forms
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.contrib import messages
# Create your views here.
User = get_user_model()

#this class will be responsible for showing the list of all post in a group
class PostList(SelectRelatedMixin,generic.ListView):
    model = models.Post
    select_related = ('user','group') #this specifies the fk relations between
    #basically what it does is it will select all the posts that as fk as
    # a particular group or user or both

    def get_context_data(self, **kwargs):

        context = super(PostList, self).get_context_data(**kwargs)
        context['user_groups'] = models.Group.objects.filter(members__in=[self.request.user]) #this statements says select all object of member which has user in it
        context['other_groups'] = models.Group.objects.all()
        return context

#this class will give the list of all posts by a particula user
class UserPosts(generic.ListView):
    model = models.Post
#sice list view will fetch all the posts in the database, but we only want the post by
#particular user so we add a queryset by get_queryset function by default, if u dont specify the
#the  queryset, it is in .all()

    #basically what this function is doing, we add a query set to this funtion
    #select * from Post as p JOIN User as u On p.userid=u.userid  where u.username = in_username
    def get_queryset(self):

        queryset = User.objects.all()
             #we are able to fetch the user in post by related_name='post'
        self.post_user = queryset.prefetch_related('posts').get(username__iexact=self.kwargs.get("username"))
        #User.objects.prefetch_related("posts").get(
        #username__iexact=self.kwargs.get("username")
        #    )
         #this statement will return above sql query, we find the username related to that post
            #and store it in the post_user
        return self.post_user.posts.all() #if no exception then return all the posts in post_user

    #this function get_context_data used for displaying the object by injecting the in templates
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_user'] = self.post_user.posts.all()
        return context




class CreatePost(SelectRelatedMixin, LoginRequiredMixin, generic.CreateView):
    fields=('message', 'group')
    model = models.Post
    #this is for form validation (not required just to show this is also possible)
    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class DeletePost(SelectRelatedMixin,LoginRequiredMixin,generic.DeleteView):
    model = models.Post
    select_related = ('user', 'group')
    success_url = reverse_lazy('posts:all')

    #this function is saying that
    #first get the query and store it in variable queryset
    #then filter the query by userid i.e. only user are able to delete of their
    #own post not someone else
    #technically it gets the detail of post by pk
    #then filter(checks) is userid is attached to that post
    #if yes it deletes otherwise not delete
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id = self.request.user.id)

    #this fuction is just a fancy way to deletes
    #it is just an addon feature which tells after deletion show a message 'post deleted'
    def delete(self,*args,**kwargs):
        messages.success(self.request, 'Post_deleted')
        return super().delete(*args,**kwargs)


class PostDetail(SelectRelatedMixin, generic.DetailView):
    model = models.Post
    select_related = ('user','group')
    #this function is saying that
    #first get the query and store it in variable queryset
    #then filter the query by username i.e. only user are able to see detail of their
    #own posts not the others posts
    #technically it gets the detail of post by pk
    #then filter(checks) is usename is attached to that post
    #if yes then display otherwise notfound
    def get_queryset(self):
        queryset = super().get_queryset(self)
        return queryset.filter(username__iexact = self.kwargs.get("username"))
