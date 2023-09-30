from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import ProductView, CategoryView, SubCategoryView
from rest_framework import routers

route = routers.DefaultRouter()
route.register("products", ProductView, basename='productview')
route.register("category", CategoryView, basename='categoryview')
route.register("subcategory", SubCategoryView, basename='subcategoryview')

urlpatterns = [
    path('api/', include(route.urls)),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
