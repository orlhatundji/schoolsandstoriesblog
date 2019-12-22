from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.views.generic import ListView
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as django_logout


from .models import Post
from .forms import PostForm
from .forms import CommentForm


def index(request):
    latest_blog_list = Post.objects.order_by('-created_date')#[:15]
    context = {
        'latest_blog_list': latest_blog_list
    }
    return render(request, 'blog/index.html', context)

class DetailView(generic.DetailView):
    model = Post      
    template_name = 'blog/details.html'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        comment_form = CommentForm()
        context['comment_form'] = comment_form
        return context

@login_required
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        form.created_date = timezone.now()
        if form.is_valid():
            inst = form.save(commit=False)
            inst.author = request.user            
            inst.save()
            post_id = inst.id            
            return HttpResponseRedirect(reverse('blog:detail', args=[post_id]))
        else:
            return HttpResponse("Sorry, a problem occured and the post could not be created")
    else:
        form = PostForm()
        return render(request, 'blog/create.html', {'form': form})

@login_required
def update(request, post_id): 
    if request.method == 'POST':
        instance = get_object_or_404(Post, id=post_id)
        form = PostForm(request.POST or None, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blog:detail', args=[post_id]))
        else:
            return HttpResponse("Sorry, a problem occured and the post could not be updated")
    else:
        instance = get_object_or_404(Post, id=post_id)
        form = PostForm(request.POST or None, instance=instance)
        return render(request, 'blog/update.html', {'form': form, 'post_id':post_id})

@login_required
def delete(request, post_id): 
    if request.method == 'POST':
        instance = get_object_or_404(Post, id=post_id)
        instance.delete()
        return HttpResponseRedirect(reverse('blog:index'))
    else:
        instance = get_object_or_404(Post, id=post_id)
        form = PostForm(request.POST or None, instance=instance)
        return render(request, 'blog/delete.html', {'form': form, 'post_id':post_id})

def comment(request, post_id):
    if request.method == 'POST':
        post = get_object_or_404(Post, id=post_id)
        print('\n\nrequest-post-comment\n\n', request.POST, '\n\npost-content\n\n', post)
        
        form = CommentForm(request.POST)
        form.post = post
        form.created_date = timezone.now()
        print('\n\nThe form now\n\n',form)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.post = post
            instance.save()
            return HttpResponseRedirect(reverse('blog:detail', args=[post_id]))
        else:
            return HttpResponse("Sorry, a problem occured and comment could not be posted")

def logout(request):
    django_logout(request)
    return HttpResponseRedirect(reverse('blog:index'))

