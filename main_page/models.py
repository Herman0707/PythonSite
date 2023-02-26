
from django.db import models
from  django.core.validators import RegexValidator
import uuid
import os

class Category(models.Model):
    title = models.CharField(max_length=50, unique=True, db_index=True)
    position = models.SmallIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title}'

    def __iter__(self):
        for item in self.dishes.all():
            yield item

    class Meta:
        ordering = ('position',)


class Dish(models.Model):
    title = models.CharField(max_length=50, unique=True, db_index=True)
    position = models.SmallIntegerField()
    is_visible = models.BooleanField(default=True)
    ingredients = models.CharField(max_length=255)
    desc = models.TextField(max_length=500, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    photo = models.ImageField(upload_to='dishes/%Y-%m-%d', blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='dishes')
    is_special = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ('category', 'position',)


class Events(models.Model):
    title = models.CharField(max_length=50, unique=True, db_index=True)
    is_visible = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    position = models.SmallIntegerField()
    desc = models.TextField(max_length=500, blank=True)
    photo = models.ImageField(upload_to='events/%Y-%m-%d', blank=True)


    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ('position',)

class Photo_gallery(models.Model):
    def get_file_name(self, filename: str):
        ext = filename.strip().split('.')[-1]
        filename = f'{uuid.uuid4()}.{ext}'
        return os.path.join('gallery/%Y-%m-%d', filename)

    title = models.CharField(max_length=50, unique=True, db_index=True)
    position = models.SmallIntegerField()
    is_visible = models.BooleanField(default=True)
    photo = models.ImageField(upload_to=get_file_name, default=1)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ('position',)




class Booking(models.Model):
    phone_validator=RegexValidator(regex=r'/^\+38\d({3})\d{3}\d{2}\d{2}$/', message="Thats wrong number, let's try again")

    persons=models.SmallIntegerField(default=1)
    user = models.CharField(max_length=20, db_index=True)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20, validators=[phone_validator])

    date = models.DateField(auto_now_add=True)
    date_processing=models.DateField(auto_now=True)

    time = models.TimeField()
    count = models.SmallIntegerField()
    text = models.CharField(blank=True, max_length=255)
    message=models.TextField(max_length=250, blank=True)


    is_processed=models.BooleanField(default=False)


    def __str__(self):
        return f'{self.date} ({self.time}): {self.user}'

    class Meta:
        ordering = ('-date', 'time', 'user',)


class Whu_Us (models.Model):
    name = models.CharField(max_length=50, db_index=True, unique=True)
    position = models.CharField(max_length=50)
    description = models.TextField(max_length=500, blank=True)
    photo = models.ImageField(upload_to='Workers/', blank=True)
    twitter = models.URLField(help_text='Twitter account')
    facebook = models.URLField(help_text='Facebook account')
    instagram = models.URLField(help_text='Instagram account')
    linkedin = models.URLField(help_text='LinkedIn account')
    is_visible = models.BooleanField(default=True)


    def __str__(self):
        return f'{self.name}: {self.position}'


# Create your models here.
