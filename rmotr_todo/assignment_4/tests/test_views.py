from todo.tests import test_views as views_tests
from test_utils.decorators import rmotr_tester, PASS, FAIL
from test_utils import mocked_models
from unittest.mock import patch, Mock
from assignment_4.fixtures.views import ItemForm


class HomePageTestPass(views_tests.HomePageTest):

    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def setUp(self):
        mocked_models.CleanObjects().__enter__()
        super(HomePageTestPass, self).setUp()

    def tearDown(self):
        mocked_models.CleanObjects().__exit__()

    @rmotr_tester(PASS)
    def test_home_page_renders_using_template(self):
        super(HomePageTestPass, self).test_home_page_renders_using_template()

    @rmotr_tester(PASS)
    @patch('todo.tests.test_views.ItemForm', ItemForm)
    def test_home_page_uses_item_form(self):
        super(HomePageTestPass, self).test_home_page_uses_item_form()


class HomePageTestFail(views_tests.HomePageTest):

    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def setUp(self):
        mocked_models.CleanObjects().__enter__()
        super(HomePageTestFail, self).setUp()

    def tearDown(self):
        mocked_models.CleanObjects().__exit__()

    @rmotr_tester(FAIL)
    def test_home_page_renders_using_template(self):
        super(HomePageTestFail, self).test_home_page_renders_using_template()

    @rmotr_tester(FAIL)
    def test_home_page_uses_item_form(self):
        super(HomePageTestFail, self).test_home_page_uses_item_form()


class NewListTestPass(views_tests.NewListTest):

    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def setUp(self):
        mocked_models.CleanObjects().__enter__()
        super(NewListTestPass, self).setUp()

    def tearDown(self):
        mocked_models.CleanObjects().__exit__()

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
        mocked_models.CleanObjects().__enter__()
        super(NewListTestFail, self).setUp()

    def tearDown(self):
        mocked_models.CleanObjects().__exit__()

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

class ListViewTestPass(views_tests.ListViewTest):

    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def setUp(self):
        mocked_models.CleanObjects().__enter__()
        super(ListViewTestPass, self).setUp()

    def tearDown(self):
        mocked_models.CleanObjects().__exit__()

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


class ListViewTestFail(views_tests.ListViewTest):
    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def setUp(self):
        mocked_models.CleanObjects().__enter__()
        super(ListViewTestFail, self).setUp()

    def tearDown(self):
        mocked_models.CleanObjects().__exit__()

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

class ItemEndpointTestPass(views_tests.ItemEndpointTest):

    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def setUp(self):
        mocked_models.CleanObjects().__enter__()
        super(ItemEndpointTestPass, self).setUp()

    def tearDown(self):
        mocked_models.CleanObjects().__exit__()

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

class ItemEndpointTestFail(views_tests.ItemEndpointTest):

    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def setUp(self):
        mocked_models.CleanObjects().__enter__()
        super(ItemEndpointTestFail, self).setUp()

    def tearDown(self):
        mocked_models.CleanObjects().__exit__()

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