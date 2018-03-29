from todo.tests import test_models as models_tests
from test_utils.decorators import rmotr_tester, PASS, FAIL
from test_utils.mocked_models import Item, List
from assignment_2.fixtures import fail_models
from unittest.mock import patch


class ItemAndListModelTestPass(models_tests.ItemAndListModelTest):

    @rmotr_tester(PASS, url_override=False)
    @patch('todo.tests.test_models.List', List)
    @patch('todo.tests.test_models.Item', Item)
    def test_item_saves_to_list(self):
        super(ItemAndListModelTestPass, self).test_item_saves_to_list()

    @patch('todo.tests.test_models.List', List)
    @patch('todo.tests.test_models.Item', Item)
    @rmotr_tester(PASS, url_override=False)
    def test_get_absolute_url(self):
        super(ItemAndListModelTestPass, self).test_get_absolute_url()


class ItemAndListModelTestFail(models_tests.ItemAndListModelTest):

    @rmotr_tester(FAIL, url_override=False)
    @patch('todo.tests.test_models.List', fail_models.List)
    @patch('todo.tests.test_models.Item', fail_models.Item)
    def test_item_saves_to_list(self):
        super(ItemAndListModelTestFail, self).test_item_saves_to_list()

    @rmotr_tester(FAIL, url_override=False)
    @patch('todo.tests.test_models.List', fail_models.List)
    @patch('todo.tests.test_models.Item', fail_models.Item)
    def test_get_absolute_url(self):
        super(ItemAndListModelTestFail, self).test_get_absolute_url()