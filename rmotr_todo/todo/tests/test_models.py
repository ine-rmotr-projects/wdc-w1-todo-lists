from django.test import TestCase
from todo.models import Item, List


class ItemAndListModelTest(TestCase):

    def test_item_saves_to_list(self):
        list_ = List.objects.create()
        item = Item(text="Hello there")
        item.list = list_
        item.save()
        self.assertIn(item, list_.item_set.all())

    def test_get_absolute_url(self):
        list_ = List.objects.create()
        self.assertEqual(list_.get_absolute_url(),
                         '/lists/{}/'.format(list_.id))
