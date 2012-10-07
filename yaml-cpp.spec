Summary:	YAML parser and emitter for C++
Summary(pl.UTF-8):	Biblioteka C++ analizująca i generująca YAML
Name:		yaml-cpp
Version:	0.3.0
Release:	1
License:	MIT
Group:		Libraries
#Source0Download: http://code.google.com/p/yaml-cpp/downloads/list
Source0:	http://yaml-cpp.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	9aa519205a543f9372bf4179071c8ac6
URL:		http://code.google.com/p/yaml-cpp/
BuildRequires:	cmake >= 2.6
BuildRequires:	libstdc++-devel
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
YAML parser and emitter for C++.

%description -l pl.UTF-8
Biblioteka C++ analizująca i generująca YAML.

%package devel
Summary:	Header files for yaml-cpp library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki yaml-cpp
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
Header files for yaml-cpp library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki yaml-cpp.

%prep
%setup -q -n %{name}

%build
%cmake .
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc license.txt
%attr(755,root,root) %{_libdir}/libyaml-cpp.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libyaml-cpp.so.0.3

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libyaml-cpp.so
%{_includedir}/yaml-cpp
%{_pkgconfigdir}/yaml-cpp.pc
