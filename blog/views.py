from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.forms import modelformset_factory
from django.http import HttpResponse

class PostListView(ListView):
    model = Post
    paginate_by = 5
    template_name = 'post_list.html'
    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class GarbageView(PostListView):
    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-garbage')

class LoveView(PostListView):
    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-love')

class DrunkView(PostListView):
    def get_queryset(self):
        return Post.objects.filter(drunk=True).order_by('-published_date')
        
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})  
        
@login_required  
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            
            return redirect('blog:post_detail', pk=post.pk)
    else:
        form = PostForm()
        
    return render(request, 'post_edit.html', {'form': form})

@login_required    
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog:post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'post_edit.html', {'form': form})
    
def tst(request):
    return render(request, 'tst.html')

def google(request):
    return render(request, 'googlef6613f69040c50ea.html')
    
def trash_category(request):
    cat_id = None
    if request.method == 'GET':
        cat_id = request.GET['category_id']
        button = request.GET['type']
        state = request.GET['action']

    if cat_id:
        cat = Post.objects.get(id=int(cat_id))
        value = (-1, 1) [state == "do"]
        output = ""
        if button == "love":
            cat.love = cat.love + value
            output = str(cat.love)
        elif button == "trash":
            cat.garbage = cat.garbage + value
            output = str(cat.garbage)
        cat.save()

    return HttpResponse(output + " " + (("untrash", "unlove") [button == "love"], "") [state == "undo"])