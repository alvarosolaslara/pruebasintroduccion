from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import PostCreateForm
from .models import Post


class BlogListView(View): # creamos las vistas de blog, aquí enlistaremos todos los post que existen
    def get(self, request, *args, **kwargs):
        context={

        }
        return render(request, 'blog_list.html', context)
    

class BlogCreateView(View):
    def get(self, request, *args, **kwargs):
        form=PostCreateForm()
        context={
            'form':form #en el html , con esto podremos obtener el contenido de form {{}}
        }
        return render(request, 'blog_create.html', context)
    
    def post(self, request, *args, **kwargs):
        if request.method=="POST":
            form=PostCreateForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data.get('title')
                content = form.cleaned_data.get('content')
                p, created = Post.objects.get_or_create(title=title, content=content)
                p.save()
                return redirect('blog:home')
        context={

        }
        return render(request, 'blog_create.html', context)