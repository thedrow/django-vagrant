from django.test import TestCase
from factory import Factory, use_strategy, BUILD_STRATEGY, SubFactory
from mock import patch
from tests.unit.config.test_role import RoleFactory
from vagrant.config import Node


@use_strategy(BUILD_STRATEGY)
class NodeFactory(Factory):
    FACTORY_FOR = Node

    name = 'test'
    ip = '172.16.32.10'
    role = SubFactory(RoleFactory)
    domain = 'domain.com'


class NodeTestCase(TestCase):
    TEST_APPS = ['vagrant']

    SUTFactory = NodeFactory


class NodeInitializationFailureTests(NodeTestCase):
    """
    Failure tests are for the ip attribute are not implemented because the ipaddress module is only available
    on python 3.4 and therefore the ip attribute cannot be validated without portability issues
    between the ipaddr and ipaddress libraries.
    """

    def test_that_when_providing_an_object_which_is_not_a_role_a_type_error_is_raised(self):
        with patch('os.path.isfile', return_value=True), patch('os.path.splitext',
                                                               return_value=('./boxes/box', '.box')):
            with self.assertRaisesRegexp(TypeError, r'role must be a Role object.'):
                self.SUTFactory(role=object())


class NodeInitializationSuccessTests(NodeTestCase):
    def test_that_when_providing_a_node_name_without_a_domain_it_is_assigned_to_the_hostname_attribute(self):
        with patch('os.path.isfile', return_value=True), patch('os.path.splitext',
                                                               return_value=('./boxes/box', '.box')):
            sut = self.SUTFactory(domain=None)

            try:
                self.assertEqual(sut.hostname, 'test')
            except AttributeError, e:
                if e.message == "'Node' object has no attribute 'hostname'":  # Expected failure.
                    raise AssertionError(e.message)
                else:
                    raise

    def test_that_when_providing_a_node_name_with_a_domain_the_node_name_and_domain_are_concated_to_the_hostname_attribute(
            self):
        with patch('os.path.isfile', return_value=True), patch('os.path.splitext',
                                                               return_value=('./boxes/box', '.box')):
            sut = self.SUTFactory()

            try:
                self.assertEqual(sut.hostname, 'test.domain.com')
            except AttributeError, e:
                if e.message == "'Node' object has no attribute 'hostname'":  # Expected failure.
                    raise AssertionError(e.message)
                else:
                    raise

    def test_that_when_providing_the_node_ip_address_it_is_assigned_to_the_ip_attribute(self):
        with patch('os.path.isfile', return_value=True), patch('os.path.splitext',
                                                               return_value=('./boxes/box', '.box')):
            sut = self.SUTFactory()

            try:
                self.assertEqual(sut.ip, '172.16.32.10')
            except AttributeError, e:
                if e.message == "'Node' object has no attribute 'ip'":  # Expected failure.
                    raise AssertionError(e.message)
                else:
                    raise

    def test_that_when_providing_a_role_it_is_assigned_to_the_role_attribute(self):
        with patch('os.path.isfile', return_value=True), patch('os.path.splitext',
                                                               return_value=('./boxes/box', '.box')):
            expected = RoleFactory()

            sut = self.SUTFactory(role=expected)

            try:
                self.assertEqual(sut.role, expected)
            except AttributeError, e:
                if e.message == "'Node' object has no attribute 'role'":  # Expected failure.
                    raise AssertionError(e.message)
                else:
                    raise