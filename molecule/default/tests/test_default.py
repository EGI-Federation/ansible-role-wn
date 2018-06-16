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


@pytest.mark.parametrize("name", [
    "c-ares",
    "cleanup-grid-accounts  ",
    "cvmfs",
    "dcache-srmclient",
    "dcap",
    "dcap-devel  ",
    "dcap-libs  ",
    "dcap-tunnel-gsi  ",
    "dcap-tunnel-krb  ",
    "dcap-tunnel-ssl  ",
    "dcap-tunnel-telnet",
    "dpm",
    "libdpm.so.1()(64bit),  dpm-libs",
    "dpm-devel",
    "dpm-perl",
    "dpm-python",
    "fetch-crl",
    "gfal2-all",
    "gfal2-python",
    "gfal2-util",
    "gfalFS",
    "gfal2-all",
    "gfal2-doc",
    "gfal2-devel",
    "ginfo",
    "lcg-info  ",
    "lcg-ManageVOTag",
    "lcg-tags",
    "lcgdm-devel",
    "globus-gass-copy-progs",
    "globus-proxy-utils",
    "glite-yaim-core",
    "gridsite-libs",
    "lcg-infosites  ",
    "lfc  ",
    "lfc-devel",
    "lfc-perl",
    "liblfc.so.1()(64bit), lfc-libs",
    "openldap-clients",
    "python-ldap  ",
    "uberftp",
    "voms-clients-java",
    "voms-devel  ",
    "xrootd-client "])
def test_dependencies(host,name):
    p=host.package(name)
    assert p.is_installed