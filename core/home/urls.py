from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index' ),
    path('blog/',views.blog, name="blog"),
    path('about/', views.about, name='about'),
    path('materia/<int:id>/<slug:slug>', views.materia, name="materia"),
]