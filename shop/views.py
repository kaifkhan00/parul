from django.shortcuts import get_object_or_404, render
from .models import Product, FeedPost

from django.http import HttpResponse

def health(request):
    """Lightweight ping target for cron-job.org. Does not touch the database."""
    return HttpResponse("ok", content_type="text/plain")

def home(request):
    feed = list(FeedPost.objects.all()[:6])
    if len(feed) < 6:  # fall back to product photos until feed photos are uploaded
        feed += list(Product.objects.all()[: 6 - len(feed)])
    return render(request, "shop/home.html", {"products": Product.objects.all()[:8], "feed": feed})

def shop(request):
    q = request.GET.get("q", "").strip()
    products = Product.objects.all()
    if q:
        products = products.filter(name__icontains=q) | products.filter(title__icontains=q)
    if request.GET.get("custom"):
        products = products.filter(is_custom_available=True)
    return render(request, "shop/shop.html", {"products": products, "q": q, "custom": request.GET.get("custom")})

def product(request, pk):
    p = get_object_or_404(Product, pk=pk)
    more = Product.objects.exclude(pk=pk)[:4]
    return render(request, "shop/product.html", {"p": p, "more": more, "saving": p.original_price - p.price})
