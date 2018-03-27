from django.test import modify_settings, override_settings

PASS = True
FAIL = False


class rmotr_tester(object):
    def __init__(self, test_mode):
        self.test_mode = test_mode

    def __call__(self, fn):
        self.fn = fn

        @override_settings(ROOT_URLCONF=self.root_urlconf())
        @modify_settings(INSTALLED_APPS=self.installed_apps())
        def wrapper(*args, **kwargs):

            if self.test_mode is PASS:
                return self.fn(*args, **kwargs)
            test_failed_to_fail = False
            try:
                self.fn(*args, **kwargs)
                test_failed_to_fail = True
            except AssertionError:
                pass
            if test_failed_to_fail:
                err = 'Test {} failed to fail.'
                raise AssertionError(err.format(self.fn.__name__))

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
