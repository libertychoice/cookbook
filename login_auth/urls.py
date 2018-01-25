from django.urls import include, path
# from django.conf.urls import url
from . import views

urlpatterns = [
    path('create_user/', views.create_user, name='create_user'),
    path('users/<int:user_id>/', views.show_user, name='user_page'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
