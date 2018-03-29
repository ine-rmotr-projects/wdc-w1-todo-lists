from django.test import TestCase
from django.utils.html import escape
from todo.models import Item, List



class HomePageTest(TestCase):

    def test_home_page_renders_using_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')


class NewListTest(TestCase):

    def test_add_item(self):
        response = self.client.post('/lists/new',
                                    data={'item_text': 'Buy milk'})
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'Buy milk')

    def test_redirects_after_post(self):
        response = self.client.post('/lists/new',
                                    data={'item_text': 'Hello there'})
        new_list = List.objects.first()
        self.assertRedirects(response, "/lists/{}/".format(new_list.id))


class ListViewTest(TestCase):

    def test_uses_list_template(self):
        list_ = List.objects.create()
        response = self.client.get('/lists/{}/'.format(list_.id))
        self.assertTemplateUsed(response, 'list.html')

    def test_only_shows_correct_items(self):
        correct_list = List.objects.create()
        correct_1 = Item.objects.create(text='Buy milk',
                                        list=correct_list)
        correct_2 = Item.objects.create(text='Take out trash',
                                        list=correct_list)

        incorrect_list = List.objects.create()
        incorrect_1 = Item.objects.create(text="Don't show me",
                                          list=incorrect_list)
        incorrect_2 = Item.objects.create(text="Can't see me",
                                          list=incorrect_list)

        response = self.client.get("/lists/{}/".format(correct_list.id))

        self.assertContains(response, escape(correct_1.text))
        self.assertContains(response, escape(correct_2.text))
        self.assertNotContains(response, escape(incorrect_1.text))
        self.assertNotContains(response, escape(incorrect_2.text))

    def test_passes_correct_list_to_template(self):
        other_list = List.objects.create()
        correct_list = List.objects.create()
        response = self.client.get('/lists/{}/'.format(correct_list.id))
        self.assertEqual(response.context['list'], correct_list)

    def test_able_to_add_items_to_existing_list(self):
        List.objects.create()
        list_ = List.objects.create()

        self.client.post('/lists/{}/'.format(list_.id),
                         data={'item_text': 'New item'})

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'New item')
        self.assertEqual(new_item.list, list_)