from todo.tests import test_models as models_tests
from test_utils.decorators import rmotr_tester, PASS, FAIL
from test_utils import mocked_models
from unittest import mock


class ItemModelTestPass(models_tests.ItemModelTest):

    @rmotr_tester(PASS)
    @mock.patch("todo.tests.test_models.Item", mocked_models.Item._get())
    def test_saving_and_retrieving_items(self):
        with mocked_models.CleanObjects():
            super(ItemModelTestPass, self).test_saving_and_retrieving_items()


class ItemModelTestFail(models_tests.ItemModelTest):

    @rmotr_tester(FAIL)
    @mock.patch("todo.tests.test_models.Item", mocked_models.Item._get())
    def test_saving_and_retrieving_items(self):
        with mocked_models.CleanObjects():
            with mock.patch('test_utils.mocked_models.MockIterator') as fake_iterator:
                fake_iterator.count.return_value = 0
                fake_iterator.__getitem__.return_value = mocked_models.ItemObject()
                super(ItemModelTestFail, self).test_saving_and_retrieving_items()
