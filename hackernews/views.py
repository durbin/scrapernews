from hackernews.models import Item
from django.shortcuts import render


def home(request):
    items = Item.objects.order_by('-hnid')[0:99]


    return render(request, "home.html", {
        "items": items,
    })