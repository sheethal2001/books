from django.shortcuts import render,redirect,get_object_or_404
from .models import Blog
from.forms import BlogForm

def blog_list(request):
    blogs = Blog.objects.all()
    return render(request,'blog_list.html',{'blogs':blogs})

def add_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    else:
        form=BlogForm()
        return render(request,'blog_form.html',{'form':form})
    
def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    return render(request, 'blog_detail.html', {'blog': blog})

def update_blog(request,pk):
    blog = get_object_or_404(Blog,pk=pk)
    if request.method=='POST':
        form = BlogForm(request.POST,instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    else:
        form=BlogForm(instance=blog)
        return render(request,'blog_form.html',{'form':form})
    
def delete_blog(request,pk):
    blog=get_object_or_404(Blog,pk=pk)
    if request.method=='POST':
        blog.delete()
        return redirect('blog_list')
    else:
        return render(request, 'blog_confirm_delete.html', {'blog': blog})
    






    
    