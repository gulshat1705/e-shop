from distutils.command.upload import upload
from email.mime import image
from django.core.files import File
from django.db import models
from io import BytesIO
from unicodedata import category, name         # because I'm going to handle images here and resizing
from PIL import Image



class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        ordering = ('name',)


    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return f'/{self.slug}/'


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)                
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)        
    stock = models.IntegerField(blank=True, null=True)
    status = models.BooleanField(default=True)
    sale = models.IntegerField('Discount in percent', blank=True, default=0)
    draft = models.BooleanField(default=False)
    sold_count = models.IntegerField(default=0)
    view_count = models.IntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ('-date_added',)


    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.slug}/'        #foreignkey category


    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''


    def get_thumbnail(self):
        if self.thumbnail:
            return 'http://127.0.0.1:8000' + self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return 'http://127.0.0.1:8000' + self.thumbnail.url
            else:
                return ''


    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)   
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail   
    @property
    def get_sale_price(self):
        '''Calculate the discounted price'''
        if self.sale > 0:
            sale_price = round(float(self.price - (self.price * self.sale) / 100), 2)

            return sale_price   
