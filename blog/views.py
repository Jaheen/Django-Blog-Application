from django.shortcuts import render
from .models import Blog
# importing our data model

# Create your views here.
def blog(request):
    blog_data = Blog.objects.all()
    # recieves the all database rows from blog table
    context = {
        'blog_data':blog_data
    } #This is the context which is a dictionary
    # This object maps the blog_data object to "blog_data" key in the "{% if blog_data %}" while rendering the the index.html page
    return render(request,'blog/index.html',context) #Returns a rendered dynamic index.html page to the Http request from the browser
