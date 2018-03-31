from django.test import modify_settings, override_settings
from django.core.exceptions import ValidationError

PASS = True
FAIL = False


class rmotr_tester(object):
    def __init__(self, test_mode,
                 url_override=True,
                 allow_validation_error=False):
        self.test_mode = test_mode
        self.url_override = url_override
        self.allow_validation_error = allow_validation_error

    def __call__(self, fn):
        self.fn = fn

        if self.url_override:
            return self.override_urls()

        return self.no_overrides()

    def override_urls(self):
        """ Overrides django's urls to our own test-specific paths """
        @override_settings(ROOT_URLCONF=self.root_urlconf())
        @modify_settings(INSTALLED_APPS=self.installed_apps())
        def wrapper(*args, **kwargs):
            self.run_test(*args, **kwargs)

        return wrapper

    def no_overrides(self):
        @modify_settings(INSTALLED_APPS=self.installed_apps())
        def wrapper(*args, **kwargs):
            self.run_test(*args, **kwargs)

        return wrapper

    def run_test(self, *args, **kwargs):
        if self.test_mode is PASS:
            return self.fn(*args, **kwargs)
        test_failed_to_fail = False
        try:
            self.fn(*args, **kwargs)
            test_failed_to_fail = True
        except AssertionError:
            pass
        except ValidationError as err:
            if self.allow_validation_error:
                pass
            else:
                raise err
        if test_failed_to_fail:
            err = 'Test {} failed to fail.'
            raise AssertionError(err.format(self.fn.__name__))

    def get_assignment_module(self):
        return self.fn.__module__.split('.')[0]

    def installed_apps(self):
        """ adds assignment fixtures directory to django installed apps """
        return {'append': self.get_assignment_module() + '.fixtures'}

    def root_urlconf(self):
        """ Generate location for custom url config """
        module = (self.get_assignment_module() +
                  '.fixtures.url_overrides.')
        if self.test_mode is PASS:
            try:
                mod = module + self.fn.__name__ + '_pass'
                __import__(mod)
                module = mod
            except ImportError:
                module += 'pass'
        if self.test_mode is FAIL:
            module += self.fn.__name__

        return module
