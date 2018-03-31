from django.test import TestCase
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.contrib.auth.models import User
from todo.models import Item, List


class ItemAndListModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user('obiwan',
                                             'kenobi@jedi.org',
                                             'hellothere')

    def test_item_saves_to_list(self):
        list_ = List.objects.create(user=self.user)
        item = Item(text="Buy milk")
        item.list = list_
        item.save()
        self.assertIn(item, list_.item_set.all())

    def test_get_absolute_url(self):
        list_ = List.objects.create(user=self.user)
        self.assertEqual(list_.get_absolute_url(),
                         '/lists/{}/'.format(list_.id))

    def test_cannot_save_empty_list_items(self):
        list_ = List.objects.create(user=self.user)
        item = Item(list=list_, text='')
        with self.assertRaises(ValidationError):
            item.save()
            item.full_clean()

    def test_duplicate_items_not_allowed(self):
        list_ = List.objects.create(user=self.user)
        Item.objects.create(list=list_, text='Hello there')
        with self.assertRaises(ValidationError):
            item = Item(list=list_, text='Hello there')
            item.full_clean()

    def test_able_to_save_same_item_to_different_lists(self):
        list1 = List.objects.create(user=self.user)
        list2 = List.objects.create(user=self.user)
        Item.objects.create(list=list1, text='Hello there')
        item = Item(list=list2, text='Hello there')
        item.full_clean()

    def test_ownership(self):
        list_ = List.objects.create(user=self.user)
        self.assertTrue(list_.owned_by(self.user))
        item = Item.objects.create(list=list_, text='Hello there')
        self.assertTrue(item.owned_by(self.user))
