from django.contrib import admin
from .models import FeedItem, RegisteredUser
# Register your models here.
admin.site.register(FeedItem)
admin.site.register(RegisteredUser)