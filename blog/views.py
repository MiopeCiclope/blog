from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post, Images
from .forms import PostForm, ImageForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.forms import modelformset_factory

class PostListView(ListView):
    model = Post
    paginate_by = 2
    template_name = 'post_list.html'
    # queryset = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})  
        
@login_required  
def post_new(request):
    ImageFormSet = modelformset_factory(Images, form=ImageForm)

    if request.method == "POST":
        form = PostForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES,queryset=Images.objects.none())
        
        if form.is_valid() and formset.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()

            for form in formset.cleaned_data:
                image = form['image']
                photo = Images(post=post, image=image)
                photo.save()
            
            return redirect('blog:post_detail', pk=post.pk)
    else:
        form = PostForm()
        formset = ImageFormSet(queryset=Images.objects.none())
        
    return render(request, 'post_edit.html', {'form': form, 'formset': formset})

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