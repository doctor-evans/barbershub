from django.shortcuts import render, redirect

from .forms import ProfileForm, AddImageForm
from django.http import Http404
from .models import Profile, Gallery, ProductItem

# Create your views here.

def homepage(request):
    return render(request, 'barbers/home.html')


def servicepage(request):
    return render(request, 'barbers/service.html')

def user_profile(request):
    images = Gallery.objects.filter(barber=request.user).order_by('-date_added')
    user = request.user
    if request.method != 'POST':
        form = AddImageForm()
    else:
        form = AddImageForm(request.POST, request.FILES)
        if form.is_valid():
            add = form.save(commit=False)
            add.barber = request.user
            add.save()
            return redirect('barbers:profile')
    context ={
        'user':user,
        'images' : images,
        'form' : form
    }
    return render(request, "barbers/profile.html", context)

def delete_image(request, pk):
    image = Gallery.objects.get(pk = pk)
    if request.method == 'POST':
        image.delete()
    return redirect('barbers:profile')




def edit_profile(request, slug):
    profile = Profile.objects.get(slug=slug)
    if request.method != 'POST':
        form = ProfileForm(instance = profile)
    else:
        form = ProfileForm(request.POST, request.FILES, instance = profile)
        if form.is_valid():
            update = form.save(commit=False)
            update.user = request.user
            update.save()
            return redirect('barbers:profile')
    context = {
            'form':form,
            'user':request.user
    }
    return render(request, 'barbers/edit_profile.html', context)




def hub_barbers(request):
    barbers = Profile.objects.all()
    context = {
        'barbers':barbers
    }
    return render(request, 'barbers/hub_barbers.html', context)

def spec_barber(request, slug):
    barber = Profile.objects.get(slug = slug)
    images = barber.user.gallery_set.order_by('-date_added')
    context ={
        'barber':barber,
        'images':images
    }
    return render(request, 'barbers/spec_barber.html', context)

def search_item(request):
    searched = request.GET.get('search')
    home_service = request.GET.get('homeservice')
    if home_service and searched:
        barbers = Profile.objects.filter(city__icontains = searched).filter(home_service = True)
    elif home_service:
        barbers = Profile.objects.filter(home_service = True)
    else:
        barbers = Profile.objects.filter(city__icontains = searched)
    context = {
        'barbers':barbers
    }
    return render(request, 'barbers/search.html', context)

def products(request):
    items = ProductItem.objects.all()
    for item in items:
        item.price = f'{item.price:,}'
    context = {
        'items':items
    }
    return render(request, 'barbers/products.html', context)

def itemDescription(request, slug):
    item = ProductItem.objects.get(slug=slug)
    item.price = f'{item.price:,}'
    context = {
        'item':item
    }
    return render(request, 'barbers/description.html', context)
