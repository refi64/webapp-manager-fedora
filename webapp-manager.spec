Name:    webapp-manager
Version: 1.1.1
Release: 1%{?dist}
Summary: Web Application Manager
License: GPLv3+
URL:     https://github.com/linuxmint/webapp-manager/
Source0: https://github.com/linuxmint/webapp-manager/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch: noarch

Requires: python3-beautifulsoup4
Requires: python3-configobj
Requires: python3-gobject
Requires: python3-pillow
Requires: python3-setproctitle
Requires: python3-tldextract
Requires: xapps

BuildRequires: gettext
BuildRequires: python3-devel

%{?python_disable_dependency_generator}

%description
Launch websites as if they were apps.

%prep
%autosetup -p1
sed -i 's,/usr/lib/,${libdir}/,' usr/bin/webapp-manager

%build
%make_build
libdir="%{_libdir}" envsubst '$libdir' <usr/bin/webapp-manager > webapp-manager
%py_byte_compile %{python3} usr/lib/webapp-manager/*.py

%install
install -Dm 755 webapp-manager -t %{buildroot}/%{_bindir}
cp -r etc %{buildroot}/%{_sysconfdir}
cp -r usr/lib %{buildroot}/%{_libdir}
cp -r usr/share %{buildroot}/%{_datadir}
rm -rf %{buildroot}/%{_datadir}/applications/kde4

%files
%{_bindir}/webapp-manager
%{_libdir}/webapp-manager
%{_datadir}/applications/webapp-manager.desktop
%{_datadir}/desktop-directories/webapps-webapps.directory
%{_datadir}/glib-2.0/schemas/org.x.webapp-manager.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/webapp-manager.svg
%{_datadir}/icons/hicolor/scalable/categories/applications-webapps.svg
%{_datadir}/locale/
%{_datadir}/webapp-manager/
%{_sysconfdir}/xdg/menus/applications-merged/webapps.menu
