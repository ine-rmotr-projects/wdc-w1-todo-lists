from django.shortcuts import render, redirect
from todo.models import Item, List


def home(request):
    if request.method == 'POST':
        item = Item(text=request.POST.get('item_text', None))
        item.save()
    return render(request, 'home.html', {'items': Item.objects.all()})

def new_list(request):
    list_ = List.objects.create()
    item = Item(text=request.POST.get('item_text', None),
                list=list_)
    item.save()
    return redirect(list_)

def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    if request.method == 'POST':
        item = Item(text=request.POST.get('item_text', None),
                    list=list_)
        item.save()
        return redirect(list_)
    return render(request, 'list.html', {'list': list_})