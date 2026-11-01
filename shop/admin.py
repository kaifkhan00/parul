from django import forms
from django.contrib import admin
from django.utils.html import format_html
from .models import Product, FeedPost

class PhotoForm(forms.ModelForm):
    def clean_photo(self):
        p = self.cleaned_data["photo"]
        if hasattr(p, "content_type") and p.size > 2 * 1024 * 1024:
            raise forms.ValidationError("Photo 2 MB se chhoti honi chahiye.")
        return p

@admin.display(description="Photo")
def photo_thumb(obj):
    if not obj.photo:
        return "-"
    return format_html('<img src="{}" style="height:56px;width:44px;object-fit:cover;border-radius:6px">', obj.photo.url)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    form = PhotoForm
    list_display = (photo_thumb, "name", "price", "original_price", "is_custom_available", "created")
    list_filter = ("is_custom_available",)
    search_fields = ("name", "title")

@admin.register(FeedPost)
class FeedPostAdmin(admin.ModelAdmin):
    form = PhotoForm
    list_display = (photo_thumb, "link", "created")

admin.site.site_header = "Parul Designer Creation"
admin.site.site_title = "Parul Admin"
admin.site.index_title = "Boutique dashboard"