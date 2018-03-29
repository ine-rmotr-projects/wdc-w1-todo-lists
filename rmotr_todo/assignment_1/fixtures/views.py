from django.shortcuts import render
from django.http import HttpResponse
from test_utils import mocked_models

Item = mocked_models.Item._get()


def home(request):
    if request.method == 'POST':
        item = Item(text=request.POST.get('item_text', None))
        item.save()
    return render(request, 'home.html', {'items': Item.objects.all()})

def no_template(request, *args, **kwargs):
    response = HttpResponse("Text only, please.", content_type="text/plain")
    return response

def home_no_save(request):
    return render(request, 'home.html', {'items': Item.objects.all()})

def home_save_only_one(request):
    if request.method == 'POST' and Item.objects.count() == 0:
        item = Item(text=request.POST.get('item_text', None))
        item.save()
    return render(request, 'home.html', {'items': Item.objects.all()})