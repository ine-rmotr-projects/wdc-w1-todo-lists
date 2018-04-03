from django.test import TestCase
from django.core.exceptions import ValidationError
from todo.models import Item, List


class ItemAndListModelTest(TestCase):

    def test_item_saves_to_list(self):
        list_ = List.objects.create()
        item = Item(text="Buy milk")
        item.list = list_
        item.save()
        self.assertIn(item, list_.item_set.all())

    def test_get_absolute_url(self):
        list_ = List.objects.create()
        self.assertEqual(list_.get_absolute_url(),
                         '/lists/{}/'.format(list_.id))

    def test_cannot_save_empty_list_items(self):
        list_ = List.objects.create()
        item = Item(list=list_, text='')
        with self.assertRaises(ValidationError):
            item.save()
            item.full_clean()

    def test_duplicate_items_not_allowed(self):
        list_ = List.objects.create()
        Item.objects.create(list=list_, text='Hello there')
        with self.assertRaises(ValidationError):
            item = Item(list=list_, text='Hello there')
            item.full_clean()

    def test_able_to_save_same_item_to_different_lists(self):
        list1 = List.objects.create()
        list2 = List.objects.create()
        Item.objects.create(list=list1, text='Hello there')
        item = Item(list=list2, text='Hello there')
        item.full_clean()