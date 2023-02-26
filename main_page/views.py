

from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.
from .models import  Category, Dish, Photo_gallery
from .forms import BookingForm
import random

QTY_PHOTOS_IN_GALLERY = 2

def main (request):
    categories = Category.objects.filter(is_visible=True)
    dishes =Dish.objects.filter(is_visible=True, is_special=False)
    special_dishes = Dish.objects.filter(is_visible=True, is_special=True)
    gallery_photos = list(Photo_gallery.objects.filter(is_visible=True))
    gallery_photos = random.sample(gallery_photos, QTY_PHOTOS_IN_GALLERY)
    form_reserve = BookingForm()
    # dishes = Dish.objects.all()
    return render(request,'main_page.html', context={
        'categories': categories,
        'dishes': dishes,
        'special_dishes': special_dishes,
        'form_reserve': form_reserve,
        'gallery_photos': gallery_photos,
    })
    # for item in categories:
    #     for dish in item:
    #         print(dish)
    #
    # res_1= f"Categories:{';'.join(map(str,categories)) }"
    # res_2 = f"Dishes:{';'.join(map(str, dishes))}"
    #
    # return HttpResponse (res_1+'\n'+ res_2)
