from django.test import TestCase


class HomePageTest(TestCase):

    def test_home_page_renders_using_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_add_item(self):
        response = self.client.post('/', data={'item_text': 'Buy milk'})
        self.assertContains(response, 'Buy milk')

    def test_add_multiple_items(self):
        response = self.client.post('/', data={'item_text': 'Buy milk'})
        self.assertContains(response, 'Buy milk')
        response = self.client.post('/', data={'item_text': 'Take out trash'})
        self.assertContains(response, 'Buy milk')
        self.assertContains(response, 'Take out trash')
