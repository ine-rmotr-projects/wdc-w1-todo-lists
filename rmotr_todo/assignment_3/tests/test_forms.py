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
        """
        Test that an ItemForm correctly renders the text input
        complete with placeholder text
        See Form.as_p: https://docs.djangoproject.com/en/2.0/ref/forms/api/#as-p
        """
        super(ItemFormTestPass, self).test_form_renders_item_text_input()

    @rmotr_tester(PASS, url_override=False)
    @patch('todo.tests.test_forms.List', mocked_models.List._get())
    @patch('todo.tests.test_forms.Item', mocked_models.Item._get())
    @patch('todo.tests.test_forms.ItemForm', mocked_models.ItemForm)
    def test_form_validation_for_blank_items(self):
        """
        Ensure that a form passed an empty string for its text data
        comes back invalid and with the correct error message.
        See Form.is_valid: https://docs.djangoproject.com/en/2.0/ref/forms/api/#django.forms.Form.is_valid
        Also see Form.errors: https://docs.djangoproject.com/en/2.0/ref/forms/api/#django.forms.Form.errors
        """
        super(ItemFormTestPass, self).test_form_validation_for_blank_items()

    @rmotr_tester(PASS, url_override=False)
    @patch('todo.tests.test_forms.List', mocked_models.List._get())
    @patch('todo.tests.test_forms.Item', mocked_models.Item._get())
    @patch('todo.tests.test_forms.ItemForm', mocked_models.ItemForm)
    def test_form_save_handles_saving_to_a_list(self):
        """
        Check that when a form is passed an item and then has its
        `save` called with the list parameter filled
        ie `form.save(list_=a_list)` that the item is saved properly
        """
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
        """
        Should fail if the input is not supplied and does not have
        the correct placeholder
        """
        with patch('test_utils.mocked_models.TextInput.as_p') as fake_p:
            fake_p.return_value = '<input name="nope" id="no-way" placeholder="Break your test" />'
            super(ItemFormTestFail, self).test_form_renders_item_text_input()

    @rmotr_tester(FAIL, url_override=False)
    @patch('todo.tests.test_forms.List', mocked_models.List._get())
    @patch('todo.tests.test_forms.Item', mocked_models.Item._get())
    @patch('todo.tests.test_forms.ItemForm', mocked_models.ItemForm)
    def test_form_validation_for_blank_items(self):
        """
        Should fail if the form fails to throw validation errors
        """
        with patch('test_utils.mocked_models.MockForm.is_valid') as always_valid:
            always_valid.return_value = True
            super(ItemFormTestFail, self).test_form_validation_for_blank_items()

    @rmotr_tester(FAIL, url_override=False)
    @patch('todo.tests.test_forms.List', mocked_models.List._get())
    @patch('todo.tests.test_forms.Item', mocked_models.Item._get())
    @patch('todo.tests.test_forms.ItemForm', mocked_models.ItemForm)
    def test_form_save_handles_saving_to_a_list(self):
        """
        Should fail if the item does not correctly save to a list
        """
        with patch('test_utils.mocked_models.ItemForm._DEBUG_DO_NOT_SAVE_TO_LIST', True):
            super(ItemFormTestFail, self).test_form_save_handles_saving_to_a_list()