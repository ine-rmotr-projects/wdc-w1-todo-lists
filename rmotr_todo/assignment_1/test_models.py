from todo.tests import test_models as models_tests
from test_utils.decorators import rmotr_tester, PASS, FAIL


class ItemModelTestPass(models_tests.ItemModelTest):

    @rmotr_tester(PASS)
    def test_saving_and_retrieving_items(self):
        super(ItemModelTestPass, self).test_saving_and_retrieving_items()


class ItemModelTestFail(models_tests.ItemModelTest):

    @rmotr_tester(FAIL)
    def test_saving_and_retrieving_items(self):
        super(ItemModelTestFail, self).test_saving_and_retrieving_items()
