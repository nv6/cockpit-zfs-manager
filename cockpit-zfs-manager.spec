%define        __spec_install_post %{nil}
%define          debug_package %{nil}
%define        __os_install_post %{_dbpath}/brp-compress

Name:		cockpit-zfs-manager
Version:	0.3.3.404
Release:	1%{?dist}
Summary:	An interactive ZFS on Linux admin package for Cockpit

Group:		Development/Tools
License:	GPL
URL:		https://github.com/45Drives/tools
Source0:	%{name}-%{version}.tar.gz

BuildArch:	x86_64
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

Requires: cockpit
Requires: cockpit-ws
Requires: cockpit-bridge

%description
An interactive ZFS on Linux admin package for Cockpit

%prep
%setup -q

%build
# empty

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/cockpit/zfs/

# in builddir
cp -a zfs/ %{buildroot}/usr/share/cockpit/

%clean
rm -rf %{buildroot}

%files
%dir /usr/share/cockpit/zfs
%defattr(-,root,root,-)
/usr/share/cockpit/zfs/*

%changelog
* Mon Oct 26 2020 Brett Kelly <bkelly@45drives.com> 0.3.3.404
- First build of 0.3.3.404

