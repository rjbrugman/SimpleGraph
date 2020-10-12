from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_world, name='hello_world'),
    path('GraphApp/', views.hello_world, name='GraphApp'),
    path('GraphInput/', views.graph_input, name='GraphInput'),

]