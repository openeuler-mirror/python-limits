%global _empty_manifest_terminate_build 0
Name:		python-limits
Version:	2.7.0
Release:	1
Summary:	Rate limiting utilities
License:	MIT
URL:		https://limits.readthedocs.org
Source0:	https://files.pythonhosted.org/packages/b4/95/b08b833e2a386d08df7a5e5b8b2115bb0a930320088fc4efdf9746367a1d/limits-2.7.0.tar.gz
BuildArch:	noarch

Requires:	python3-six

%description
limits provides utilities to implement rate limiting using
various strategies and storage backends such as redis & memcached.

%package -n python3-limits
Summary:	Rate limiting utilities
Provides:	python-limits
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
%description -n python3-limits
limits provides utilities to implement rate limiting using
various strategies and storage backends such as redis & memcached.

%package help
Summary:	Development documents and examples for limits
Provides:	python3-limits-doc
%description help
Development documents and examples for limits

%prep
%autosetup -n limits-2.7.0

%build
%py3_build

%install
%py3_install
install -d -m755 %{buildroot}/%{_pkgdocdir}
if [ -d doc ]; then cp -arf doc %{buildroot}/%{_pkgdocdir}; fi
if [ -d docs ]; then cp -arf docs %{buildroot}/%{_pkgdocdir}; fi
if [ -d example ]; then cp -arf example %{buildroot}/%{_pkgdocdir}; fi
if [ -d examples ]; then cp -arf examples %{buildroot}/%{_pkgdocdir}; fi
pushd %{buildroot}
if [ -d usr/lib ]; then
	find usr/lib -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/lib64 ]; then
	find usr/lib64 -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/bin ]; then
	find usr/bin -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/sbin ]; then
	find usr/sbin -type f -printf "/%h/%f\n" >> filelist.lst
fi
touch doclist.lst
if [ -d usr/share/man ]; then
	find usr/share/man -type f -printf "/%h/%f.gz\n" >> doclist.lst
fi
popd
mv %{buildroot}/filelist.lst .
mv %{buildroot}/doclist.lst .

%files -n python3-limits -f filelist.lst
%dir %{python3_sitelib}/*

%files help -f doclist.lst
%{_docdir}/*

%changelog
* Wed Aug 24 2022 hkgy <kaguyahatu@outlook.com> - 2.7.0-1
- Update to 2.7.0

* Sat Feb 20 2021 Python_Bot <Python_Bot@openeuler.org>
- Package Spec generated
