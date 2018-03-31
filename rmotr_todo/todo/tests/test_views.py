from django.test import TestCase
from django.utils.html import escape
from django.contrib.auth.models import User
from todo.models import Item, List
from todo.forms import ItemForm, EMPTY_ITEM_ERROR


class HomePageTest(TestCase):

    def test_requires_login(self):
        response = self.client.get('/')
        self.assertRedirects(response, '/login?next=/')

    def test_home_redirects_to_authenticated_users_list(self):
        user = User.objects.create_user('obiwan', 'kenobi@jedi.org', 'hellothere')
        list_ = List.objects.create(user=user)
        self.client.login(username='obiwan', password='hellothere')
        response = self.client.get('/')
        self.assertRedirects(response, '/lists/{}/'.format(list_.id))


class ListViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user('obiwan',
                                             'obiwan@jedi.org',
                                             'hellothere')
        self.list_ = List.objects.create(user=self.user)
        self.client.login(username='obiwan', password='hellothere')
        self.list_url = '/lists/{}/'.format(self.list_.id)

    def test_uses_list_template(self):
        response = self.client.get(self.list_url)
        self.assertTemplateUsed(response, 'list.html')

    def test_only_shows_correct_items(self):
        correct_1 = Item.objects.create(text='Buy milk',
                                        list=self.list_)
        correct_2 = Item.objects.create(text='Take out trash',
                                        list=self.list_)

        other_user = User.objects.create_user('yoda',
                                              'yoda@jedi.org',
                                              'thereisnotry')

        incorrect_list = List.objects.create(user=other_user)
        incorrect_1 = Item.objects.create(text="Don't show me",
                                          list=incorrect_list)
        incorrect_2 = Item.objects.create(text="Can't see me",
                                          list=incorrect_list)

        response = self.client.get(self.list_url)

        self.assertContains(response, escape(correct_1.text))
        self.assertContains(response, escape(correct_2.text))
        self.assertNotContains(response, escape(incorrect_1.text))
        self.assertNotContains(response, escape(incorrect_2.text))

    def test_passes_correct_list_to_template(self):
        other_user = User.objects.create_user('yoda',
                                              'yoda@jedi.org',
                                              'thereisnotry')
        other_list = List.objects.create(user=other_user)
        correct_list = List.objects.create(user=self.user)
        response = self.client.get('/lists/{}/'.format(correct_list.id))
        self.assertEqual(response.context['list'], correct_list)

    def test_able_to_add_items_to_existing_list(self):
        self.client.post(self.list_url,
                         data={'text': 'New item'})

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'New item')
        self.assertEqual(new_item.list, self.list_)

    def test_invalid_input_does_not_save_to_db(self):
        self.client.post(self.list_url,
                         data={'text': ''})
        self.assertEqual(Item.objects.count(), 0)

    def test_invalid_input_renders_list_template(self):
        response = self.client.post(self.list_url,
                                    data={'text': ''})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'list.html')

    def test_invalid_input_shows_error_on_page(self):
        response = self.client.post(self.list_url,
                                    data={'text': ''})
        self.assertContains(response, escape(EMPTY_ITEM_ERROR))

    def test_raise_404_on_list_not_found(self):
        response = self.client.get('/lists/{}1/'.format(self.list_.id))
        self.assertEqual(response.status_code, 404)

    def test_shows_delete_button(self):
        item = Item.objects.create(list=self.list_, text="Hello there")

        response = self.client.get(self.list_url)
        delete_url = "/lists/{}/item/{}/delete".format(self.list_.id, item.id)

        self.assertContains(response, delete_url)

    def test_page_uses_item_form(self):
        response = self.client.get(self.list_url)
        self.assertIsInstance(response.context['form'], ItemForm)

    def test_redirects_after_post(self):
        response = self.client.post(self.list_url, data={'text': 'Buy milk'})
        self.assertRedirects(response, self.list_url)

    def test_raise_403_error_if_wrong_user(self):
        other_user = User.objects.create_user('yoda',
                                              'yoda@jedi.org',
                                              'thereisnotry')
        other_list = List.objects.create(user=other_user)
        response = self.client.get('/lists/{}/'.format(other_list.id))
        self.assertEqual(response.status_code, 403)


class ItemEndpointTest(TestCase):

    def setUp(self):
        user = User.objects.create_user('obiwan',
                                        'kenobi@jedi.org',
                                        'hellothere')
        self.list_ = List.objects.create(user=user)
        self.item = Item.objects.create(list=self.list_, text='Hello there')
        self.delete_url = '/lists/{}/item/{}/delete'.format(self.list_.id,
                                                            self.item.id)
        self.client.login(username='obiwan', password='hellothere')

    def test_delete_item(self):
        self.assertEqual(Item.objects.count(), 1)
        response = self.client.post(self.delete_url)
        self.assertEqual(Item.objects.count(), 0)

    def test_does_not_delete_if_not_post(self):
        self.assertEqual(Item.objects.count(), 1)
        response = self.client.get(self.delete_url)
        self.assertEqual(Item.objects.count(), 1)

    def test_raise_404_on_item_not_found(self):
        response = self.client.post('/lists/{}/item/{}1/delete'.format(self.list_.id,
                                                                       self.item.id))
        self.assertEqual(response.status_code, 404)

    def test_raise_403_on_wrong_user(self):
        other_user = User.objects.create_user('yoda',
                                              'yoda@jedi.org',
                                              'thereisnotry')
        self.client.login(username='yoda', password='thereisnotry')
        response = self.client.post(self.delete_url)
        self.assertEqual(response.status_code, 403)
        


class LoginTest(TestCase):

    def setUp(self):
        self.username = 'obiwan'
        self.password = 'hellothere'
        self.email = 'obiwan.kenobi@jedi.org'
        self.user = User.objects.create_user(self.username,
                                             self.email,
                                             self.password)

    def test_uses_login_template(self):
        response = self.client.get('/login')
        self.assertTemplateUsed(response, 'login.html')

    def test_successful_login(self):
        response = self.client.post('/login', data={'username': self.username,
                                                    'password': self.password})
        
        self.assertTrue(self.user.is_authenticated)
