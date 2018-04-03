from todo.tests import test_views as views_tests
from test_utils.decorators import rmotr_tester, PASS, FAIL
from test_utils import mocked_models
from unittest.mock import patch


class HomePageTestsPass(views_tests.HomePageTest):

    def setUp(self):
        mocked_models.CleanObjects().setUp()
        super(HomePageTestsPass, self).setUp()

    def tearDown(self):
        mocked_models.CleanObjects.tearDown()
        super(HomePageTestsPass, self).tearDown()

    @rmotr_tester(test_mode=PASS)
    def test_home_page_renders_using_template(self):
        """
        Checks to ensure the page for '/' renders the appropriate template
        See https://docs.djangoproject.com/en/2.0/topics/testing/tools/#django.test.SimpleTestCase.assertTemplateUsed
        """
        super(HomePageTestsPass, self).test_home_page_renders_using_template()

    @rmotr_tester(test_mode=PASS)
    def test_add_item(self):
        """
        Test that when an item is POSTed to '/' it is added to the todo list
        todo item text should be in a field called 'item_text'
        """
        super(HomePageTestsPass, self).test_add_item()

    @rmotr_tester(test_mode=PASS)
    def test_add_multiple_items(self):
        """
        Continuing on previous test, if a second POST is made containing
        a second item, both items will be displayed on the list
        """
        super(HomePageTestsPass, self).test_add_multiple_items()


class HomePageTestsFail(views_tests.HomePageTest):

    def setUp(self):
        mocked_models.CleanObjects().setUp()
        super(HomePageTestsFail, self).setUp()

    def tearDown(self):
        mocked_models.CleanObjects.tearDown()
        super(HomePageTestsFail, self).tearDown()

    @rmotr_tester(test_mode=FAIL)
    def test_home_page_renders_using_template(self):
        """
        This test should fail if the home page is either using an
        incorrect template or no template.
        """
        super(HomePageTestsFail, self).test_home_page_renders_using_template()

    @rmotr_tester(test_mode=FAIL)
    def test_add_item(self):
        """
        This test should fail if POSTed items are not displayed on the page
        """
        super(HomePageTestsFail, self).test_add_item()

    @rmotr_tester(test_mode=FAIL)
    def test_add_multiple_items(self):
        """
        This test should fail if either no items are displayed, or just a
        single item is.
        """
        super(HomePageTestsFail, self).test_add_multiple_items()

