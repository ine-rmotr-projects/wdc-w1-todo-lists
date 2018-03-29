from unittest.mock import Mock


class Item(object):
    _COUNT = 0
    _OBJECTS = []

    objects = Mock()

    def __init__(self, *args, **kwargs):
        self.__class__._COUNT += 1
        self.__class__._OBJECTS.append(self)
        for k, v in kwargs.items():
            setattr(self, k, v)

    def save(self):
        pass

    @classmethod
    def _all(cls):
        obj = Mock()
        obj.__getitem__ = cls._getitem
        obj.count = Mock(return_value=cls._COUNT)
        return obj

    @classmethod
    def _getitem(cls, _, idx):
        return cls._OBJECTS[idx]

    @classmethod
    def _count(cls):
        return cls._COUNT


Item.objects.all = Item._all
Item.objects.count = Item._count
