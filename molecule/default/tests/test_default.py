import os
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'

@pytest.mark.parametrize("name,version", [
    ("epel-release","7.11"),
    ("umd-release","4.1.3"),
    ("wn","4.1.3")])
def test_packages(host, name, version):
    p = host.package(name)
    assert p.is_installed
    assert p.version.startswith(version)
