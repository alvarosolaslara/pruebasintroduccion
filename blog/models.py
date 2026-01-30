from django.db import models

# Create your models here.

# los modelos son los responsables de mandar información y solicitarla a la base de datos

#cada vez que hagamos un cambio en el archivo de models.py haremos una migración nueva "python manage.py migrate"



class Post(models.Model): #el modelp que crearemos será para los post, este tendrán los componentes de los post
    title=models.CharField(max_length=250)
    content=models.TextField()

    def __str__(self): # con esto haremos referencia al post y le daremos un título y no el código que tiene por defecto
        return self.title