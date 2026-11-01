BRAND = {
    "name": "Parul Designer Creation",
    "tagline": "Trendy Ethnic Wear | Custom Designs & Stitching",
    "handle": "parul.desginer_creation",
}
def brand(request):
    return {
        "brand": BRAND,
        "ig_profile": f"https://instagram.com/{BRAND['handle']}",
        "ig_dm": f"https://ig.me/m/{BRAND['handle']}",
    }
