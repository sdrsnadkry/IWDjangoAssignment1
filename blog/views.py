from django.shortcuts import render
from .models import Blog, Author
from django.shortcuts import redirect

from .forms import BlogForm, AuthorForm
from django.contrib import messages


# Create your views here.

def home(request):
    if request.method == 'POST':
        form1 = BlogForm(request.POST)
        form2 = AuthorForm(request.POST)

        if form1.is_valid() and form2.is_valid():
            blog_model = form1.save()
            author_model = form2.save(commit=False)
            author_model.blog_id = blog_model.id
            author_model.save()
            messages.success(request, 'Blog created successfully')
        return redirect('/blog')

    context = {
        'blogForm': BlogForm,
        'authorForm': AuthorForm,
        'blogCount': Blog.objects.count(),
        'authorCount': Author.objects.count()
    }
    return render(request, 'blog/home.html', context=context)


def blog(request):
    context = {
        'blog_list': Blog.objects.all()
    }
    return render(request, 'blog/blog.html', context=context)


def author(request):
    context = {
        'author_list': Author.objects.all()
    }
    return render(request, 'blog/author.html', context=context)


def delete_blog(request, id):
    obj = Blog.objects.get(id=id)
    obj.delete()
    messages.error(request, 'Blog deleted successfully')
    return redirect('/blog')


def delete_author(request, id):
    obj = Author.objects.get(id=id)
    obj.delete()
    messages.error(request, 'Author deleted successfully')
    return redirect('/author')
