from django.contrib import admin
from .models import Author, Image, HashTag


admin.site.register(Author)
admin.site.register(Image)
admin.site.register(HashTag)
