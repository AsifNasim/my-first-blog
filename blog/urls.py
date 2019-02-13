from django.urls import path
from . import views

#here we are importing Django's function path and all of our views from blog appli-
#cation.

urlpatterns=[
    path('',views.post_list,name='post_list'),

    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]
