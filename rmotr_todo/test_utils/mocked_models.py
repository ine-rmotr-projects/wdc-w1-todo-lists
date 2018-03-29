from unittest.mock import Mock
from django.urls import reverse

class CleanObjects(object):
    def __enter__(self):
        Item.clean()
        List.clean()

    def __exit__(self, *args):
        Item.clean()
        List.clean()

class MockObject(object):

    def __init__(self, *args, **kwargs):
        for k, v, in kwargs.items():
            setattr(self, k, v)
        self._items = []

    @property
    def item_set(self):
        i_s =  MockIterator(self._items)
        i_s.all = self._all
        return i_s

    def _all(self):
        return self._items

    def _append(self, item):
        self._items.append(item)


class MockModel(object):
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


class ListObject(MockObject):

    def get_absolute_url(self):
        args = [self.id]
        rev =  reverse('view_list', args=args)
        return rev


class List(MockModel):
    ITEM_CLASS = ListObject


class ItemObject(MockObject):
    def __init__(self, *args, **kwargs):
        super(ItemObject, self).__init__(*args, **kwargs)
        self.save()

    def save(self):
        if hasattr(self, 'list'):
            self.list._append(self)


class Item(MockModel):
    ITEM_CLASS = ItemObject
