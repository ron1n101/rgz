from django.contrib import admin
from django import forms
from django.utils.safestring import mark_safe
from .models import *

from ckeditor_uploader.widgets import CKEditorUploadingWidget


class CartAdminForm(forms.ModelForm):
    desc = forms.CharField(label="Опис", widget=CKEditorUploadingWidget())
    class Meta:
        model = Cart
        fields = '__all__'




@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['category', 'title', 'slug', 'get_image_poster']
    list_filter = ['category']
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ("get_image_poster", "get_images")
    form = CartAdminForm
    def get_image_poster(self, object):
        return mark_safe(f'<img src = {object.poster.url} width = "50" height = "50"')
    get_image_poster.short_description = 'Постер'



    def get_images(self, object):
        return mark_safe(f'<img src = {object.image.url} width = "50" height = "50"')
    get_images.short_description = 'Зображення'    

admin.site.register(Home)
admin.site.register(CartShots)
