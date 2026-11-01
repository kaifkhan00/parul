from urllib.parse import quote
from django.db import models
from django.urls import reverse
from .context import BRAND


class Product(models.Model):
    title = models.CharField(max_length=160, help_text="Headline shown on the product page, e.g. 'Maroon Handloom Cotton Kurti'")
    name = models.CharField(max_length=80, help_text="Short name used in the Instagram order message")
    description = models.TextField(blank=True)
    price = models.PositiveIntegerField(help_text="Selling price in ₹")
    original_price = models.PositiveIntegerField(help_text="Price before discount in ₹")
    photo = models.ImageField(upload_to="products/")
    is_custom_available = models.BooleanField(default=False, help_text="Can be stitched to custom measurements / design")
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product", args=[self.pk])

    @property
    def discount_percent(self):
        if self.original_price and self.original_price > self.price:
            return round(100 - (self.price * 100 / self.original_price))
        return 0

    @property
    def order_message(self):
        return f"Hi {BRAND['name']}! I'd like to order: {self.name} (₹{self.price})"

    @property
    def ig_order_url(self):
        return f"https://ig.me/m/{BRAND['handle']}?text={quote(self.order_message)}"


class FeedPost(models.Model):
    """Photos for the homepage Instagram grid. Upload your latest 6 post images here."""
    photo = models.ImageField(upload_to="feed/")
    link = models.URLField(help_text="Exact Instagram post link, e.g. https://www.instagram.com/p/XXXXXXX/")
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created"]
