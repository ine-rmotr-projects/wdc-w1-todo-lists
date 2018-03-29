from django.shortcuts import render, redirect
from django.http import HttpResponse
from test_utils import mocked_models


Item = mocked_models.Item._get()
List = mocked_models.List._get()


def home(request):
    if request.method == 'POST':
        item = Item(text=request.POST.get('item_text', None))
        item.save()
    return render(request, 'home.html', {'items': Item.objects.all()})


def no_template(request, *args, **kwargs):
    response = HttpResponse("Text only, please.", content_type="text/plain")
    return response

def new_list(request):
    list_ = List.objects.create()
    item = Item(text=request.POST.get('item_text', None),
                list=list_)
    item.save()
    return redirect(list_)

def new_list_no_create_item(request):
    list_ = List.objects.create()
    return redirect(list_)

def new_list_redirects_home(request):
    list_ = List.objects.create()
    item = Item(text=request.POST.get('item_text', None),
                list=list_)
    item.save()
    return redirect('home')

def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    if request.method == 'POST':
        item = Item(text=request.POST.get('item_text', None),
                    list=list_)
        item.save()
        return redirect(list_)
    return render(request, 'list.html', {'list': list_})

def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    if request.method == 'POST':
        item = Item(text=request.POST.get('item_text', None),
                    list=list_)
        item.save()
        return redirect(list_)
    return render(request, 'list.html', {'list': list_})

def view_list_doesnt_add_items(request, list_id):
    list_ = List.objects.get(id=list_id)
    if request.method == 'POST':
        pass
    return render(request, 'list.html', {'list': list_})

def view_list_shows_wrong_list(request, list_id):
    list_ = List()
    if request.method == 'POST':
        item = Item(text=request.POST.get('item_text', None),
                    list=list_)
        item.save()
        return redirect(list_)
    return render(request, 'list.html', {'list': list_})

def view_list_shows_all_items(request, list_id):
    list_ = List.objects.get(id=list_id)
    if request.method == 'POST':
        item = Item(text=request.POST.get('item_text', None),
                    list=list_)
        item.save()
        return redirect(list_)

    list_ = List()
    for i in Item.items:
        list_._items.append(i)
    return render(request, 'list.html', {'list': list_})