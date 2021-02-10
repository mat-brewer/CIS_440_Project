from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

# the path name is 'home' and the url path is http://127.0.0.1:8000/
urlpatterns = [
    # gets the function 'main' from views to display index.html
    path('', views.main, name='home'),
    path('menu/', views.menu, name='menu'),
    path('about/', views.about, name='about'),
    path('order/', views.order, name='order'),
    #path('reviews/', views.reviews, name='reviews'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login')
    
   
   
]
