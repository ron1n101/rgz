from django.db import models
from django.urls import reverse

class Category(models.Model):
    title = models.CharField(max_length=64, db_index=True, verbose_name="Категорія", blank=True)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("category_detail", kwargs={"slug": self.slug})
        
class Home(models.Model):
    title = models.CharField(max_length=64, db_index=True, blank=True)
    category = models.ForeignKey(Category, related_name="home_category", on_delete=models.CASCADE, db_index=True, blank=True)

    def __str__(self):
        return self.title

class Cart(models.Model):
    category = models.ForeignKey(Category, related_name="cart_category", db_index=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=128, blank=True, db_index=True, verbose_name="Назва")
    desc = models.TextField(blank=True, db_index=True)
    poster = models.ImageField(upload_to="blog/poster", verbose_name="Постер")
    image = models.ImageField(upload_to="blog/image", verbose_name="Зображення")
    slug = models.SlugField(unique=True)
    type = models.CharField(max_length=20, default="null")

    
    
    def get_absolute_url(self):
        return reverse("cart_detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title


class CartShots(models.Model):
    title = models.CharField(max_length=128, db_index=True, blank=True)
    image = models.ImageField(upload_to='blog/cart_shots')
    cart = models.ForeignKey(Cart, verbose_name="Карточка", related_name="img_card", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Зображення з карточки"
        verbose_name_plural = "Зображення з карток"
        pass
    def __str__(self):
        return self.title