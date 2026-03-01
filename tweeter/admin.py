from django.contrib import admin
from . import models
from .models import Tweet

# Register your models here.

class TweetAdmin(admin.ModelAdmin):
    fields = ('nickname', 'content', 'created_at')

admin.site.register(Tweet, TweetAdmin)
 