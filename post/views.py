from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from post.forms import PostForm
from post.models import Post

@login_required
def post_list(request):
    posts = Post.objects.all()
    context = { "posts" : posts }
    return render(request, "post/index.html", context)

@login_required
def post_details(request, id):
    post = get_object_or_404(Post, id=id)
    author = post.author.get_full_name()
    context = { "post": post, "author": author }
    return render(request, "post/details.html", context)

@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('post.list')
    else:
        form = PostForm(user=request.user)
    return render(request, 'post/create.html', {'form': form})

@login_required
def post_update(request, id):
    pass

@login_required
def post_delete(request, id):
    pass