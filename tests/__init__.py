from fabric.decorators import task
import sys

def configure_settings():
    from django.conf import settings

    if not settings.configured:
        settings.configure(TEST_RUNNER='discoverage.runner.DiscoverageRunner', INSTALLED_APPS=(
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.sites',
            'django.contrib.messages',
            'discoverage',
            ),
            DATABASES={
                'default': {
                    'ENGINE': 'django.db.backends.sqlite3',
                    'NAME': '.',
                    'USER': '',
                    'PASSWORD': '',
                    'HOST': '',
                    'PORT': '',
                }
            })


def run_tests(verbosity=1):
    configure_settings()
    from django.conf import settings
    from django.test.utils import get_runner
    from django.test.utils import setup_test_environment

    setup_test_environment()
    TestRunner = get_runner(settings)
    test_runner = TestRunner(verbosity=verbosity)
    failures = test_runner.run_tests(('unit', 'functional', 'integration'))

    if failures:
        sys.exit(failures)


@task
def run(verbosity=1):
    run_tests(verbosity)

if __name__ == '__main__':
    run_tests()