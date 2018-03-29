from todo.tests import test_models as models_tests
from test_utils.decorators import rmotr_tester, PASS, FAIL
from test_utils import mocked_models
from unittest import mock

class ItemAndListModelTestPass(models_tests.ItemAndListModelTest):

    @rmotr_tester(PASS, url_override=False)
    @mock.patch('todo.tests.test_models.List', mocked_models.List._get())
    @mock.patch('todo.tests.test_models.Item', mocked_models.Item._get())
    def test_item_saves_to_list(self):
        with mocked_models.CleanObjects():
            super(ItemAndListModelTestPass, self).test_item_saves_to_list()

    @mock.patch('todo.tests.test_models.List', mocked_models.List._get())
    @mock.patch('todo.tests.test_models.Item', mocked_models.Item._get())
    @rmotr_tester(PASS, url_override=False)
    def test_get_absolute_url(self):
        with mocked_models.CleanObjects():
            super(ItemAndListModelTestPass, self).test_get_absolute_url()


class ItemAndListModelTestFail(models_tests.ItemAndListModelTest):

    @rmotr_tester(FAIL, url_override=False)
    @mock.patch('todo.tests.test_models.List', mocked_models.List._get())
    @mock.patch('todo.tests.test_models.Item', mocked_models.Item._get())
    def test_item_saves_to_list(self):
        with mocked_models.CleanObjects():
            with mock.patch('test_utils.mocked_models.ItemObject.save') as fake_save:
                super(ItemAndListModelTestFail, self).test_item_saves_to_list()

    @rmotr_tester(FAIL, url_override=False)
    @mock.patch('todo.tests.test_models.List', mocked_models.List._get())
    @mock.patch('todo.tests.test_models.Item', mocked_models.Item._get())
    def test_get_absolute_url(self):
        with mocked_models.CleanObjects():
            with mock.patch('test_utils.mocked_models.ListObject.get_absolute_url'):
                super(ItemAndListModelTestFail, self).test_get_absolute_url()