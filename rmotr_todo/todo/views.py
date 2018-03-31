from django.shortcuts import render, redirect
from django.http import (HttpResponseBadRequest,
                         HttpResponseNotFound,
                         HttpResponseForbidden)
from django.contrib.auth.decorators import login_required
from todo.models import Item, List
from todo.forms import ItemForm
from django.core.exceptions import ObjectDoesNotExist


@login_required
def home(request):
    try:
        list_ = List.objects.get(user=request.user)
    except ObjectDoesNotExist:
        list_ = List.objects.create(user=request.user)
    return redirect(list_)


def view_list(request, list_id):
    try:
        list_ = List.objects.get(id=list_id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound()

    if not list_.owned_by(request.user):
        return HttpResponseForbidden()

    form = ItemForm()

    if request.method == 'POST':
        form = ItemForm(data=request.POST)
        if form.is_valid():
            form.save(list_=list_)
            return(redirect(list_))
    return render(request, 'list.html', {'list': list_, 'form': form})


def delete_item(request, list_id, item_id):
    try:
        list_ = List.objects.get(id=list_id)
        item = Item.objects.get(id=item_id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound()
    if not item.owned_by(request.user):
        return HttpResponseForbidden()
    if request.method == 'POST':
        item.delete()
    return redirect(list_)

