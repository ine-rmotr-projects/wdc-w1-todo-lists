from todo.tests import test_views as views_tests
from test_utils.decorators import rmotr_tester, PASS, FAIL
from test_utils import mocked_models
from unittest.mock import patch, Mock
from assignment_4.fixtures.views import ItemForm


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
    def test_home_page_renders_using_template(self):
        """ Unchanged from previous assignment """
        super(HomePageTestPass, self).test_home_page_renders_using_template()

    @rmotr_tester(PASS)
    @patch('todo.tests.test_views.ItemForm', ItemForm)
    def test_home_page_uses_item_form(self):
        """ Unchanged from previous assignment """
        super(HomePageTestPass, self).test_home_page_uses_item_form()


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
    def test_home_page_renders_using_template(self):
        """ Unchanged from previous assignment """
        super(HomePageTestFail, self).test_home_page_renders_using_template()

    @rmotr_tester(FAIL)
    def test_home_page_uses_item_form(self):
        """ Unchanged from previous assignment """
        super(HomePageTestFail, self).test_home_page_uses_item_form()


class NewListTestPass(views_tests.NewListTest):

    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def setUp(self):
        mocked_models.CleanObjects.setUp()
        super(NewListTestPass, self).setUp()

    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def tearDown(self):
        mocked_models.CleanObjects.tearDown()
        super(NewListTestPass, self).tearDown()

    @rmotr_tester(PASS)
    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def test_add_item(self):
        """ Unchanged from previous assignment """
        super(NewListTestPass, self).test_add_item()

    @rmotr_tester(PASS)
    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def test_redirects_after_post(self):
        """ Unchanged from previous assignment """
        super(NewListTestPass, self).test_redirects_after_post()

    @rmotr_tester(PASS)
    def test_invalid_item_renders_home(self):
        """ Unchanged from previous assignment """
        super(NewListTestPass, self).test_invalid_item_renders_home()

    @rmotr_tester(PASS)
    def test_invalid_item_shows_error(self):
        """ Unchanged from previous assignment """
        super(NewListTestPass, self).test_invalid_item_shows_error()



class NewListTestFail(views_tests.NewListTest):

    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def setUp(self):
        mocked_models.CleanObjects.setUp()
        super(NewListTestFail, self).setUp()

    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def tearDown(self):
        mocked_models.CleanObjects.tearDown()
        super(NewListTestFail, self).tearDown()

    @rmotr_tester(FAIL)
    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def test_add_item(self):
        """ Unchanged from previous assignment """
        super(NewListTestFail, self).test_add_item()

    @rmotr_tester(FAIL)
    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def test_redirects_after_post(self):
        """ Unchanged from previous assignment """
        super(NewListTestFail, self).test_redirects_after_post()

    @rmotr_tester(FAIL)
    def test_invalid_item_renders_home(self):
        """ Unchanged from previous assignment """
        super(NewListTestFail, self).test_invalid_item_renders_home()

    @rmotr_tester(FAIL)
    def test_invalid_item_shows_error(self):
        """ Unchanged from previous assignment """
        super(NewListTestFail, self).test_invalid_item_shows_error()

class ListViewTestPass(views_tests.ListViewTest):

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
        """ Unchanged from previous assignment """
        super(ListViewTestPass, self).test_only_shows_correct_items()

    @rmotr_tester(PASS)
    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def test_passes_correct_list_to_template(self):
        """ Unchanged from previous assignment """
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
        """
        Ensure that when a list matching the given id is not found
        we return a 404
        See response.status_code: https://docs.djangoproject.com/en/2.0/topics/testing/tools/#django.test.Response.status_code
        """
        super(ListViewTestPass, self).test_raise_404_on_list_not_found()

    @rmotr_tester(PASS)
    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def test_shows_delete_button(self):
        """
        Ensure that list items now include a delete form as part of their
        listing. ie. search for appropriate deletion url in rendered page
        """
        super(ListViewTestPass, self).test_shows_delete_button()


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
        """
        Should fail if status code is not 404 on a request with an invalid
        list id
        """
        super(ListViewTestFail, self).test_raise_404_on_list_not_found()

    @rmotr_tester(FAIL)
    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def test_shows_delete_button(self):
        """
        Should fail if deletion forms are not in rendered page
        """
        super(ListViewTestFail, self).test_shows_delete_button()


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
        """
        Ensure that when delete request is POSTed that the item
        is deleted.
        """
        super(ItemEndpointTestPass, self).test_delete_item()

    @rmotr_tester(PASS)
    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def test_does_not_delete_if_not_post(self):
        """
        Test that item is not deleted if the request is not a POST
        request (a GET request for example)
        """
        super(ItemEndpointTestPass, self).test_does_not_delete_if_not_post()

    @rmotr_tester(PASS)
    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def test_raise_404_on_item_not_found(self):
        """
        Test that we return a 404 if we can't find the item requested
        """
        super(ItemEndpointTestPass, self).test_raise_404_on_item_not_found()

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
        """
        Should fail if item is not deleted
        """
        super(ItemEndpointTestFail, self).test_delete_item()

    @rmotr_tester(FAIL)
    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def test_does_not_delete_if_not_post(self):
        """
        Should fail if we delete for a GET request
        """
        super(ItemEndpointTestFail, self).test_does_not_delete_if_not_post()

    @rmotr_tester(FAIL)
    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def test_raise_404_on_item_not_found(self):
        """
        Should fail if we don't get a 404 on an invalid item id
        """
        super(ItemEndpointTestFail, self).test_raise_404_on_item_not_found()