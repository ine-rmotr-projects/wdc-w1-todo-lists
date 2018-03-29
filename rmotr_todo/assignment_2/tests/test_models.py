from todo.tests import test_models as models_tests
from test_utils.decorators import rmotr_tester, PASS, FAIL
from test_utils import mocked_models
from assignment_2.fixtures import fail_models
from unittest.mock import patch


class ItemAndListModelTestPass(models_tests.ItemAndListModelTest):

    @rmotr_tester(PASS, url_override=False)
    @patch('todo.tests.test_models.List', mocked_models.List())
    @patch('todo.tests.test_models.Item', mocked_models.Item())
    def test_item_saves_to_list(self):
        mocked_models.List.clean()
        mocked_models.List.clean()
        super(ItemAndListModelTestPass, self).test_item_saves_to_list()

    @patch('todo.tests.test_models.List', mocked_models.List())
    @patch('todo.tests.test_models.Item', mocked_models.Item())
    @rmotr_tester(PASS, url_override=False)
    def test_get_absolute_url(self):
        mocked_models.List.clean()
        mocked_models.List.clean()
        super(ItemAndListModelTestPass, self).test_get_absolute_url()


class ItemAndListModelTestFail(models_tests.ItemAndListModelTest):

    @rmotr_tester(FAIL, url_override=False)
    @patch('todo.tests.test_models.List', fail_models.List)
    @patch('todo.tests.test_models.Item', fail_models.Item)
    def test_item_saves_to_list(self):
        fail_models.List.clean()
        fail_models.Item.clean()
        super(ItemAndListModelTestFail, self).test_item_saves_to_list()

    @rmotr_tester(FAIL, url_override=False)
    @patch('todo.tests.test_models.List', fail_models.List)
    @patch('todo.tests.test_models.Item', fail_models.Item)
    def test_get_absolute_url(self):
        fail_models.List.clean()
        fail_models.Item.clean()
        super(ItemAndListModelTestFail, self).test_get_absolute_url()