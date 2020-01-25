#
# TODO:
#  locale, icon, desktop file
#
Summary:	Extensible image recognition systems modelling program
Summary(pl.UTF-8):	Rozszerzalny program modelujący systemy rozpoznawania obrazów
Name:		FaRetSys
Version:	0.4.2
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://team.pld-linux.org/~wolf/eithne/res/eithne-%{version}.tar.bz2
# Source0-md5:	7f06fbf045a51ff06294bdb793d41b59
URL:		http://team.pld-linux.org/~wolf/eithne/
BuildRequires:	dotnet-gtk-sharp2-devel >= 2.10.2
BuildRequires:	gettext-tools
BuildRequires:	mono-csharp >= 1.2.5
Requires:	gtk+2 >= 2:2.12.1
Suggests:	fftw3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Extensible image recognition systems modelling program.

%description -l pl.UTF-8
Rozszerzalny program modelujący systemy rozpoznawania obrazów.

%prep
%setup -q -n eithne-%{version}

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_pixmapsdir},%{_desktopdir},%{_libdir}/eithne/Plugins}

install eithne.exe		$RPM_BUILD_ROOT%{_libdir}/eithne
install *.dll			$RPM_BUILD_ROOT%{_libdir}/eithne
install *.dll.config		$RPM_BUILD_ROOT%{_libdir}/eithne
install Plugins/*.dll		$RPM_BUILD_ROOT%{_libdir}/eithne/Plugins
install Plugins/*.dll.config	$RPM_BUILD_ROOT%{_libdir}/eithne/Plugins

cat > $RPM_BUILD_ROOT%{_bindir}/FaRetSys << EOF
#!/bin/sh
exec /usr/bin/mono %{_libdir}/eithne/eithne.exe "\$@"
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS
%attr(755,root,root) %{_bindir}/*
%{_libdir}/eithne
