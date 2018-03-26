from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest, HttpResponseNotFound
from todo.models import Item, List
from todo.forms import ItemForm
from django.core.exceptions import ObjectDoesNotExist


def home(request):
    return render(request, 'home.html', {'form': ItemForm()})


def new_list(request):
    form = ItemForm(data=request.POST)
    if form.is_valid():
        list_ = List.objects.create()
        Item.objects.create(text=request.POST['text'], list=list_)
        return redirect(list_)
    else:
        return render(request, 'home.html', {'form': form})


def view_list(request, list_id):
    try:
        list_ = List.objects.get(id=list_id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound()

    form = ItemForm()

    if request.method == 'POST':
        form = ItemForm(data=request.POST)
        if form.is_valid():
            form.save(list_=list_)
            return(redirect(list_))
    return render(request, 'list.html', {'list': list_, 'form': form})

def view_item(request, list_id, item_id):
    try:
        list_ = List.objects.get(id=list_id)
        item = Item.objects.get(id=item_id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound()
    if request.method not in ('DELETE',):
        return HttpResponseBadRequest()
    if item is not None:
        item.delete()
    return redirect(list_)
