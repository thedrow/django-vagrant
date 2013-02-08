from shutil import copyfile, move
from fabric.context_managers import cd
from fabric.decorators import task
from fabric.operations import local
import tests

@task
def package():
    with cd('./box_template'):
        copyfile('Vagrantfile', 'Vagrantfile.pkg')
        local('vagrant up')
        local('vagrant package --vagrantfile Vagrantfile.pkg')
        move('./django_devenv.box', '../boxes/django_devenv.box')