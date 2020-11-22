from django.urls import path

from .views import (
    homepage,
    servicepage,
    user_profile,
    edit_profile,
    delete_image,
    hub_barbers,
    spec_barber,
    search_item,
    products,
    itemDescription,
    )

app_name = 'barbers'

urlpatterns = [
    path('', homepage, name = 'home'),
    path('services/', servicepage, name = 'service'),
    path('profile/', user_profile, name='profile'),
    path('Editprofile/<slug>/', edit_profile, name = 'edit_profile'),
    path('delete/<pk>/', delete_image, name = 'delete'),
    path('barbers/<slug>/', spec_barber, name = 'spec_barber'),
    path('barbers/', hub_barbers, name = 'hub_barbers'),
    path('search/', search_item, name = 'search_item'),
    path('products/', products, name = 'products'),
    path('products/<slug>', itemDescription, name= 'description')
]
