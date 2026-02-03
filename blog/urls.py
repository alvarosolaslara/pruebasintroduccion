from django.urls import path
from .views import BlogListView, BlogCreateView, BlogDetailView, BlogUpdateView, BlogDeleteView, ejemplo #lo importamos de views.py

app_name="blog"

urlpatterns=[# accederemos a todas las vistas básicas de nuestro blog

    path('', BlogListView.as_view(), name='home'), # con esto conectamos a las url de core, este es el home
    path('create/', BlogCreateView.as_view(), name='create'),

    path('update/', BlogUpdateView.as_view(), name='update'),
    
    path('<int:pk>/delete/', BlogDeleteView.as_view(), name='delete'),# <int:pk> hace referencia al id de cada modelo, en este caso es importante para saber que es lo que estamos borrando

    path('<int:pk>/', BlogDetailView.as_view(), name='detail'), # <int:pk> hace referencia al id de cada modelo

    path('movimiento/', ejemplo.as_view(), name='mov'),
    
]