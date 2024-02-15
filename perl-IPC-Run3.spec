#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v4
# autospec commit: da8b975a5699
#
Name     : perl-IPC-Run3
Version  : 0.049
Release  : 25
URL      : https://cpan.metacpan.org/authors/id/R/RJ/RJBS/IPC-Run3-0.049.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/R/RJ/RJBS/IPC-Run3-0.049.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libi/libipc-run3-perl/libipc-run3-perl_0.048-1.debian.tar.xz
Summary  : 'run a subprocess with input/output redirection'
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0 MIT
Requires: perl-IPC-Run3-license = %{version}-%{release}
Requires: perl-IPC-Run3-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
IPC::Run3 - run a subprocess in batch mode (a la system) on Unix, Win32, etc.
SYNOPSIS

%package dev
Summary: dev components for the perl-IPC-Run3 package.
Group: Development
Provides: perl-IPC-Run3-devel = %{version}-%{release}
Requires: perl-IPC-Run3 = %{version}-%{release}

%description dev
dev components for the perl-IPC-Run3 package.


%package license
Summary: license components for the perl-IPC-Run3 package.
Group: Default

%description license
license components for the perl-IPC-Run3 package.


%package perl
Summary: perl components for the perl-IPC-Run3 package.
Group: Default
Requires: perl-IPC-Run3 = %{version}-%{release}

%description perl
perl components for the perl-IPC-Run3 package.


%prep
%setup -q -n IPC-Run3-0.049
cd %{_builddir}
tar xf %{_sourcedir}/libipc-run3-perl_0.048-1.debian.tar.xz
cd %{_builddir}/IPC-Run3-0.049
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/IPC-Run3-0.049/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-IPC-Run3
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-IPC-Run3/c049809f0f110ce729d1d3d865e859a199cb0725 || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/IPC::Run3.3
/usr/share/man/man3/IPC::Run3::ProfArrayBuffer.3
/usr/share/man/man3/IPC::Run3::ProfLogReader.3
/usr/share/man/man3/IPC::Run3::ProfLogger.3
/usr/share/man/man3/IPC::Run3::ProfPP.3
/usr/share/man/man3/IPC::Run3::ProfReporter.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-IPC-Run3/c049809f0f110ce729d1d3d865e859a199cb0725

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
