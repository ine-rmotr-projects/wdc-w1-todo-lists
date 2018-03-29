from django.shortcuts import render
from todo.models import Item


def home(request):
    if request.method == 'POST':
        item = Item(text=request.POST.get('item_text', None))
        item.save()
    return render(request, 'home.html', {'items': Item.objects.all()})