from todo.tests import test_views as views_tests
from test_utils.decorators import rmotr_tester, PASS, FAIL
from test_utils import mocked_models
from unittest.mock import patch


class HomePageTestPass(views_tests.HomePageTest):

    @rmotr_tester(PASS)
    def test_home_page_renders_using_template(self):
        super(HomePageTestPass, self).test_home_page_renders_using_template()


class HomePageTestFail(views_tests.HomePageTest):

    @rmotr_tester(FAIL)
    def test_home_page_renders_using_template(self):
        super(HomePageTestFail, self).test_home_page_renders_using_template()


class NewListTestPass(views_tests.NewListTest):

    @rmotr_tester(PASS)
    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def test_add_item(self):
        with mocked_models.CleanObjects():
            super(NewListTestPass, self).test_add_item()

    @rmotr_tester(PASS)
    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def test_redirects_after_post(self):
        with mocked_models.CleanObjects():
            super(NewListTestPass, self).test_redirects_after_post()

class NewListTestFail(views_tests.NewListTest):

    @rmotr_tester(FAIL)
    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def test_add_item(self):
        with mocked_models.CleanObjects():
            super(NewListTestFail, self).test_add_item()

    @rmotr_tester(FAIL)
    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def test_redirects_after_post(self):
        with mocked_models.CleanObjects():
            super(NewListTestFail, self).test_redirects_after_post()

class ListViewTestPass(views_tests.ListViewTest):

    @rmotr_tester(PASS)
    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def test_uses_list_template(self):
        with mocked_models.CleanObjects():
            super(ListViewTestPass, self).test_uses_list_template()

    @rmotr_tester(PASS)
    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def test_only_shows_correct_items(self):
        with mocked_models.CleanObjects():
            super(ListViewTestPass, self).test_only_shows_correct_items()

    @rmotr_tester(PASS)
    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def test_passes_correct_list_to_template(self):
        with mocked_models.CleanObjects():
            super(ListViewTestPass, self).test_passes_correct_list_to_template()

    @rmotr_tester(PASS)
    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def test_able_to_add_items_to_existing_list(self):
        with mocked_models.CleanObjects():
            super(ListViewTestPass, self).test_able_to_add_items_to_existing_list()


class ListViewTestFail(views_tests.ListViewTest):

    @rmotr_tester(FAIL)
    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def test_uses_list_template(self):
        with mocked_models.CleanObjects():
            super(ListViewTestFail, self).test_uses_list_template()

    @rmotr_tester(FAIL)
    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def test_only_shows_correct_items(self):
        with mocked_models.CleanObjects():
            super(ListViewTestFail, self).test_only_shows_correct_items()

    @rmotr_tester(FAIL)
    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def test_passes_correct_list_to_template(self):
        with mocked_models.CleanObjects():
            super(ListViewTestFail, self).test_passes_correct_list_to_template()

    @rmotr_tester(FAIL)
    @patch('todo.tests.test_views.Item', mocked_models.Item._get())
    @patch('todo.tests.test_views.List', mocked_models.List._get())
    def test_able_to_add_items_to_existing_list(self):
        with mocked_models.CleanObjects():
            super(ListViewTestFail, self).test_able_to_add_items_to_existing_list()
