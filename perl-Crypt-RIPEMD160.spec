#
# Conditional build:
%bcond_without	tests	# Do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	RIPEMD160
Summary:	Crypt::RIPEMD160 Perl module - RIPEMD160 message digest algorithm
Summary(pl):	Modu³ Perla Crypt::RIPEMD160 - algorytm skrótu RIPEMD160
Name:		perl-Crypt-RIPEMD160
Version:	0.04
Release:	4
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	132c1b74deabd6511726945373308699
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Crypt::RIPEMD160 module allows you to use the RIPEMD160 Message
Digest algorithm from within Perl programs. RIPEMD-160 is a 160-bit
cryptographic hash function, designed by Hans Dobbertin, Antoon
Bosselaers, and Bart Preneel. It is intended to be used as a secure
replacement for the 128-bit hash functions MD4, MD5, and RIPEMD.

%description -l pl
Modu³ Crypt::RIPEMD160 pozwala na u¿ywanie algorytmu skrótu RIPEMD160
z poziomu programów w Perlu. RIPEMD-160 jest 160-bitow±
kryptograficzn± funkcj± mieszaj±c±, opracowan± przez Hansa Dobbertina,
Antoona Bosselaersa i Barta Preneela. Ma byæ bezpiecznym zamiennikiem
128-bitowych funkcji mieszaj±cych MD4, MD5 i RIPEMD.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README rmd160/doc/*.html
%{perl_vendorarch}/Crypt/RIPEMD160.pm
%{perl_vendorarch}/Crypt/RIPEMD160
%dir %{perl_vendorarch}/auto/Crypt/RIPEMD160
%{perl_vendorarch}/auto/Crypt/RIPEMD160/autosplit.ix
%{perl_vendorarch}/auto/Crypt/RIPEMD160/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Crypt/RIPEMD160/*.so
%{_mandir}/man3/*
