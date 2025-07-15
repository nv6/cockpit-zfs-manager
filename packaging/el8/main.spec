Name: ::package_name::
Version: ::package_version::
Release: ::package_build_version::%{?dist}
Summary: ::package_description_short::
License: ::package_licence::
URL: ::package_url::
Source0: %{name}-%{version}.tar.gz
BuildArch: ::package_architecture_el::
Requires: ::package_dependencies_el::

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
::package_title::
::package_description_long::

%prep
%setup -q

%build

%install
make DESTDIR=%{buildroot} install

%files
/usr/share/cockpit/*

%changelog
* Tue Jul 15 2025 Nivesh Varma <73319848+nv6@users.noreply.github.com> 1.3.1-2
- change build base path to include missing fonts
* Thu Nov 16 2023 Brett Kelly <bkelly@45drives.com> 1.3.1-1
- Fixed issue with duplicated modal screens when creating zfs replication tasks
* Wed Apr 26 2023 Brett Kelly <bkelly@45drives.com> 1.3.0-5
- fix broken ubuntu dependency
* Mon Apr 24 2023 Brett Kelly <bkelly@45drives.com> 1.3.0-4
- relaxed dependancy to allow zfs-kmod or zfs-dkms
* Wed Aug 11 2021 Dawson Della Valle <ddellavalle@45drives.com> 1.3.0-3
- Rebuild Packages.
* Mon Jul 05 2021 Dawson Della Valle <ddellavalle@45drives.com> 1.3.0-2
- Add EL8 Packaging.
* Thu Jul 01 2021 Dawson Della Valle <ddellavalle@45drives.com> 1.3.0-1
- Add znapzend Replication Task support at the dataset level.
- Enhance methods of managing dropdown menus.
- Add Dataset Permissions as a dropdown action.
- Change default disk selector name to prefer aliases.
