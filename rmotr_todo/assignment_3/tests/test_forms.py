from todo.tests import test_forms as forms_tests
from test_utils.decorators import rmotr_tester, PASS, FAIL
from test_utils import mocked_models
from unittest.mock import patch


class ItemFormTestPass(forms_tests.ItemFormTest):

    @patch('todo.tests.test_forms.Item', mocked_models.Item._get())
    @patch('todo.tests.test_forms.List', mocked_models.List._get())
    @patch('todo.tests.test_forms.ItemForm', mocked_models.ItemForm)
    def setUp(self):
        mocked_models.CleanObjects().setUp()
        super(ItemFormTestPass, self).setUp()

    @patch('todo.tests.test_forms.Item', mocked_models.Item._get())
    @patch('todo.tests.test_forms.List', mocked_models.List._get())
    @patch('todo.tests.test_forms.ItemForm', mocked_models.ItemForm)
    def tearDown(self):
        mocked_models.CleanObjects.tearDown()
        super(ItemFormTestPass, self).tearDown()

    @rmotr_tester(PASS, url_override=False)
    @patch('todo.tests.test_forms.List', mocked_models.List._get())
    @patch('todo.tests.test_forms.Item', mocked_models.Item._get())
    @patch('todo.tests.test_forms.ItemForm', mocked_models.ItemForm)
    def test_form_renders_item_text_input(self):
        super(ItemFormTestPass, self).test_form_renders_item_text_input()

    @rmotr_tester(PASS, url_override=False)
    @patch('todo.tests.test_forms.List', mocked_models.List._get())
    @patch('todo.tests.test_forms.Item', mocked_models.Item._get())
    @patch('todo.tests.test_forms.ItemForm', mocked_models.ItemForm)
    def test_form_validation_for_blank_items(self):
        super(ItemFormTestPass, self).test_form_validation_for_blank_items()

    @rmotr_tester(PASS, url_override=False)
    @patch('todo.tests.test_forms.List', mocked_models.List._get())
    @patch('todo.tests.test_forms.Item', mocked_models.Item._get())
    @patch('todo.tests.test_forms.ItemForm', mocked_models.ItemForm)
    def test_form_save_handles_saving_to_a_list(self):
        super(ItemFormTestPass, self).test_form_save_handles_saving_to_a_list()


class ItemFormTestFail(forms_tests.ItemFormTest):

    @patch('todo.tests.test_forms.Item', mocked_models.Item._get())
    @patch('todo.tests.test_forms.List', mocked_models.List._get())
    @patch('todo.tests.test_forms.ItemForm', mocked_models.ItemForm)
    def setUp(self):
        mocked_models.CleanObjects().setUp()
        super(ItemFormTestFail, self).setUp()

    @patch('todo.tests.test_forms.Item', mocked_models.Item._get())
    @patch('todo.tests.test_forms.List', mocked_models.List._get())
    @patch('todo.tests.test_forms.ItemForm', mocked_models.ItemForm)
    def tearDown(self):
        mocked_models.CleanObjects.tearDown()
        super(ItemFormTestFail, self).tearDown()

    @rmotr_tester(FAIL, url_override=False)
    @patch('todo.tests.test_forms.List', mocked_models.List._get())
    @patch('todo.tests.test_forms.Item', mocked_models.Item._get())
    @patch('todo.tests.test_forms.ItemForm', mocked_models.ItemForm)
    def test_form_renders_item_text_input(self):
        with patch('test_utils.mocked_models.TextInput.as_p') as fake_p:
            fake_p.return_value = '<input name="nope" id="no-way" placeholder="Break your test" />'
            super(ItemFormTestFail, self).test_form_renders_item_text_input()

    @rmotr_tester(FAIL, url_override=False)
    @patch('todo.tests.test_forms.List', mocked_models.List._get())
    @patch('todo.tests.test_forms.Item', mocked_models.Item._get())
    @patch('todo.tests.test_forms.ItemForm', mocked_models.ItemForm)
    def test_form_validation_for_blank_items(self):
        with patch('test_utils.mocked_models.MockForm.is_valid') as always_valid:
            always_valid.return_value = True
            super(ItemFormTestFail, self).test_form_validation_for_blank_items()

    @rmotr_tester(FAIL, url_override=False)
    @patch('todo.tests.test_forms.List', mocked_models.List._get())
    @patch('todo.tests.test_forms.Item', mocked_models.Item._get())
    @patch('todo.tests.test_forms.ItemForm', mocked_models.ItemForm)
    def test_form_save_handles_saving_to_a_list(self):
        with patch('test_utils.mocked_models.ItemForm._DEBUG_DO_NOT_SAVE_TO_LIST', True):
            super(ItemFormTestFail, self).test_form_save_handles_saving_to_a_list()