PASS = True
FAIL = False


class rmotr_tester(object):
    def __init__(self, test_mode):
        self.test_mode = test_mode

    def __call__(self, fn):
        self.fn = fn

        def wrapper(*args, **kwargs):
            fn_self = args[0]
            with fn_self.modify_settings(INTSTALLED_APPS=self.installed_apps()):
                with fn_self.settings(ROOT_URLCONF=self.root_urlconf()):
                    if self.test_mode is PASS:
                        return self.fn(*args, **kwargs)
                    test_failed_to_fail = False
                    try:
                        result = self.fn(*args, **kwargs)
                        test_failed_to_fail = True
                    except AssertionError:
                        pass
                    if test_failed_to_fail:
                        raise AssertionError('Test {} failed to fail.'.format(self.fn.__name__))


        return wrapper

    def get_assignment_module(self):
        return self.fn.__module__.split('.')[0]

    def installed_apps(self):
        return {'append': self.get_assignment_module() + '.fixtures'}

    def root_urlconf(self):
        module = (self.get_assignment_module() +
                  '.fixtures.url_overrides.' +
                  self.fn.__name__ + '_')
        module += 'pass' if self.test_mode == PASS else 'fail'
        return module


'''
@override_settings(ROOT_URLCONF='assignment_1.fixtures.url_overrides.test_home_page_renders_using_template_pass')
'''
