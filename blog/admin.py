from django.contrib import admin
from .models import Blog, Category, Comment, Tag

admin.site.register([Category, Blog, Tag, Comment])
