from todo.tests import test_models as models_tests
from test_utils.decorators import rmotr_tester, PASS, FAIL
from test_utils import mocked_models
from unittest.mock import patch

class ItemAndListModelTestPass(models_tests.ItemAndListModelTest):

    @patch('todo.tests.test_models.Item', mocked_models.Item._get())
    @patch('todo.tests.test_models.List', mocked_models.List._get())
    def setUp(self):
        mocked_models.CleanObjects().setUp()
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
        """
        Replaces the previous item save method
        Now checks to see if saved item is contained in the parent
        List Model object
        """
        super(ItemAndListModelTestPass, self).test_item_saves_to_list()

    @patch('todo.tests.test_models.List', mocked_models.List._get())
    @patch('todo.tests.test_models.Item', mocked_models.Item._get())
    @rmotr_tester(PASS, url_override=False)
    def test_get_absolute_url(self):
        """
        Tests that List Model objects have a `test_get_absolute_url`
        method that returns the url '/lists/<list object id/'
        """
        super(ItemAndListModelTestPass, self).test_get_absolute_url()


class ItemAndListModelTestFail(models_tests.ItemAndListModelTest):

    @patch('todo.tests.test_models.Item', mocked_models.Item._get())
    @patch('todo.tests.test_models.List', mocked_models.List._get())
    def setUp(self):
        mocked_models.CleanObjects().setUp()
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
        """
        Should fail if Item fails to save to List
        """
        with patch('test_utils.mocked_models.ItemObject.save') as fake_save:
            super(ItemAndListModelTestFail, self).test_item_saves_to_list()

    @rmotr_tester(FAIL, url_override=False)
    @patch('todo.tests.test_models.List', mocked_models.List._get())
    @patch('todo.tests.test_models.Item', mocked_models.Item._get())
    def test_get_absolute_url(self):
        """
        Should fail if List's `get_absolute_url` method does not
        return the appropriate url
        """
        with patch('test_utils.mocked_models.ListObject.get_absolute_url'):
            super(ItemAndListModelTestFail, self).test_get_absolute_url()