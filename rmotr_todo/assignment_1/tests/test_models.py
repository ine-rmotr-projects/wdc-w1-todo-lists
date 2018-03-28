from todo.tests import test_models as models_tests
from test_utils.decorators import rmotr_tester, PASS, FAIL
from assignment_1.fixtures.models_fail import Item
from unittest import mock


class ItemModelTestPass(models_tests.ItemModelTest):

    @rmotr_tester(PASS)
    def test_saving_and_retrieving_items(self):
        super(ItemModelTestPass, self).test_saving_and_retrieving_items()


class ItemModelTestFail(models_tests.ItemModelTest):

    @rmotr_tester(FAIL)
    @mock.patch("todo.tests.test_models.Item", Item)
    def test_saving_and_retrieving_items(self):
        super(ItemModelTestFail, self).test_saving_and_retrieving_items()
