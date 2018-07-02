#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-IPC-Run3
Version  : 0.048
Release  : 1
URL      : https://cpan.metacpan.org/authors/id/R/RJ/RJBS/IPC-Run3-0.048.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/R/RJ/RJBS/IPC-Run3-0.048.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libi/libipc-run3-perl/libipc-run3-perl_0.048-1.debian.tar.xz
Summary  : 'run a subprocess with input/ouput redirection'
Group    : Development/Tools
License  : GPL-2.0
Requires: perl-IPC-Run3-license
Requires: perl-IPC-Run3-man

%description
IPC::Run3 - run a subprocess in batch mode (a la system) on Unix, Win32, etc.
SYNOPSIS

%package license
Summary: license components for the perl-IPC-Run3 package.
Group: Default

%description license
license components for the perl-IPC-Run3 package.


%package man
Summary: man components for the perl-IPC-Run3 package.
Group: Default

%description man
man components for the perl-IPC-Run3 package.


%prep
tar -xf %{SOURCE1}
cd ..
%setup -q -n IPC-Run3-0.048
mkdir -p %{_topdir}/BUILD/IPC-Run3-0.048/deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/IPC-Run3-0.048/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/perl-IPC-Run3
cp LICENSE %{buildroot}/usr/share/doc/perl-IPC-Run3/LICENSE
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot}
else
./Build install --installdirs=site --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.26.1/IPC/Run3.pm
/usr/lib/perl5/site_perl/5.26.1/IPC/Run3/ProfArrayBuffer.pm
/usr/lib/perl5/site_perl/5.26.1/IPC/Run3/ProfLogReader.pm
/usr/lib/perl5/site_perl/5.26.1/IPC/Run3/ProfLogger.pm
/usr/lib/perl5/site_perl/5.26.1/IPC/Run3/ProfPP.pm
/usr/lib/perl5/site_perl/5.26.1/IPC/Run3/ProfReporter.pm

%files license
%defattr(-,root,root,-)
/usr/share/doc/perl-IPC-Run3/LICENSE

%files man
%defattr(-,root,root,-)
/usr/share/man/man3/IPC::Run3.3
/usr/share/man/man3/IPC::Run3::ProfArrayBuffer.3
/usr/share/man/man3/IPC::Run3::ProfLogReader.3
/usr/share/man/man3/IPC::Run3::ProfLogger.3
/usr/share/man/man3/IPC::Run3::ProfPP.3
/usr/share/man/man3/IPC::Run3::ProfReporter.3
