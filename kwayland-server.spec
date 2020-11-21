%define major 5
%define libname %mklibname KWaylandServer %{major}
%define devname %mklibname -d KWaylandServer
%define plasmaver %(echo %{version} |cut -d. -f1-3)
%define stable %([ "`echo %{plasmaver} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary: 	KDE Library for integration with the Wayland display server
Name: 		kwayland-server
Version:	5.20.3
Release: 	2
Source0: 	http://download.kde.org/%{stable}/plasma/%{plasmaver}/%{name}-%{version}.tar.xz
Url: 		http://kde.org/
License: 	GPL
Group: 		System/Libraries
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(PlasmaWaylandProtocols)
BuildRequires:	cmake(Qt5Concurrent)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5WaylandClient)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(Wayland)
BuildRequires:	cmake(WaylandScanner)
BuildRequires:	cmake(KF5Wayland)
BuildRequires:	pkgconfig(wayland-protocols)
BuildRequires:	pkgconfig(wayland-client)
BuildRequires:	pkgconfig(wayland-server)
BuildRequires:	qt5-qtwayland
BuildRequires:	kernel-release-headers
BuildRequires:	wayland-tools
BuildRequires:	doxygen qt5-assistant
Requires:	%{libname} = %{EVRD}

%description
KDE Library for integration with the Wayland display server.

%package -n %{libname}
Summary:	KDE Library for working with the Wayland display server
Group:		System/Libraries
Requires:	%{name} = %{EVRD}

%description -n %{libname}
KDE Library for working with the Wayland display server

%package -n %{devname}
Summary:	Development files for KDE Wayland display server integration
Group:		Development/KDE and Qt
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
Development files for KDE Wayland display server integration

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%files
%{_datadir}/qlogging-categories5/kwaylandserver.categories

%files -n %{libname}
%{_libdir}/libKWaylandServer.so.%{major}*

%files -n %{devname}
%{_includedir}/KWaylandServer
%{_includedir}/kwaylandserver_version.h
%{_libdir}/cmake/KWaylandServer
%{_libdir}/libKWaylandServer.so
%doc %{_docdir}/qt5/KWaylandServer.*
