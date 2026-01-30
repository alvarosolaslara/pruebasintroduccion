from django.urls import path
from .views import BlogListView, BlogCreateView #lo importamos de views.py

app_name="blog"

urlpatterns=[# accederemos a todas las vistas básicas de nuestro blog

    path('', BlogListView.as_view(), name='home'), # con esto conectamos a las url de core, este es el home
    path('create/', BlogCreateView.as_view(), name='create'),
    
]