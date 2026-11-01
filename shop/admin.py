from django.contrib import admin
from .models import Product, FeedPost

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "original_price", "is_custom_available", "created")
    list_filter = ("is_custom_available",)
    search_fields = ("name", "title")

admin.site.register(FeedPost)
