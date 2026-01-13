#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Class
%define		pnam	WhiteHole
Summary:	Class::WhiteHole - prevent from inheriting AUTOLOAD
Summary(pl.UTF-8):	Class::WhiteHole - ochrona przed dziedziczeniem AUTOLOAD
Name:		perl-Class-WhiteHole
Version:	0.04
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	43b986ad7d5d186a9a43d2d69a2ef327
URL:		http://search.cpan.org/dist/Class-WhiteHole/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Its possible to accidentally inherit an AUTOLOAD method. Often this
will happen if a class somewhere in the chain uses AutoLoader or
defines one of their own. This can lead to confusing error messages
when method lookups fail.

Sometimes you want to avoid this accidental inheritance. In that case,
inherit from Class::WhiteHole. All unhandled methods will produce
normal Perl error messages.

%description -l pl.UTF-8
Istnieje możliwość przypadkowego odziedziczenia metody AUTOLOAD.
Często zdarzy się to, gdy jedna z łańcucha klas stosuje AutoLoader lub
definiuje własną. Może to spowodować dziwne komunikaty błędów, gdy
odszukanie metody nie powiedzie się.

Czasami chcesz uniknąć przypadkowego dziedziczenia. W takim wypadku,
odziedzicz po Class::WhiteHole. Każde wywołanie nieistniejącej metody
spowoduje zwyczajną informację o błędzie Perla.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
