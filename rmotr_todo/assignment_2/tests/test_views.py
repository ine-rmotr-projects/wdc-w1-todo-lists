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
    @patch('todo.views.Item', mocked_models.Item)
    @patch('todo.tests.test_views.Item', mocked_models.Item)
    def test_add_item(self):
        super(NewListTestPass, self).test_add_item()
