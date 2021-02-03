"""
CIS_440_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/

Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from users import views as user_views
from reviews import views as review_views
from django.conf.urls import url, include

urlpatterns = [
    # this is the main url path and includes all urls from 'main'. If there is a url path in main like 'checkout/', then the path will be http://127.0.0.1:8000/checkout/
    path('', include('main.urls')),
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('reviews/', review_views.ReviewListView.as_view(), name='reviews'),
    path('reviews/create/', review_views.ReviewCreateView.as_view(), name='create-review'),
    path('reviews/<str:username>', review_views.UserReviewListView.as_view(), name='user-reviews'),
    path('admin/', admin.site.urls)
]
