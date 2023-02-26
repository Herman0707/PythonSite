

from django.contrib import admin

from .models import Category, Dish, Events,Photo_gallery, Whu_Us, Booking
# Register your models here.

class DishAdmin(admin.TabularInline):
    model = Dish
    raw_id_fields = ["category"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title','position','is_visible']
    list_editable = ['position','is_visible']

    inlines=[DishAdmin]

# admin.site.register(Category)
# admin.site.register(Dish)

@admin.register(Dish)
class DishAllAdmin(admin.ModelAdmin):
    model=Dish
    list_display = ['title','position','is_visible','ingredients','desc','price','photo','category','is_special']
    list_filter = ['is_visible','category']
    list_editable = ['position','is_visible','price']

@admin.register(Events)

class EventsAdmin(admin.ModelAdmin):
    model = Events
    list_display = ['title', 'position','photo', 'is_visible', 'desc', 'price' ]
    list_editable = ['price', 'position', 'is_visible']
    list_filter = ['is_visible']

@admin.register(Booking)
class Booking_Admin(admin.ModelAdmin):
    model = Booking
    list_display = ['text', 'count', 'time', 'date', 'phone', 'email','user' ]
    list_filter = ['count','time', 'date','user']

@admin.register(Photo_gallery)
class Photo_galleryAdmin(admin.ModelAdmin):
    model= Photo_gallery
    list_display = ['title', 'position','is_visible']


@admin.register(Whu_Us)

class Whu_UsAdmin(admin.ModelAdmin):
    model=Whu_Us
    list_display = ['name', 'position', 'description', 'photo', 'twitter', 'facebook', 'instagram', 'linkedin', 'is_visible']
    list_editable = ['description',  'is_visible','position']