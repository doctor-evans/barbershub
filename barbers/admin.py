from django.contrib import admin

# Register your models here.
from .models import Profile, Gallery, ProductItem
admin.site.register(Profile)
admin.site.register(Gallery)
admin.site.register(ProductItem)
