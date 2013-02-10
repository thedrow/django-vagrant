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
    def __init__(self, name, ip, role, domain=None):
        pass