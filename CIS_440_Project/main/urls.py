from django.urls import path
from . import views

# the path name is 'home' and the url path is http://127.0.0.1:8000/
urlpatterns = [
    # gets the function 'main' from views to display index.html
    path('', views.main, name='home'),
]
