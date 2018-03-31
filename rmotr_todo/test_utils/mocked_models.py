from django.urls import reverse
from django.core.exceptions import ValidationError
from django.utils.html import escape
from django.forms.utils import ErrorDict
from types import SimpleNamespace


class CleanObjects(object):
    """
    Context manager to ensure Items and Lists are cleaned
    before and after tests.

    Simulates database wipes between tests
    """

    def __enter__(self):
        Item.clean()
        List.clean()

    def __exit__(self, *args):
        Item.clean()
        List.clean()


class MockObject(object):
    """ Mocks out a single item from a Django model """

    def __init__(self, *args, **kwargs):
        for k, v, in kwargs.items():
            setattr(self, k, v)
        self._items = []

    @property
    def item_set(self):
        i_s = MockIterator(self._items)
        i_s.all = self._all
        return i_s

    def _all(self):
        return self._items

    def _append(self, item):
        self._items.append(item)


class MockModel(object):
    """
    Mocks out a Django Model
    When using w/ patch use ._get() to properly simulate
    the way Django treats Models
    """
    _ACTIVE = None

    def __init__(self, **kwargs):
        self._clean()

    @classmethod
    def _get(cls):
        if cls._ACTIVE is None:
            cls._ACTIVE = cls()
        return cls._ACTIVE

    @classmethod
    def clean(cls):
        cls._get()._clean()

    def _clean(self):
        self.items = []
        # This is a messy hack to create thi .objects interface
        self.objects = MockIterator(self.items)
        self.objects.create = self._create
        self.objects.first = self._getfirst
        self.objects.all = self._all
        self.objects.count = self._count
        self.objects.first = self._getfirst
        self.objects.get = self._get_single_item

    def __call__(self, *args, **kwargs):
        return self._create(*args, **kwargs)

    def _create(self, *args, **kwargs):
        obj = self.ITEM_CLASS(*args, **kwargs)
        self.items.append(obj)
        obj.id = len(self.items)
        return obj

    def _getfirst(self):
        if len(self.items) > 0:
            return self.items[0]

    def _count(self):
        return len(self.items)

    def _all(self):
        return MockIterator(self.items)

    def _getitem(self, _, idx):
        return self._OBJECTS[idx]

    def _get_single_item(self, **kwargs):
        for item in self.items:
            match = True
            for attr, value in kwargs.items():
                if attr == 'id':
                    value = int(value)
                if getattr(item, attr) != value:
                    match = False
                    break
            if match:
                return item


class MockIterator(object):
    """
    Mocks out the iterable parts of the .objects
    interface for a Django Model
    """

    def __init__(self, iterable):
        self._iterable = iterable
        self._counter = 0

    def count(self):
        return len(self._iterable)

    def __iter__(self):
        self._counter = 0
        return self

    def __next__(self):
        if self._counter < len(self._iterable):
            item = self._iterable[self._counter]
            self._counter += 1
            return item
        raise StopIteration

    next = __next__

    def __getitem__(self, idx):
        return self._iterable[idx]


class ListObject(MockObject):

    def get_absolute_url(self):
        args = [self.id]
        return reverse('view_list', args=args)


class List(MockModel):
    ITEM_CLASS = ListObject


class ItemObject(MockObject):
    _DEBUG_NO_DUPLICATES_ACROSS_LISTS = False

    def __init__(self, DEBUG_OVERRIDE_LIST_SAVE=False, *args, **kwargs):
        super(ItemObject, self).__init__(*args, **kwargs)
        if not DEBUG_OVERRIDE_LIST_SAVE:
            self.save()

    def save(self):
        if hasattr(self, 'list'):
            self.list._append(self)

    def delete(self):
        self.list._items.remove(self)
        Item._get().items.remove(self)

    def full_clean(self):
        if self.__class__._DEBUG_NO_DUPLICATES_ACROSS_LISTS:
            for item in Item._get().items:
                if item is not self and item.text == self.text:
                    raise ValidationError('Duplicate items not allowed')
        if getattr(self, 'text', '') == '':
            raise ValidationError('Field "text" cannot be blank')
        if hasattr(self, 'list'):
            for item in self.list.item_set.all():
                if item is not self and item.text == self.text:
                    raise ValidationError('Duplicate items not allowed')


class Item(MockModel):
    ITEM_CLASS = ItemObject


class MockForm(object):
    def __init__(self, **kwargs):
        self.data = {}
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __getitem__(self, idx):
        return self.WIDGETS[idx]

    def as_p(self):
        result = ""
        for name, widget in self.WIDGETS.items():
            result += widget.as_p(name=name)
        return result

    def is_valid(self):
        model = self.MODEL_CLASS._get()
        item = model(**self.data)
        try:
            item.full_clean()
            valid = True
        except ValidationError:
            valid = False
        model.items.remove(item)
        return valid


class MockFormField(object):
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)


class TextInput(MockFormField):
    def as_p(self, name):
        form_input = '<input name="{}" id="id_{}" placeholder="{}" />'
        return form_input.format(escape(name), escape(name),
                                 escape(self.attrs['placeholder']))


class ItemForm(MockForm):
    _DEBUG_DO_NOT_SAVE_TO_LIST = False
    MODEL_CLASS = Item
    FIELDS = ('text',)
    WIDGETS = {'text': TextInput(attrs={'placeholder':
                                        'Enter a to-do item.'})}
    error_message = {'text': {'required':
                              "Blank list items are not permitted"}}

    def __init__(self, **kwargs):
        if 'data' in kwargs:
            kwargs['data'] = dict(kwargs['data'])
            text = kwargs['data'].get('text', '')
            if type(text) == list:
                text = text[0]
            kwargs['data']['text'] = text
        super(ItemForm, self).__init__(**kwargs)
        self.errors = {'text': [self.error_message['text']['required']]}

    def save(self, list_):
        if self.is_valid():
            if self._DEBUG_DO_NOT_SAVE_TO_LIST:
                item = Item._get()(list=None, DEBUG_OVERRIDE_LIST_SAVE=True, **self.data)
                return item
            item = Item._get()(list=list_, **self.data)
            item.save()
            return item
