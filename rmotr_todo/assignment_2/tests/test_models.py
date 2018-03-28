from todo.tests import test_models as models_tests
from test_utils.decorators import rmotr_tester, PASS, FAIL


class ItemAndListModelTestPass(TestCase):

    @rmotr_tester(PASS)
    def test_item_saves_to_list(self):
        super(ItemAndListModelTestPass, self).test_item_saves_to_list()

    @rmotr_tester(PASS)
    def test_item_saves_to_list(self):
        super(ItemAndListModelTestPass, self)