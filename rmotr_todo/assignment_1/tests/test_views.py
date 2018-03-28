from todo.tests import test_views as views_tests
from test_utils.decorators import rmotr_tester, PASS, FAIL


class HomePageTestsPass(views_tests.HomePageTest):

    @rmotr_tester(test_mode=PASS)
    def test_home_page_renders_using_template(self):
        super(HomePageTestsPass, self).test_home_page_renders_using_template()

    @rmotr_tester(test_mode=PASS)
    def test_add_item(self):
        super(HomePageTestsPass, self).test_add_item()

    @rmotr_tester(test_mode=PASS)
    def test_add_multiple_items(self):
        super(HomePageTestsPass, self).test_add_multiple_items()


class HomePageTestsFail(views_tests.HomePageTest):
    @rmotr_tester(test_mode=FAIL)
    def test_home_page_renders_using_template(self):
        super(HomePageTestsFail, self).test_home_page_renders_using_template()

    @rmotr_tester(test_mode=FAIL)
    def test_add_item(self):
        super(HomePageTestsFail, self).test_add_item()

    @rmotr_tester(test_mode=FAIL)
    def test_add_multiple_items(self):
        super(HomePageTestsFail, self).test_add_multiple_items()

