from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/like/', views.like, name='like'),
    path('recommend2/', views.recommend2, name='recommend2'),
    path('<int:pk>/create/', views.reviews_create, name='reviews_create'),
    path('<int:pk>/<int:review_pk>/', views.reviews_detail, name='reviews_detail'),
    path('<int:pk>/<int:review_pk>/review_like/', views.review_like, name='review_like'),
    path('<int:pk>/<int:review_pk>/review_hate/', views.review_hate, name='review_hate'),
    path('<int:pk>/<int:review_pk>/update/', views.reviews_update, name='reviews_update'),
    path('<int:pk>/<int:review_pk>/delete/', views.reviews_delete, name='reviews_delete'),
    path('<int:pk>/<int:review_pk>/comment/', views.comment_create, name='comment_create'),
    path('<int:pk>/<int:review_pk>/<int:comment_pk>/delete/', views.comment_delete, name='comment_delete'),
]