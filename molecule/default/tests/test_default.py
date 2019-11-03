import os
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_hosts_file(host):
    """This is the default test included by Molecule.

    It checks for /etc/hosts and that it is owned by root:root
    """
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


@pytest.mark.parametrize('pkg', [
  'apache2',
  'php',
  'libapache2-mod-php',
  'mysql-server',
  'php-mysql'
])
def test_pkg(host, pkg):
    package = host.package(pkg)

    assert package.is_installed
