from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import View, UpdateView, DeleteView #CON UPDATE MODIFICAREMOS UNA VISTA
from .forms import PostCreateForm
from .models import Post
from django.urls import reverse_lazy #para redirigir 


class BlogListView(View): # creamos las vistas de blog, aquí enlistaremos todos los post que existen
    def get(self, request, *args, **kwargs):
        #Para enlistar llamaremos a los POST (a sus objetos) que se encuentran en la base de datos
        posts = Post.objects.all() #para ver esta información la pasaremos al contexto para luegos hacer referencia en el html
        context={
            'posts':posts
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
        if request.method=="POST": # si el request es igual a POST, le pasaremos la información que se encuentra dentro de FORM
            form=PostCreateForm(request.POST)
            if form.is_valid(): #si el formulario es válido tendremos la información, título y contenido
                title = form.cleaned_data.get('title')
                content = form.cleaned_data.get('content')
                p, created = Post.objects.get_or_create(title=title, content=content)
                p.save()
                return redirect('blog:home')
        context={

        }
        return render(request, 'blog_create.html', context)
    


class BlogDetailView(View):
    def get(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk)
        context={
            'post':post
        }
        return render(request, 'blog_detail.html',context)
    
class BlogUpdateView(UpdateView):
    model=Post #Ahora le pasaremos los campos que queremos editar
    fields=['title','content']
    template_name='blog_update.html'

    #cuando se actualice se nor redirigirá al enlace que indicaremos a continuación
    def get_success_url(self):
        pk = self.kwargs['pk'] #información del objeto que se encuentra dentro llamando, es decir, del modelo arriba llamado POST
        return reverse_lazy('blog:detail', kwargs={'pk':pk})


class BlogDeleteView(DeleteView):
    model=Post #Se le pasa a Delete view el model que se dea borrar
    template_name='blog_delete.html'
    success_url= reverse_lazy('blog:home')


    
class ejemplo(View):
    def get(self, request, *args, **kwargs):
        context={

        }
        return render(request, 'vision.html', context)