from django.urls import path
from . import views
urlpatterns = [
    path('blog/',views.blog), #Passes the Http Request as first parameter to the index function in the view.py for recieving response
    path('', views.blog)    #Passes the Http Request as first parameter to the index function in the view.py for recieving response
]