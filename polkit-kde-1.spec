%define		qtver	4.6.3

Summary:	Polkit-kde-1 wrapper library around polkit-gobject and polkit-agent
Name:		polkit-kde-1
Version:	0.99.0
Release:	2
License:	GPL v2+
Group:		Libraries
Source0:	ftp://ftp.kde.org/pub/kde/stable/apps/KDE4.x/admin/polkit-kde-agent-1-%{version}.tar.bz2
# Source0-md5:	a02d3fddc6270a88bceaf3ba604c92f8
URL:		http://www.kde.org/
Patch0:		%{name}-gcc4.5.patch
BuildRequires:	QtCore-devel >= %{qtver}
BuildRequires:	QtDBus-devel >= %{qtver}
BuildRequires:	QtGui-devel >= %{qtver}
BuildRequires:	QtTest-devel >= %{qtver}
BuildRequires:	QtXml-devel >= %{qtver}
BuildRequires:	automoc4
BuildRequires:	cmake
BuildRequires:	polkit-qt-1-gui-devel >= 0.99.0
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.600
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Polkit-kde-1 is a polkit-1 authentication agent.

%prep
%setup -q -n polkit-kde-agent-1-%{version}

%build
install -d build
cd build
%cmake \
	-LCMS_DIR=%{_libdir} \
	../
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir}

# unsupported
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/locale/sr@ijekavian
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/locale/sr@ijekavianlatin

%find_lang polkit-kde-1 --with-kde --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/libexec/polkit-kde-authentication-agent-1
%dir %{_datadir}/apps/policykit1-kde
%{_datadir}/apps/policykit1-kde/policykit1-kde.notifyrc
%{_datadir}/autostart/polkit-kde-authentication-agent-1.desktop
