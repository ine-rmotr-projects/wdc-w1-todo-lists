from todo.tests import test_models as models_tests
from test_utils.decorators import rmotr_tester, PASS, FAIL
from test_utils import mocked_models
from unittest.mock import patch

class ItemAndListModelTestPass(models_tests.ItemAndListModelTest):

    @patch('todo.tests.test_models.Item', mocked_models.Item._get())
    @patch('todo.tests.test_models.List', mocked_models.List._get())
    def setUp(self):
        mocked_models.CleanObjects.setUp()
        super(ItemAndListModelTestPass, self).setUp()

    @patch('todo.tests.test_models.Item', mocked_models.Item._get())
    @patch('todo.tests.test_models.List', mocked_models.List._get())
    def tearDown(self):
        mocked_models.CleanObjects.tearDown()
        super(ItemAndListModelTestPass, self).tearDown()

    @rmotr_tester(PASS, url_override=False)
    @patch('todo.tests.test_models.List', mocked_models.List._get())
    @patch('todo.tests.test_models.Item', mocked_models.Item._get())
    def test_item_saves_to_list(self):
        super(ItemAndListModelTestPass, self).test_item_saves_to_list()

    @patch('todo.tests.test_models.List', mocked_models.List._get())
    @patch('todo.tests.test_models.Item', mocked_models.Item._get())
    @rmotr_tester(PASS, url_override=False)
    def test_get_absolute_url(self):
        super(ItemAndListModelTestPass, self).test_get_absolute_url()

    @patch('todo.tests.test_models.List', mocked_models.List._get())
    @patch('todo.tests.test_models.Item', mocked_models.Item._get())
    @rmotr_tester(PASS, url_override=False)
    def test_cannot_save_empty_list_items(self):
        super(ItemAndListModelTestPass, self).test_cannot_save_empty_list_items()

    @patch('todo.tests.test_models.List', mocked_models.List._get())
    @patch('todo.tests.test_models.Item', mocked_models.Item._get())
    @rmotr_tester(PASS, url_override=False)
    def test_duplicate_items_not_allowed(self):
        super(ItemAndListModelTestPass, self).test_duplicate_items_not_allowed()

    @patch('todo.tests.test_models.List', mocked_models.List._get())
    @patch('todo.tests.test_models.Item', mocked_models.Item._get())
    @rmotr_tester(PASS, url_override=False)
    def test_able_to_save_same_item_to_different_lists(self):
        super(ItemAndListModelTestPass, self).test_able_to_save_same_item_to_different_lists()

    @patch('todo.tests.test_models.List', mocked_models.List._get())
    @patch('todo.tests.test_models.Item', mocked_models.Item._get())
    @rmotr_tester(PASS, url_override=False)
    def test_ownership(self):
        super(ItemAndListModelTestPass, self).test_ownership()


class ItemAndListModelTestFail(models_tests.ItemAndListModelTest):

    @patch('todo.tests.test_models.Item', mocked_models.Item._get())
    @patch('todo.tests.test_models.List', mocked_models.List._get())
    def setUp(self):
        mocked_models.CleanObjects.setUp()
        super(ItemAndListModelTestFail, self).setUp()

    @patch('todo.tests.test_models.Item', mocked_models.Item._get())
    @patch('todo.tests.test_models.List', mocked_models.List._get())
    def tearDown(self):
        mocked_models.CleanObjects.tearDown()
        super(ItemAndListModelTestFail, self).tearDown()

    @rmotr_tester(FAIL, url_override=False)
    @patch('todo.tests.test_models.List', mocked_models.List._get())
    @patch('todo.tests.test_models.Item', mocked_models.Item._get())
    def test_item_saves_to_list(self):
        with patch('test_utils.mocked_models.ItemObject.save') as fake_save:
            super(ItemAndListModelTestFail, self).test_item_saves_to_list()

    @rmotr_tester(FAIL, url_override=False)
    @patch('todo.tests.test_models.List', mocked_models.List._get())
    @patch('todo.tests.test_models.Item', mocked_models.Item._get())
    def test_get_absolute_url(self):
        with patch('test_utils.mocked_models.ListObject.get_absolute_url'):
            super(ItemAndListModelTestFail, self).test_get_absolute_url()

    @patch('todo.tests.test_models.List', mocked_models.List._get())
    @patch('todo.tests.test_models.Item', mocked_models.Item._get())
    @rmotr_tester(FAIL, url_override=False)
    def test_cannot_save_emptly_list_items(self):
        with patch('test_utils.mocked_models.ItemObject.full_clean'):
            super(ItemAndListModelTestFail, self).test_cannot_save_empty_list_items()
    

    @patch('todo.tests.test_models.List', mocked_models.List._get())
    @patch('todo.tests.test_models.Item', mocked_models.Item._get())
    @rmotr_tester(FAIL, url_override=False)
    def test_duplicate_items_not_allowed(self):
        with patch('test_utils.mocked_models.ItemObject.full_clean'):
            super(ItemAndListModelTestFail, self).test_duplicate_items_not_allowed()

    @patch('todo.tests.test_models.List', mocked_models.List._get())
    @patch('todo.tests.test_models.Item', mocked_models.Item._get())
    @rmotr_tester(FAIL, url_override=False, allow_validation_error=True)
    def test_able_to_save_same_item_to_different_lists(self):
        with patch('test_utils.mocked_models.ItemObject._DEBUG_NO_DUPLICATES_ACROSS_LISTS', True):
            super(ItemAndListModelTestFail, self).test_able_to_save_same_item_to_different_lists()

    @patch('todo.tests.test_models.List', mocked_models.List._get())
    @patch('todo.tests.test_models.Item', mocked_models.Item._get())
    @rmotr_tester(FAIL, url_override=False)
    def test_ownership(self):
        with patch('test_utils.mocked_models.ListObject.owned_by') as owned_by_none:
            owned_by_none.return_value = False
            super(ItemAndListModelTestFail, self).test_ownership()

