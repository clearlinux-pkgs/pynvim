#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pynvim
Version  : 0.4.2
Release  : 11
URL      : https://github.com/neovim/pynvim/archive/0.4.2/pynvim-0.4.2.tar.gz
Source0  : https://github.com/neovim/pynvim/archive/0.4.2/pynvim-0.4.2.tar.gz
Summary  : Python client to neovim
Group    : Development/Tools
License  : Apache-2.0
Requires: pynvim-license = %{version}-%{release}
Requires: pynvim-python = %{version}-%{release}
Requires: pynvim-python3 = %{version}-%{release}
Requires: greenlet
Requires: msgpack
Requires: pynvim
BuildRequires : buildreq-distutils3
BuildRequires : greenlet
BuildRequires : msgpack
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pynvim
BuildRequires : pytest
BuildRequires : tox
BuildRequires : virtualenv

%description
Pynvim: Python client to [Neovim](https://github.com/neovim/neovim)
===================================================================

%package license
Summary: license components for the pynvim package.
Group: Default

%description license
license components for the pynvim package.


%package python
Summary: python components for the pynvim package.
Group: Default
Requires: pynvim-python3 = %{version}-%{release}

%description python
python components for the pynvim package.


%package python3
Summary: python3 components for the pynvim package.
Group: Default
Requires: python3-core
Provides: pypi(pynvim)
Requires: pypi(greenlet)
Requires: pypi(msgpack)

%description python3
python3 components for the pynvim package.


%prep
%setup -q -n pynvim-0.4.2
cd %{_builddir}/pynvim-0.4.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1600452513
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pynvim
cp %{_builddir}/pynvim-0.4.2/LICENSE %{buildroot}/usr/share/package-licenses/pynvim/e3db89a4bda5ca1013225637c5e6d0716f6587b5
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pynvim/e3db89a4bda5ca1013225637c5e6d0716f6587b5

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
