from django.contrib import admin

from app_one.models import Blog
from .models import Blog
# Register your models here.
admin.site.register(Blog)