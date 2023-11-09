from django.urls import path
from . import views


urlpatterns = [
    # path("", views.HomeView.as_view(), name = "home"),
    # path("", views.CategoryView.as_view(), name = "categorys" ),
    # path("<slug:slug>/", views.category_detail, name = 'category_name')
    path("", views.home, name = "home"),
    path("<slug:slug>/", views.category_detail, name = "category_detail"),
    path("<slug:category_slug>/<slug:card_slug>/", views.card_detail, name="cards_detail")


]