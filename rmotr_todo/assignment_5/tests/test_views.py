from todo.tests import test_views as views_tests
from test_utils.decorators import rmotr_tester, PASS, FAIL
from test_utils import mocked_models
from unittest.mock import patch, Mock
from assignment_5.fixtures.views import ItemForm


class HomePageTestPass(views_tests.HomePageTest):

    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def setUp(self):
        mocked_models.CleanObjects.setUp()
        super(HomePageTestPass, self).setUp()

    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def tearDown(self):
        mocked_models.CleanObjects.tearDown()
        super(HomePageTestPass, self).tearDown()

    @rmotr_tester(PASS)
    def test_requires_login(self):
        """
        Verifies that if a user is not logged in it redirects
        them to the login page
        """
        super(HomePageTestPass, self).test_requires_login()

    @rmotr_tester(PASS)
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def test_home_redirects_to_authenticated_users_list(self):
        """
        Tests that if we are logged in and request the homepage we are
        redirected to the user's list
        See client.login: https://docs.djangoproject.com/en/2.0/topics/testing/tools/#django.test.Client.login
        See Creating Users: https://docs.djangoproject.com/en/2.0/topics/auth/default/#creating-users
        
        """
        super(HomePageTestPass, self).test_home_redirects_to_authenticated_users_list()


class HomePageTestFail(views_tests.HomePageTest):

    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def setUp(self):
        mocked_models.CleanObjects.setUp()
        super(HomePageTestFail, self).setUp()

    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def tearDown(self):
        mocked_models.CleanObjects.tearDown()
        super(HomePageTestFail, self).tearDown()

    @rmotr_tester(FAIL)
    def test_requires_login(self):
        """
        Should fail if we are not redirected to login
        """
        super(HomePageTestFail, self).test_requires_login()

    @rmotr_tester(FAIL)
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def test_home_redirects_to_authenticated_users_list(self):
        """
        Should fail if an authenticated user is not redirected to their
        list
        """
        super(HomePageTestFail, self).test_home_redirects_to_authenticated_users_list()

'''
NewListTest is no longer required.

'''

class ListViewTestPass(views_tests.ListViewTest):
    """
    As the list view requires login to view it is advised that you
    handle user creation and login inside setUp to avoid repeating
    yourself.
    See setUp: https://docs.python.org/3/library/unittest.html#unittest.TestCase.setUp
    """

    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def setUp(self):
        mocked_models.CleanObjects.setUp()
        super(ListViewTestPass, self).setUp()

    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def tearDown(self):
        mocked_models.CleanObjects.tearDown()
        super(ListViewTestPass, self).tearDown()

    @rmotr_tester(PASS)
    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def test_uses_list_template(self):
        """ Unchanged from previous assignment """
        super(ListViewTestPass, self).test_uses_list_template()

    @rmotr_tester(PASS)
    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def test_only_shows_correct_items(self):
        """ May require changes due to user implementation """
        super(ListViewTestPass, self).test_only_shows_correct_items()

    @rmotr_tester(PASS)
    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def test_passes_correct_list_to_template(self):
        """ May require changes due to user implementation """
        super(ListViewTestPass, self).test_passes_correct_list_to_template()

    @rmotr_tester(PASS)
    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def test_able_to_add_items_to_existing_list(self):
        """ Unchanged from previous assignment """
        super(ListViewTestPass, self).test_able_to_add_items_to_existing_list()

    @rmotr_tester(PASS)
    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def test_invalid_input_does_not_save_to_db(self):
        """ Unchanged from previous assignment """
        super(ListViewTestPass, self).test_invalid_input_does_not_save_to_db()

    @rmotr_tester(PASS)
    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def test_invalid_input_renders_list_template(self):
        """ Unchanged from previous assignment """
        super(ListViewTestPass, self).test_invalid_input_renders_list_template()

    @rmotr_tester(PASS)
    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def test_invalid_input_shows_error_on_page(self):
        """ Unchanged from previous assignment """
        super(ListViewTestPass, self).test_invalid_input_shows_error_on_page()

    @rmotr_tester(PASS)
    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def test_raise_404_on_list_not_found(self):
        """ Unchanged from previous assignment """
        super(ListViewTestPass, self).test_raise_404_on_list_not_found()

    @rmotr_tester(PASS)
    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def test_shows_delete_button(self):
        """ Unchanged from previous assignment """
        super(ListViewTestPass, self).test_shows_delete_button()

    @rmotr_tester(PASS)
    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    @patch('todo.tests.test_views.ItemForm', ItemForm)
    def test_page_uses_item_form(self):
        """
        Re-implemented from HomePageTest as it no longer applies there
        """
        super(ListViewTestPass, self).test_page_uses_item_form()

    @rmotr_tester(PASS)
    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def test_raise_403_error_if_wrong_user(self):
        """
        Tests that we return a 403 if the user trying to view the page
        is not the owner
        """
        super(ListViewTestPass, self).test_raise_403_error_if_wrong_user()

    @rmotr_tester(PASS)
    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def test_redirects_after_post(self):
        """
        Re-implemented from NewListTest
        """
        super(ListViewTestPass, self).test_redirects_after_post()


