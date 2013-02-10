import os


class Role(object):
    def __init__(self, name, box_path):
        if not os.path.isfile(box_path):
            raise ValueError('Path to box file does not exist.')

        if os.path.splitext(box_path)[1] != '.box':
            raise ValueError("Invalid filename. Filename extension must be '.box'.")

        self.name = name
        self.box_path = box_path


class Node(object):
    def __init__(self, ip, role, domain='', name=''):
        if not isinstance(role, Role):
            raise TypeError('role must be a Role object.')

        self.ip = ip
        self.role = role

        if name == '':
            name = role.name

        self.hostname = name + ('.' + domain if domain else '')