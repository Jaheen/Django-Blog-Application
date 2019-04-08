from django.db import models


# Create your models here.
class Blog(models.Model):
    blog_title = models.CharField(max_length=20,default="Blog-Post")
    blog_content = models.TextField(default="Blog-Content")
    def __str__(self):
        return self.blog_title  #Makes the name of blog post to show up in the Django admin site
                                #Without this the name will be just Blog object(1),Blog object(2),...etc
#Above block of code Creates A table with Schema below:
# "CREATE TABLE IF NOT EXISTS "blog_blog" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "blog_title" varchar(20) NOT NULL, "blog_content" text NOT NULL)