Summary:	YAML parser and emitter for C++
Summary(pl.UTF-8):	Biblioteka C++ analizująca i generująca YAML
Name:		yaml-cpp
Version:	0.6.2
Release:	1
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/jbeder/yaml-cpp/releases
Source0:	https://github.com/jbeder/yaml-cpp/archive/%{name}-%{version}.tar.gz
# Source0-md5:	5b943e9af0060d0811148b037449ef82
Patch0:		%{name}-gtest-no-install.patch
URL:		https://github.com/jbeder/yaml-cpp/
BuildRequires:	cmake >= 2.6
BuildRequires:	libstdc++-devel >= 6:4.7
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
Requires:	libstdc++-devel >= 6:4.7

%description devel
Header files for yaml-cpp library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki yaml-cpp.

%prep
%setup -q -n %{name}-%{name}-%{version}
%patch0 -p1

%build
install -d build
cd build
%cmake ..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%attr(755,root,root) %{_libdir}/libyaml-cpp.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libyaml-cpp.so.0.6

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libyaml-cpp.so
%{_includedir}/yaml-cpp
%{_pkgconfigdir}/yaml-cpp.pc
%{_libdir}/cmake/yaml-cpp
