from unittest.mock import Mock


class MockObject(object):

    def __init__(self, *args, **kwargs):
        for k, v, in kwargs.items():
            setattr(self, k, v)
        self._items = []
        self.item_set = Mock()
        self.item_set.all = self._all

    def _all(self):
        return self._items

    def _append(self, item):
        self._items.append(item)


class MockModel(object):

    def __init__(self, **kwargs):
        self.count = 0
        self.items = []
        self.objects = Mock()
        self.objects.create = self._create
        self.objects.first = self._getfirst
        self.objects.all = self._all
        self.objects.count = self._count
        self.objects.first = self._getfirst

    def __call__(self, *args, **kwargs):
        return self._create(*args, **kwargs)

    def _create(self, *args, **kwargs):
        self.count += 1
        obj = self.ITEM_CLASS(*args, id=self.count, **kwargs)
        self.items.append(obj)
        return obj

    def _getfirst(self):
        if len(self.items) > 0:
            return self.items[0]

    def _count(self):
        return self.count

    def _all(self):
        obj = Mock()
        obj.__getitem__ = self._getitem
        obj.count = Mock(return_value=self._count)
        return obj

    def _getitem(self, _, idx):
        return self._OBJECTS[idx]


class ListObject(MockObject):

    def get_absolute_url(self):
        return '/lists/{}/'.format(self.id)


class List(MockModel):
    ITEM_CLASS = ListObject


class ItemObject(MockObject):
    def save(self):
        if hasattr(self, 'list'):
            self.list.append(self)


class Item(MockModel):
    ITEM_CLASS = ItemObject
