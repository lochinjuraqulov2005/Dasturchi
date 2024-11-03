from django.urls import path
from .views import PostView,CreatView,DetalView,UpdView
urlpatterns=[
    path('post/<int:pk>/edit',UpdView.as_view(),name='post2.html'),
    path('post/new',CreatView.as_view(),name='post1.html'),
    path('',PostView.as_view(),name='base.html'),
    path('post/<int:pk>/',DetalView.as_view(),name='post.html')
]