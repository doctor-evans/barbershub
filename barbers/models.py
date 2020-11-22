from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.utils.text import slugify


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
    phone_no = models.CharField(max_length=11, null = True)
    whatsapp_no = models.CharField(max_length=11,null = True)
    facebook_link = models.URLField(null = True)
    intagram_link = models.URLField(null = True)
    twitter_link = models.URLField(null = True)
    bio = models.TextField()
    profile_picture = models.ImageField(upload_to='photos/', null=True, blank = True)
    home_service = models.BooleanField(default = False)
    state = models.CharField(max_length=20, null = True)
    city = models.CharField(max_length=30, null =True)
    address =  models.CharField(max_length = 100, null = True)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user)
        super(Profile, self).save(*args, **kwargs)



def profile_create(sender, instance, created, *args, **kwargs):
    if created:
        Profile.objects.get_or_create(user = instance)

post_save.connect(profile_create, sender = settings.AUTH_USER_MODEL)


class Gallery(models.Model):
    barber = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'photos/')
    date_added = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.barber.username + "'s work"
    class Meta:
        verbose_name_plural = "Galleries"

    def delete(self, *args, **kwargs):
        self.image.delete
        super().delete(*args, **kwargs)


class ProductItem(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    description = models.TextField()
    image = models.ImageField(upload_to = 'photos/', blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    bought = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(ProductItem, self).save(*args, **kwargs)
