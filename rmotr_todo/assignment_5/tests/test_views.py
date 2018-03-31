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
        super(HomePageTestPass, self).test_requires_login()

    @rmotr_tester(PASS)
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def test_home_redirects_to_authenticated_users_list(self):
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
        super(HomePageTestFail, self).test_requires_login()

    @rmotr_tester(FAIL)
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def test_home_redirects_to_authenticated_users_list(self):
        super(HomePageTestFail, self).test_home_redirects_to_authenticated_users_list()

'''
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
        super(NewListTestPass, self).test_add_item()

    @rmotr_tester(PASS)
    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def test_redirects_after_post(self):
        super(NewListTestPass, self).test_redirects_after_post()

    @rmotr_tester(PASS)
    def test_invalid_item_renders_home(self):
        super(NewListTestPass, self).test_invalid_item_renders_home()

    @rmotr_tester(PASS)
    def test_invalid_item_shows_error(self):
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
        super(NewListTestFail, self).test_add_item()

    @rmotr_tester(FAIL)
    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def test_redirects_after_post(self):
        super(NewListTestFail, self).test_redirects_after_post()

    @rmotr_tester(FAIL)
    def test_invalid_item_renders_home(self):
        super(NewListTestFail, self).test_invalid_item_renders_home()

    @rmotr_tester(FAIL)
    def test_invalid_item_shows_error(self):
        super(NewListTestFail, self).test_invalid_item_shows_error()

'''

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
        super(ListViewTestPass, self).test_uses_list_template()

    @rmotr_tester(PASS)
    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def test_only_shows_correct_items(self):
        super(ListViewTestPass, self).test_only_shows_correct_items()

    @rmotr_tester(PASS)
    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def test_passes_correct_list_to_template(self):
        super(ListViewTestPass, self).test_passes_correct_list_to_template()

    @rmotr_tester(PASS)
    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def test_able_to_add_items_to_existing_list(self):
        super(ListViewTestPass, self).test_able_to_add_items_to_existing_list()

    @rmotr_tester(PASS)
    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def test_invalid_input_does_not_save_to_db(self):
        super(ListViewTestPass, self).test_invalid_input_does_not_save_to_db()

    @rmotr_tester(PASS)
    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def test_invalid_input_renders_list_template(self):
        super(ListViewTestPass, self).test_invalid_input_renders_list_template()

    @rmotr_tester(PASS)
    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def test_invalid_input_shows_error_on_page(self):
        super(ListViewTestPass, self).test_invalid_input_shows_error_on_page()

    @rmotr_tester(PASS)
    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def test_raise_404_on_list_not_found(self):
        super(ListViewTestPass, self).test_raise_404_on_list_not_found()

    @rmotr_tester(PASS)
    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def test_shows_delete_button(self):
        super(ListViewTestPass, self).test_shows_delete_button()

    @rmotr_tester(PASS)
    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    @patch('todo.tests.test_views.ItemForm', ItemForm)
    def test_page_uses_item_form(self):
        super(ListViewTestPass, self).test_page_uses_item_form()

    @rmotr_tester(PASS)
    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def test_raise_403_error_if_wrong_user(self):
        super(ListViewTestPass, self).test_raise_403_error_if_wrong_user()

    @rmotr_tester(PASS)
    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def test_redirects_after_post(self):
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
        super(ListViewTestFail, self).test_uses_list_template()

    @rmotr_tester(FAIL)
    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def test_only_shows_correct_items(self):
        super(ListViewTestFail, self).test_only_shows_correct_items()

    @rmotr_tester(FAIL)
    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def test_passes_correct_list_to_template(self):
        super(ListViewTestFail, self).test_passes_correct_list_to_template()

    @rmotr_tester(FAIL)
    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def test_able_to_add_items_to_existing_list(self):
        super(ListViewTestFail, self).test_able_to_add_items_to_existing_list()

    @rmotr_tester(FAIL)
    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def test_invalid_input_does_not_save_to_db(self):
        with patch('test_utils.mocked_models.MockForm.is_valid') as always_valid:
            always_valid.return_value = True
            super(ListViewTestFail, self).test_invalid_input_does_not_save_to_db()

    @rmotr_tester(FAIL)
    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def test_invalid_input_renders_list_template(self):
        super(ListViewTestFail, self).test_invalid_input_renders_list_template()

    @rmotr_tester(FAIL)
    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def test_invalid_input_shows_error_on_page(self):
        super(ListViewTestFail, self).test_invalid_input_shows_error_on_page()

    @rmotr_tester(FAIL)
    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def test_raise_404_on_list_not_found(self):
        super(ListViewTestFail, self).test_raise_404_on_list_not_found()

    @rmotr_tester(FAIL)
    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def test_shows_delete_button(self):
        super(ListViewTestFail, self).test_shows_delete_button()

    @rmotr_tester(FAIL)
    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    @patch('todo.tests.test_views.ItemForm', ItemForm)
    def test_page_uses_item_form(self):
        super(ListViewTestFail, self).test_page_uses_item_form()

    @rmotr_tester(FAIL)
    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def test_raise_403_error_if_wrong_user(self):
        super(ListViewTestFail, self).test_raise_403_error_if_wrong_user()

    @rmotr_tester(FAIL)
    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def test_redirects_after_post(self):
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
        super(ItemEndpointTestPass, self).test_delete_item()

    @rmotr_tester(PASS)
    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def test_does_not_delete_if_not_post(self):
        super(ItemEndpointTestPass, self).test_does_not_delete_if_not_post()

    @rmotr_tester(PASS)
    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def test_raise_404_on_item_not_found(self):
        super(ItemEndpointTestPass, self).test_raise_404_on_item_not_found()

    @rmotr_tester(PASS)
    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def test_raise_403_on_wrong_user(self):
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
        super(ItemEndpointTestFail, self).test_delete_item()

    @rmotr_tester(FAIL)
    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def test_does_not_delete_if_not_post(self):
        super(ItemEndpointTestFail, self).test_does_not_delete_if_not_post()

    @rmotr_tester(FAIL)
    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def test_raise_404_on_item_not_found(self):
        super(ItemEndpointTestFail, self).test_raise_404_on_item_not_found()

    @rmotr_tester(FAIL)
    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def test_raise_403_on_wrong_user(self):
        super(ItemEndpointTestFail, self).test_raise_403_on_wrong_user()