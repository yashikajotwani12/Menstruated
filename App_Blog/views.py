from django.shortcuts import render,HttpResponseRedirect
from django.views.generic import CreateView, UpdateView, ListView, DetailView,TemplateView,DeleteView
from App_Blog.models import Blog, Comment, Likes
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
import uuid
from App_Blog.forms import CommentForm

# Create your views here.

class MyBlogs(LoginRequiredMixin,TemplateView):
     template_name= 'App_Blog/my_blogs.html'
     


class UpdateBlog(LoginRequiredMixin,UpdateView):
     model = Blog
     fields =('blog_title', 'blog_content','blog_image')
     template_name ='App_Blog/edit_blog.html'

     def get_success_url(self,**kwargs):
       return reverse_lazy('App_Blog:blog_details', kwargs={'slug':self.object.slug})




class BlogList(ListView):
     context_object_name ='blogs'
     model = Blog
     template_name ='App_Blog/blog_list.html'
     queryset = Blog.objects.order_by('-public_date')


class CreateBlog(LoginRequiredMixin,CreateView):
     model =  Blog
     template_name ='App_Blog/create_blog.html'
     fields =('blog_title', 'blog_content','blog_image')

     def form_valid(self, form):
          blog_obj =form.save(commit=False)
          blog_obj.author= self.request.user
          title = blog_obj.blog_title
          blog_obj.slug = title.replace(" ","-") + "-" + str(uuid.uuid4())
          blog_obj.save()
          return HttpResponseRedirect(reverse('index'))


def blog_details(request,slug):
     blog = Blog.objects.get(slug=slug)
     comment_form = CommentForm()
     already_liked = Likes.objects.filter(blog=blog,user=request.user)
     if already_liked:
          liked=True
     else:
          liked=False

     if request.method == 'POST':
          comment_form = CommentForm(request.POST)
          if comment_form.is_valid():
               comment = comment_form.save(commit=False)
               comment.user = request.user
               comment.blog = blog
               comment.save()
               return HttpResponseRedirect(reverse('App_Blog:blog_details', kwargs={'slug':slug}))
     return render(request,'App_Blog/blog_details.html', context={'blog':blog,'comment_form':comment_form,'liked':liked})
     



@login_required
def liked(request, pk):
     blog = Blog.objects.get(pk=pk)
     user = request.user
     already_liked =Likes.objects.filter(blog=blog, user=user)
     if not already_liked:
          liked_post = Likes(blog=blog, user=user)
          liked_post.save()
     return HttpResponseRedirect(reverse('App_Blog:blog_details', kwargs={'slug':blog.slug}))

@login_required
def unliked(request,pk):
     blog = Blog.objects.get(pk=pk)
     user = request.user
     already_liked = Likes.objects.filter(blog=blog, user=user)
     already_liked.delete()
     return HttpResponseRedirect(reverse('App_Blog:blog_details', kwargs={'slug':blog.slug}))








