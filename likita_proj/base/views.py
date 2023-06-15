from django.shortcuts import render, redirect
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from .models import Post, Topic, User, LikedPost, Comment, CommentReply
from .forms import PostForm, ReplyForm


# Create your views here.

def home(request):
    
    q =  request.GET.get('q') if request.GET.get('q') != None else ""
    posts = Post.objects.filter(
        Q(topic__title__icontains=q) |
        Q(owner__username__icontains=q)|
        Q(heading__icontains=q)|
        Q(body__icontains=q)
        )
    topics = Topic.objects.all()
        
    context={'posts': posts, 'topics': topics,}
    return render(request, 'base/home.html', context)

def blog(request):
    q =  request.GET.get('q') if request.GET.get('q') != None else ""
    posts = Post.objects.filter(
        Q(topic__title__icontains=q) |
        Q(owner__username__icontains=q)|
        Q(heading__icontains=q)|
        Q(body__icontains=q)
        )
    topics = Topic.objects.all()
        
    context={'posts': posts, 'topics': topics,}
    
    return render(request, 'base/blog.html', context)


@login_required(login_url='login')
def create_post(request):
    page = 'create-post'
    topics = Topic.objects.all()
    form = PostForm()
    if request.user.is_superuser:
        if request.method == 'POST':
            topic_title = request.POST.get('topic')
            topic, created = Topic.objects.get_or_create(title = topic_title)
            post =  Post.objects.create(
                topic = topic,
                heading = request.POST.get('heading'),
                body = request.POST.get('body'),
                image = request.FILES.get('image'),      
                owner = request.user
            )
            post.save()
            return redirect('home')
        
    else:
        messages.warning(request, 'Permission Denied')
        return redirect('profile', pk=request.user.username)
    
    context={'form': form, 'topics': topics, 'page': page}
    return render(request, 'base/create-update-post.html', context)



@login_required(login_url='login')
def post(request, pk):
    
    post = Post.objects.get(id=pk)
    post_comment = post.comment_set.all()
    
    
    if request.method == 'POST':
        comment = Comment.objects.create(
            body = request.POST.get('body'),
            sender = request.user,
            post = post
        )
        
        return redirect('post', pk=post.id)
    
    context={'post': post, 'post_comment': post_comment}
    return render(request, 'base/post.html', context)


@login_required(login_url='login')
def update_post(request, pk):
    topics = Topic.objects.all()
    post = Post.objects.get(id=pk)
    form = PostForm(instance=post)
    if request.user.is_superuser:
        if request.method == 'POST':
            topic_title = request.POST.get('topic')
            topic, created = Topic.objects.get_or_create(title = topic_title)
        
            post.topic = topic
            post.heading = request.POST.get('heading')
            post.body = request.POST.get('body')
            post.image = request.FILES.get('image') if request.FILES.get('image') else post.image
            
            post.save()
            return redirect('home')
        
    else:
        messages.warning(request, 'Permission Denied')
        return redirect('profile', pk=request.user.username)
    
    context={'form': form, 'topics': topics, 'post': post}
    return render(request, 'base/create-update-post.html', context)


@login_required(login_url='login')
def liked_post(request):
    user = request.user.name
    q = request.GET.get('q')
    
    post = Post.objects.get(id=q)
    liked_post_filter = LikedPost.objects.filter(post_id=q, user=user).first()
    if liked_post_filter == None:
       new_like =  LikedPost.objects.create(post_id = q, user=user)
       new_like.save()
       post.no_of_liked_post += 1
       post.save()
       return redirect('post', pk=post.id)
       
    else:
        liked_post_filter.delete()
        post.no_of_liked_post -= 1
        post.save()
        return redirect('post', pk=post.id)


@login_required(login_url='login')
def delete_post(request, pk):
    post = Post.objects.get(id=pk)
    if request.user == post.owner or request.user.is_superuser:
        if request.method == "POST":
            post.delete()
            return redirect('home')
    context={'post': post}
    return render(request, 'base/delete.html', context)


@login_required(login_url='login')
def reply_comment(request, pk):
    comment= Comment.objects.get(id=pk)
    form = ReplyForm()
    
    comment_reply = comment.commentreply_set.all()
    if request.user.is_superuser:
        replier = request.user
        
    else:
        return redirect('home')
    
    if request.method == "POST":
        reply = CommentReply.objects.create(
            replier = replier,
            body = request.POST.get('body'),
            comment = comment      
        )
        messages.success(request, f'{comment} successfully replied: {reply.body}' )
        
        return redirect('post', pk=reply.comment.post.id)
    context={'comment': comment, 'comment_reply': comment_reply, 'form': form}
    return render(request, 'base/reply.html', context)


def contact_us(request):
    
    
    return render(request, 'base/contact_us.html' )
    