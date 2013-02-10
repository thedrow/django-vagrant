from django.test import TestCase
from factory import Factory, use_strategy, BUILD_STRATEGY
from mock import patch
from vagrant.config import Role


@use_strategy(BUILD_STRATEGY)
class RoleFactory(Factory):
    FACTORY_FOR = Role

    name = 'test'
    box_path = './boxes/box.box'


class RoleTestCase(TestCase):
    TEST_APPS = ['vagrant']

    SUTFactory = RoleFactory


class RoleInitializationFailureTests(RoleTestCase):
    def test_that_when_providing_a_path_to_a_box_that_does_not_exist_a_value_error_is_raised(self):
        with patch('os.path.isfile', return_value=False):
            with self.assertRaisesRegexp(ValueError, r'Path to box file does not exist'):
                self.SUTFactory()

    def test_that_when_providing_a_path_to_a_file_that_does_not_have_the_box_file_extension_a_value_error_is_raised(
            self):
        with patch('os.path.isfile', return_value=True), patch('os.path.splitext',
                                                               return_value=('./boxes/box', '.ext')):
            with self.assertRaisesRegexp(ValueError, r"Invalid filename. Filename extension must be '.box'."):
                self.SUTFactory(box_path='./boxes/box.ext')


class RoleInitializationSuccessTests(RoleTestCase):
    def test_that_when_providing_a_role_name_it_is_assigned_to_the_name_attribute(self):
        with patch('os.path.isfile', return_value=True), patch('os.path.splitext',
                                                               return_value=('./boxes/box', '.box')):
            sut = self.SUTFactory()

            try:
                self.assertEqual(sut.name, 'test')
            except AttributeError, e:
                if e.message == "'Role' object has no attribute 'name'":  # Expected failure.
                    raise AssertionError(e.message)
                else:
                    raise

    def test_that_when_providing_a_box_path_it_is_assigned_to_the_name_attribute(self):
        with patch('os.path.isfile', return_value=True), patch('os.path.splitext',
                                                               return_value=('./boxes/box', '.box')):
            sut = self.SUTFactory()

            try:
                self.assertEqual(sut.box_path, './boxes/box.box')
            except AttributeError, e:
                if e.message == "'Role' object has no attribute 'box_path'":  # Expected failure.
                    raise AssertionError(e.message)
                else:
                    raise
