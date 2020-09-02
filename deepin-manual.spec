%bcond_with check
%global debug_package   %{nil}
%global _unpackaged_files_terminate_build 0  
Name:          deepin-manual
Version:       5.6.7
Release:       5
Summary:       Manual is designed to help users learn the operating system and its applications, providing specific instructions and function descriptions.
License:       GPLv3
URL:           https://uos-packages.deepin.com/uos/pool/main/d/deepin-manual/
Source0:       %{name}-%{version}.tar.gz

BuildRequires: cmake
BuildRequires: dtkcore-devel
BuildRequires: dtkwidget-devel
BuildRequires: dtkgui-devel
BuildRequires: qt5-qtx11extras-devel
BuildRequires: qt5-linguist
BuildRequires: qt5-qtwebchannel
BuildRequires: qt5-qtwebchannel-devel
BuildRequires: qt5-qtwebengine-devel
BuildRequires: qt5-qtwebengine
Requires: qt5-qtwebengine

%description
Manual is designed to help users learn the operating system and its applications, providing specific instructions and function descriptions.


%prep
%setup

%build
export PATH=$PATH:/usr/lib64/qt5/bin
%cmake
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

%files
/usr/bin/dman
/usr/bin/dman-search
/usr/share/applications/deepin-manual.desktop
/usr/share/dbus-1/services/com.deepin.Manual.Open.service
/usr/share/dbus-1/services/com.deepin.Manual.Search.service
/usr/share/deepin-manual/dman
/usr/share/deepin-manual/web_dist/index.css
/usr/share/deepin-manual/web_dist/index.html
/usr/share/deepin-manual/web_dist/index.js
/usr/share/deepin-manual/web_dist/qwebchannel.js
/usr/share/icons/hicolor/scalable/apps/deepin-manual.svg
%exclude /usr/share/deepin-manual/manual-assets/professional/*
/usr/share/deepin-manual/translations/*
/usr/share/deepin-manual/manual-assets/server/*
%license LICENSE
%doc README.md


%changelog
* Wed Sep 2 2020 chenbo pan <panchenbo@uniontech.com> - 5.6.7-5
- fix compile fail 

* Fri Aug 28 2020 chenbo pan <panchenbo@uniontech.com> - 5.6.7-4
- fix compile fail

* Thu Jul 30 2020 openEuler Buildteam <buildteam@openeuler.org> - 5.6.7-3
- Package init
