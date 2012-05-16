Summary:	This program adds tabs to Skype(tm) for Linux
Summary(en.UTF-8):	This program adds tabs to Skype™ for Linux
Name:		skypetab-ng
Version:	0.4.9
Release:	23
License:	LGPL
Group:		Applications/Networking
Source0:	%{name}.tar.gz
# Source0-md5:	0cd286b31278d5951a834d93579b5b2e
URL:		http://keks-n.net/skypetab
BuildRequires:	QtCore-devel
BuildRequires:	QtGui-devel
BuildRequires:	libstdc++-devel
BuildRequires:	xorg-lib-libX11-devel
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program adds tabs to Skype(tm) for Linux.

%description -l en.UTF-8
This program adds tabs to Skype™ for Linux.

%prep
%setup -q

%build
qmake-qt4
%{__make} \
	CC="%{__cc}" \
	CXX="%{__cxx}" \
	SUBLIBS="-lX11 -ldl" \
	LFLAGS="-shared -Wl,-soname,libskypetab-ng.so"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

# just use plain .so, no versions
mv -f $RPM_BUILD_ROOT%{_libdir}/libskypetab-ng.so{.%{version},}
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libskypetab-ng.so.*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/skypetab-ng
%attr(755,root,root) %{_libdir}/libskypetab-ng.so
%{_desktopdir}/skypetab-ng.desktop
