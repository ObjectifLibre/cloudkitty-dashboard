%{!?upstream_version: %global upstream_version %{version}}

Name:          openstack-cloudkitty-dashboard
Version:       XXX
Release:       XXX
Summary:       Dashboard for CloudKitty
License:       ASL 2.0
Group:         System Environment/Base
URL:           http://github.com/stackforge/cloudkitty-dashboard
Source0:       http://tarballs.openstack.org/cloudkitty-dashboard/cloudkitty-dashboard-master.tar.gz

BuildArch:     noarch

BuildRequires: git
BuildRequires: python-cloudkittyclient
BuildRequires: python-keystoneclient
BuildRequires: python-sphinx
BuildRequires: python-pbr

Requires:      openstack-dashboard
Requires:      python-cloudkittyclient

%prep
%setup -q -n cloudkitty-dashboard-%{upstream_version}

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install -O1 --skip-build --root=%{buildroot}
mkdir -p %{buildroot}/usr/share/openstack-dashboard/openstack_dashboard/enabled
( cd %{buildroot}%{python2_sitelib}/cloudkittydashboard/enabled/ ; \
  for i in _[0-9]*; do \
    ln -s %{python2_sitelib}/cloudkittydashboard/enabled/$i \
      %{buildroot}/usr/share/openstack-dashboard/openstack_dashboard/enabled/; \
  done )

%files
%license LICENSE
%{python2_sitelib}/cloudkittydashboard
%{python2_sitelib}/cloudkitty_dashboard-%{upstream_version}-py?.?.egg-info
%{_datarootdir}/openstack-dashboard/openstack_dashboard/enabled

%description
OpenStack Rating-as-a-Service - Dashboard

%changelog
