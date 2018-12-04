from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
import datetime
from .models import Post, Comment
from .forms import PostForm, CommentForm

# Create your views here.

time = datetime.datetime.now()
def index(request):
  posts = Post.objects.order_by('-created_date')
  return render(request, 'blog/index.html', {
    'time':time, 
    'posts':posts,
    })

def detail(request, post_id):
  post = get_object_or_404(Post, id = post_id)
  comment_form = CommentForm()
  return render(request, 'blog/detail.html', {
    'post':post,
    'comment_form':comment_form,
    })

def post_new(request):
  if request.method == "POST":
    form = PostForm(request.POST)
    if form.is_valid():
      post = form.save(commit=False)
      post.published_date = datetime.datetime.now()
      post.save()
      return redirect(post)
  else:
    form = PostForm()
  return render(request, 'blog/post_edit.html', {
    'time':time,
    'form':form
    })

def post_edit(request, post_id):
  post = Post.objects.get(id = post_id)
  if request.method == "POST":
    form = PostForm(request.POST, instance=post)
    if form.is_valid():
      post = form.save(commit=False)
      post.published_date = datetime.datetime.now()
      post.save()
      return redirect(post)
  else:
    form = PostForm(instance=post)
  return render(request, 'blog/post_edit.html', {
    'time':time,
    'form':form
    })

def post_delete(request, post_id):
  post = get_object_or_404(Post, id = post_id)
  post.delete()
  return redirect('blog:post_index')

def add_comment_to_post(request, post_id):
  post = get_object_or_404(Post, pk=post_id)
  if request.method == "POST":
    form = CommentForm(request.POST)
    if form.is_valid():
      comment = form.save(commit=False)
      comment.post = post
      comment.save()
  return redirect(post)

def comment_delete(request, comment_id):
  comment = get_object_or_404(Comment, pk=comment_id)
  comment.delete()
  return redirect(comment.post)