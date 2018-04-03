from todo.tests import test_views as views_tests
from test_utils.decorators import rmotr_tester, PASS, FAIL
from test_utils import mocked_models
from unittest.mock import patch, Mock
from assignment_3.fixtures.views import ItemForm


class HomePageTestPass(views_tests.HomePageTest):

    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def setUp(self):
        mocked_models.CleanObjects().setUp()
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
        """
        Test that the page is using an ItemForm
        See response.context, ie response.context['form']
        """
        super(HomePageTestPass, self).test_home_page_uses_item_form()


class HomePageTestFail(views_tests.HomePageTest):

    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def setUp(self):
        mocked_models.CleanObjects().setUp()
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
        """
        Should fail if the ItemForm is not used in the rendering of the
        page
        """
        super(HomePageTestFail, self).test_home_page_uses_item_form()


class NewListTestPass(views_tests.NewListTest):

    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def setUp(self):
        mocked_models.CleanObjects().setUp()
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
        """
        Update test so that the data field used is now 'text'
        to match our new Form
        """
        super(NewListTestPass, self).test_add_item()

    @rmotr_tester(PASS)
    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def test_redirects_after_post(self):
        """
        Also requires update to data field
        """
        super(NewListTestPass, self).test_redirects_after_post()

    @rmotr_tester(PASS)
    def test_invalid_item_renders_home(self):
        """
        Test that if we try to add an invalid item we once again
        get the home page. ie check template is using home
        """
        super(NewListTestPass, self).test_invalid_item_renders_home()

    @rmotr_tester(PASS)
    def test_invalid_item_shows_error(self):
        """
        Test that if we try to add an invalid item we also receive the
        appropriate error message
        """
        super(NewListTestPass, self).test_invalid_item_shows_error()



class NewListTestFail(views_tests.NewListTest):

    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def setUp(self):
        mocked_models.CleanObjects().setUp()
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
        """
        Should fail if home template is not rendered on invalid item
        POST
        """
        super(NewListTestFail, self).test_invalid_item_renders_home()

    @rmotr_tester(FAIL)
    def test_invalid_item_shows_error(self):
        """
        Should fail if page rendered does not include error messages
        """
        super(NewListTestFail, self).test_invalid_item_shows_error()

class ListViewTestPass(views_tests.ListViewTest):

    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def setUp(self):
        mocked_models.CleanObjects().setUp()
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
        """
        Must be updated to account for new form field name
        """
        super(ListViewTestPass, self).test_able_to_add_items_to_existing_list()

    @rmotr_tester(PASS)
    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def test_invalid_input_does_not_save_to_db(self):
        """
        Tests to ensure that invalid items are not saved to the database
        ie: after post with empty string for text the count of objects
        should not have increased
        """
        super(ListViewTestPass, self).test_invalid_input_does_not_save_to_db()

    @rmotr_tester(PASS)
    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def test_invalid_input_renders_list_template(self):
        """
        Test to ensure that if invalid item data is POSTed, we still are
        using the list template to render pages
        """
        super(ListViewTestPass, self).test_invalid_input_renders_list_template()

    @rmotr_tester(PASS)
    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def test_invalid_input_shows_error_on_page(self):
        """
        Ensure we are showing error messages on the list template on invalid
        input
        """
        super(ListViewTestPass, self).test_invalid_input_shows_error_on_page()


class ListViewTestFail(views_tests.ListViewTest):

    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def setUp(self):
        mocked_models.CleanObjects().setUp()
        super(ListViewTestFail, self).setUp()

    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def tearDown(self):
        mocked_models.CleanObjects.tearDown()
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
        """
        Should fail if invalid items are saved to the db
        """
        with patch('test_utils.mocked_models.MockForm.is_valid') as always_valid:
            always_valid.return_value = True
            super(ListViewTestFail, self).test_invalid_input_does_not_save_to_db()

    @rmotr_tester(FAIL)
    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def test_invalid_input_renders_list_template(self):
        """
        Should fail if on invalid input we render with the wrong template
        or no template
        """
        super(ListViewTestFail, self).test_invalid_input_renders_list_template()

    @rmotr_tester(FAIL)
    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def test_invalid_input_shows_error_on_page(self):
        """
        Should fail if we do not display correct error messages on invalid
        input
        """
        super(ListViewTestFail, self).test_invalid_input_shows_error_on_page()
