from django.test import TestCase


class LoginTest(TestCase):

    def test_login_page_renders_login_template(self):
        response = self.client.get('/login')
        self.assertTemplateUsed(response, 'login.html')

