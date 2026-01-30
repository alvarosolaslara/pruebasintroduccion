from django import forms
from .models import Post

class PostCreateForm(forms.ModelForm): #ahora este form lo llevaremos a la vista
    class Meta:
        model=Post #Declararemos el modelo que queremos editar para este formulario
        fields=('title', 'content') #deberá de tener el mismo contenido que los modelos