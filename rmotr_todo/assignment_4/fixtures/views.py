from django.shortcuts import render, redirect
from test_utils import mocked_models
from django import forms
from django.db import models
from django.http import HttpResponse, HttpResponseNotFound

Item = mocked_models.Item._get()
List = mocked_models.List._get()

class FakeItem(models.Model):

    text = models.TextField(default='')
    list = models.TextField(default='')

    class Meta:
        app_label = 'todo'
        unique_together = ('list', 'text')

    def __str__(self):
        return self.text


class ItemForm(forms.models.ModelForm):

    class Meta:
        model = FakeItem
        fields = ('text',)
        widgets = {'text':
                   forms.fields.TextInput(attrs={'placeholder':
                                                 'Enter a to-do item.'})}
        error_messages = {'text': {'required': "Blank list items are not permitted"}}

    def save(self, list_):
        self.instance.list = list_
        return super().save()

class OtherForm(ItemForm):
    pass


def home(request, **kwargs):
    return render(request, 'home.html', {'form': ItemForm()})


def no_template(request, *args, **kwargs):
    response = HttpResponse("Text only, please.", content_type="text/plain")
    return response

def home_wrong_form(request):
    return render(request, 'home.html', {'form': OtherForm()})


def new_list(request):
    form = mocked_models.ItemForm(data=request.POST)
    if form.is_valid():
        list_ = List.objects.create()
        Item.objects.create(text=request.POST['text'], list=list_)
        return redirect(list_)
    else:
        return render(request, 'home.html', {'form': form})


def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    form = mocked_models.ItemForm()

    if list_ is None:
        return HttpResponseNotFound()

    if request.method == 'POST':
        form = mocked_models.ItemForm(data=request.POST)
        if form.is_valid():
            form.save(list_=list_)
            return(redirect(list_))
    return render(request, 'list.html', {'list': list_, 'form': form})

def new_list_redirects_home(request):
    list_ = List.objects.create()
    item = Item(text=request.POST.get('item_text', None),
                list=list_)
    item.save()
    return redirect('home')

def new_list_no_create_item(request):
    list_ = List.objects.create()
    return redirect(list_)

def view_list_add_to_existing(request, list_id):
    list_ = List.objects.get(id=list_id)
    form = mocked_models.ItemForm()

    if request.method == 'POST':
        form = mocked_models.ItemForm(data=request.POST)
        if form.is_valid():
            form.save(list_=list_)
            return(redirect(list_))
    return render(request, 'list.html', {'list': list_, 'form': form})

def show_errors(request, *args, **kwargs):
    return render(request, 'errors.html')


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


def view_list_doesnt_add_items(request, list_id):
    list_ = List.objects.get(id=list_id)
    if request.method == 'POST':
        pass
    return render(request, 'list.html', {'list': list_})

def delete_item(request, list_id, item_id):
    try:
        list_ = List.objects.get(id=list_id)
        item = Item.objects.get(id=item_id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound()
    if list_ is None or item is None:
        return HttpResponseNotFound()
    if request.method == 'POST':
        item.delete()
    return redirect(list_)

def delete_even_not_post(request, list_id, item_id):
    try:
        list_ = List.objects.get(id=list_id)
        item = Item.objects.get(id=item_id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound()
    if list_ is None or item is None:
        return HttpResponseNotFound()
    item.delete()
    return redirect(list_)

def view_list_creates_new_on_404(request, list_id):
    list_ = List.objects.get(id=list_id)
    form = mocked_models.ItemForm()

    if list_ is None:
        list_ = List()

    if request.method == 'POST':
        form = mocked_models.ItemForm(data=request.POST)
        if form.is_valid():
            form.save(list_=list_)
            return(redirect(list_))
    return render(request, 'list.html', {'list': list_, 'form': form})


def view_list_no_delete_button(request, list_id):
    list_ = List.objects.get(id=list_id)
    form = mocked_models.ItemForm()

    if list_ is None:
        return HttpResponseNotFound()

    if request.method == 'POST':
        form = mocked_models.ItemForm(data=request.POST)
        if form.is_valid():
            form.save(list_=list_)
            return(redirect(list_))
    return render(request, 'list_no_delete_button.html', {'list': list_, 'form': form})
