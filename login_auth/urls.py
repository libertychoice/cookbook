from django.urls import include, path
# from django.conf.urls import url
from . import views

urlpatterns = [
    path('create_user/', views.CreateUserView.as_view(), name='create_user'),
    path('change_user/<int:user_id>/', views.ChangeUserView.as_view(), name='change_user'),
    path('users/<int:user_id>/', views.ShowUserView.as_view(), name='user_page'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]
