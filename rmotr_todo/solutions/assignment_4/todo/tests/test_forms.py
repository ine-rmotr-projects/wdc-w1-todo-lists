from django.test import TestCase

from todo.models import Item, List
from todo.forms import ItemForm, EMPTY_ITEM_ERROR


class ItemFormTest(TestCase):

    def test_form_renders_item_text_input(self):
        form = ItemForm()
        self.assertIn('placeholder="Enter a to-do item."', form.as_p())

    def test_form_validation_for_blank_items(self):
        form = ItemForm(data={'text': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['text'], [EMPTY_ITEM_ERROR])

    def test_form_save_handles_saving_to_a_list(self):
        list_ = List.objects.create()
        form = ItemForm(data={'text': 'Hello there'})
        new_item = form.save(list_=list_)
        self.assertEqual(new_item, Item.objects.first())
        self.assertEqual(new_item.text, 'Hello there')
        self.assertEqual(new_item.list, list_)
