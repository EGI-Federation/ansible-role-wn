import os
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize("name", [
    "c-ares",
    "cleanup-grid-accounts",
    "cvmfs",
    "dcache-srmclient",
    "dcap",
    "dcap-devel",
    "dcap-libs",
    "dcap-tunnel-gsi",
    "dcap-tunnel-krb",
    "dcap-tunnel-ssl",
    "dcap-tunnel-telnet",
    "dpm",
    "dpm-libs",
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
    "lcg-info",
    "lcg-ManageVOTag",
    "lcg-tags",
    "lcgdm-devel",
    "globus-gass-copy-progs",
    "globus-proxy-utils",
    "glite-yaim-core",
    "gridsite-libs",
    "lcg-infosites",
    "lfc",
    "lfc-devel",
    "lfc-perl",
    "lfc-libs",
    "openldap-clients",
    "python-ldap",
    "uberftp",
    "voms-clients-java",
    "voms-devel",
    "xrootd-client"])
def test_dependencies_centos7(host, name):
    if (host.system_info.distribution == 'redhat' and
            host.system_info.distribution.release.startswith(7)):
        p = host.package(name)
        assert p.is_installed


@pytest.mark.parametrize("name", [
  "a1_grid_env",
  "libdpm.so.1",
  "emi-version",
  "emi.amga.amga-cli",
  "emi.saga-adapter.context-cpp",
  "emi.saga-adapter.isn-cpp",
  "emi.saga-adapter.sd-cpp",
  "gfal",
  "gfal-python",
  "glite-jobid-api-c",
  "glite-lb-client",
  "glite-lb-common",
  "glite-lb-client-progs",
  "glite-lbjp-common-gss",
  "glite-lbjp-common-trio",
  "glite-service-discovery-api-c",
  "glite-wms-brokerinfo-access",
  "glite-wn-info",
  "glite-yaim-clients",
  "jclassads",
  "lcgdm-devel",
  "lcgdm-libs",
  "lcg-util",
  "liblfc.so.1",
  "lcg-util-libs",
  "lcg-util-python"
])
def test_dependencies_centos6(host, name):
    if (host.system_info.distribution == 'redhat' and
            host.system_info.distribution.release.startswith(6)):
        p = host.package(name)
        assert p.is_installed
