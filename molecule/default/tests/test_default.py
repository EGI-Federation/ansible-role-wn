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


# Test CEntOS7 releases
@pytest.mark.parametrize("name,version", [
    ("epel-release","7.11"),
    ("umd-release","4.1.3"),
    ("wn","4.1.3")])
def test_packages(host, name, version):
    if host.system_info.distribution == 'redhat' and host.system_info.distribution.release.startswith(7):
        p = host.package(name)
        assert p.is_installed
        assert p.version.startswith(version)

# Test CEntOS6 releases
@pytest.mark.parametrize("name,version", [
    ("epel-release","6.8"),
    ("umd-release","4.1.3"),
    ("emi-wn","3.1.0")])
def test_packages(host, name, version):
    if host.system_info.distribution == 'redhat' and host.system_info.distribution.release.startswith(6):
        p = host.package(name)
        assert p.is_installed
        assert p.version.startswith(version)
