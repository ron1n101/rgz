from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView, CreateView, View

# class HomeView(View):
#     def get(self, request):
#         home_page = Home.objects.all()
#         context = {
#             'home_view':home_page
#         }

#         return render(request, "blog/index.html", context)


def home(request):
    categories = Category.objects.all()
    context = {
        "categories": categories
    }
    return render(request, "blog/index.html", context)

def category_detail(request, slug):
    category = Category.objects.get(slug=slug)
    cards = Cart.objects.filter(category=category)
    context = {
        "category":category,
        "cards" : cards
    }
    return render(request, "blog/card.html", context)

def card_detail(request, category_slug, card_slug):
    category = Category.objects.get(slug=category_slug)
    card = Cart.objects.get(category=category, slug=card_slug)
    context = {
        "category": category,
        "card": card,
    }
    return render(request, "blog/card_detail.html", context)



