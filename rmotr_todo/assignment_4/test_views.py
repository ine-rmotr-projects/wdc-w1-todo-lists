from django.test import TestCase
from django.utils.html import escape
from todo.models import Item, List
from todo.forms import ItemForm, EMPTY_ITEM_ERROR


class HomePageTest(TestCase):

    def test_home_page_renders_using_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_home_page_uses_item_form(self):
        response = self.client.get('/')
        self.assertIsInstance(response.context['form'], ItemForm)


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

        self.assertContains(response, correct_1.text)
        self.assertContains(response, correct_2.text)
        self.assertNotContains(response, incorrect_1.text)
        self.assertNotContains(response, incorrect_2.text)

    def test_passes_correct_list_to_template(self):
        other_list = List.objects.create()
        correct_list = List.objects.create()
        response = self.client.get('/lists/{}/'.format(correct_list.id))
        self.assertEqual(response.context['list'], correct_list)

    def test_able_to_add_items_to_existing_list(self):
        List.objects.create()
        list_ = List.objects.create()

        self.client.post('/lists/{}/'.format(list_.id),
                         data={'text': 'New item'})

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'New item')
        self.assertEqual(new_item.list, list_)

    def test_invalid_input_does_not_save_to_db(self):
        list_ = List.objects.create()
        self.client.post('/lists/{}/'.format(list_.id),
                         data={'text': ''})
        self.assertEqual(Item.objects.count(), 0)

    def test_invalid_input_renders_list_template(self):
        list_ = List.objects.create()
        response = self.client.post('/lists/{}/'.format(list_.id),
                                    data={'text': ''})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'list.html')

    def test_invalid_input_shows_error_on_page(self):
        list_ = List.objects.create()
        response = self.client.post('/lists/{}/'.format(list_.id),
                                    data={'text': ''})
        self.assertContains(response, escape(EMPTY_ITEM_ERROR))

    def test_raise_404_on_list_not_found(self):
        list_ = List.objects.create()
        response = self.client.get('/lists/{}1/'.format(list_.id))
        self.assertEqual(response.status_code, 404)

    def test_shows_delete_button(self):
        list_ = List.objects.create()
        item = Item.objects.create(list=list_, text="Hello there")

        response = self.client.get('/lists/{}/'.format(list_.id))
        delete_url = "/lists/{}/item/{}/delete".format(list_.id, item.id)

        self.assertContains(response, delete_url)


class ItemEndpointTest(TestCase):

    def setUp(self):
        self.list_ = List.objects.create()
        self.item = Item.objects.create(list=self.list_, text='Hello there')

    def test_delete_item(self):
        self.assertEqual(Item.objects.count(), 1)
        response = self.client.post('/lists/{}/item/{}/delete'.format(self.list_.id,
                                                                      self.item.id))
        self.assertEqual(Item.objects.count(), 0)

    def test_does_not_delete_if_not_post(self):
        self.assertEqual(Item.objects.count(), 1)
        response = self.client.get('/lists/{}/item/{}/delete'.format(self.list_.id,
                                                                     self.item.id))
        self.assertEqual(Item.objects.count(), 1)

    def test_raise_404_on_item_not_found(self):
        response = self.client.post('/lists/{}/item/{}1/delete'.format(self.list_.id,
                                                                 self.item.id))
        self.assertEqual(response.status_code, 404)


class NewListTest(TestCase):

    def test_add_item(self):
        response = self.client.post('/lists/new', data={'text': 'Buy milk'})
        
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'Buy milk')

    def test_redirects_after_post(self):
        response = self.client.post('/lists/new', data={'text': 'Buy milk'})
        new_list = List.objects.first()
        self.assertRedirects(response, "/lists/{}/".format(new_list.id))

    def test_invalid_item_renders_home(self):
        response = self.client.post('/lists/new', data={'text': ''})
        self.assertTemplateUsed(response, 'home.html')

    def test_invalid_item_shows_error(self):
        response = self.client.post('/lists/new', data={'text': ''})
        self.assertContains(response, escape(EMPTY_ITEM_ERROR))