class ListViewTestFail(views_tests.ListViewTest):
    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def setUp(self):
        mocked_models.CleanObjects().setUp()
        super(ListViewTestFail, self).setUp()

    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def tearDown(self):
        mocked_models.CleanObjects().tearDown()
        super(ListViewTestFail, self).tearDown()

    @rmotr_tester(FAIL)
    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def test_uses_list_template(self):
        """ Unchanged from previous assignment """
        super(ListViewTestFail, self).test_uses_list_template()

    @rmotr_tester(FAIL)
    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def test_only_shows_correct_items(self):
        """ Unchanged from previous assignment """
        super(ListViewTestFail, self).test_only_shows_correct_items()

    @rmotr_tester(FAIL)
    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def test_passes_correct_list_to_template(self):
        """ Unchanged from previous assignment """
        super(ListViewTestFail, self).test_passes_correct_list_to_template()

    @rmotr_tester(FAIL)
    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def test_able_to_add_items_to_existing_list(self):
        """ Unchanged from previous assignment """
        super(ListViewTestFail, self).test_able_to_add_items_to_existing_list()

    @rmotr_tester(FAIL)
    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def test_invalid_input_does_not_save_to_db(self):
        """ Unchanged from previous assignment """
        with patch('test_utils.mocked_models.MockForm.is_valid') as always_valid:
            always_valid.return_value = True
            super(ListViewTestFail, self).test_invalid_input_does_not_save_to_db()

    @rmotr_tester(FAIL)
    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def test_invalid_input_renders_list_template(self):
        """ Unchanged from previous assignment """
        super(ListViewTestFail, self).test_invalid_input_renders_list_template()

    @rmotr_tester(FAIL)
    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def test_invalid_input_shows_error_on_page(self):
        """ Unchanged from previous assignment """
        super(ListViewTestFail, self).test_invalid_input_shows_error_on_page()

    @rmotr_tester(FAIL)
    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def test_raise_404_on_list_not_found(self):
        """ Unchanged from previous assignment """
        super(ListViewTestFail, self).test_raise_404_on_list_not_found()

    @rmotr_tester(FAIL)
    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def test_shows_delete_button(self):
        """ Unchanged from previous assignment """
        super(ListViewTestFail, self).test_shows_delete_button()

    @rmotr_tester(FAIL)
    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    @patch('todo.tests.test_views.ItemForm', ItemForm)
    def test_page_uses_item_form(self):
        """
        Should fail if not using ItemForm in rendering of page
        """
        super(ListViewTestFail, self).test_page_uses_item_form()

    @rmotr_tester(FAIL)
    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def test_raise_403_error_if_wrong_user(self):
        """
        Should fail if we are able to view other users' lists
        """
        super(ListViewTestFail, self).test_raise_403_error_if_wrong_user()

    @rmotr_tester(FAIL)
    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def test_redirects_after_post(self):
        """
        Should fail if we do not redirect after a POST
        """
        super(ListViewTestFail, self).test_redirects_after_post()


class ItemEndpointTestPass(views_tests.ItemEndpointTest):

    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def setUp(self):
        mocked_models.CleanObjects.setUp()
        super(ItemEndpointTestPass, self).setUp()

    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def tearDown(self):
        mocked_models.CleanObjects.tearDown()
        super(ItemEndpointTestPass, self).tearDown()

    @rmotr_tester(PASS)
    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def test_delete_item(self):
        """ Unchanged from previous assignment """
        super(ItemEndpointTestPass, self).test_delete_item()

    @rmotr_tester(PASS)
    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def test_does_not_delete_if_not_post(self):
        """ Unchanged from previous assignment """
        super(ItemEndpointTestPass, self).test_does_not_delete_if_not_post()

    @rmotr_tester(PASS)
    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def test_raise_404_on_item_not_found(self):
        """ Unchanged from previous assignment """
        super(ItemEndpointTestPass, self).test_raise_404_on_item_not_found()

    @rmotr_tester(PASS)
    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def test_raise_403_on_wrong_user(self):
        """
        Verify that we return a 403 if a user tries to delete something
        that they do not own
        """
        super(ItemEndpointTestPass, self).test_raise_403_on_wrong_user()

class ItemEndpointTestFail(views_tests.ItemEndpointTest):

    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def setUp(self):
        mocked_models.CleanObjects.setUp()
        super(ItemEndpointTestFail, self).setUp()

    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def tearDown(self):
        mocked_models.CleanObjects.tearDown()
        super(ItemEndpointTestFail, self).tearDown()

    @rmotr_tester(FAIL)
    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def test_delete_item(self):
        """ Unchanged from previous assignment """
        super(ItemEndpointTestFail, self).test_delete_item()

    @rmotr_tester(FAIL)
    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def test_does_not_delete_if_not_post(self):
        """ Unchanged from previous assignment """
        super(ItemEndpointTestFail, self).test_does_not_delete_if_not_post()

    @rmotr_tester(FAIL)
    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def test_raise_404_on_item_not_found(self):
        """ Unchanged from previous assignment """
        super(ItemEndpointTestFail, self).test_raise_404_on_item_not_found()

    @rmotr_tester(FAIL)
    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def test_raise_403_on_wrong_user(self):
        """
        Should fail if we do not return a 403, or even worse allow
        deletion by a user who in not the owner
        """
        super(ItemEndpointTestFail, self).test_raise_403_on_wrong_user()