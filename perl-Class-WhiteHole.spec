%include	/usr/lib/rpm/macros.perl
%define	pdir	Class
%define	pnam	WhiteHole
Summary:	%{pdir}::%{pnam} - prevent from inheriting AUTOLOAD
Summary(pl):	%{pdir}::%{pnam} - ochrona przed dziedziczeniem AUTOLOAD
Name:		perl-Class-WhiteHole
Version:	0.03
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Its possible to accidentally inherit an AUTOLOAD method.  Often this
will happen if a class somewhere in the chain uses AutoLoader or defines
one of their own.  This can lead to confusing error messages when method
lookups fail.

Sometimes you want to avoid this accidental inheritance.  In that case,
inherit from Class::WhiteHole.  All unhandled methods will produce normal
Perl error messages.

%description -l pl
Istnieje mo�liwo�� przypadkowego odziedziczenia metody AUTOLOAD.  Cz�sto
zdarzy si� to, gdy jedna z �a�cucha klas stosuje AutoLoader lub definiuje
w�asn�.  Mo�e to spowodowa� dziwne komunikaty b��d�w, gdy odszukanie metody
nie powiedzie si�.

Czasami chcesz unikn�� przypadkowego dziedziczenia.  W takim wypadku,
odziedzicz po Class::WhiteHole.  Ka�de wywo�anie nieistniej�cej metody
spowoduje zwyczajn� informacj� o b��dzie perla.


%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}
#%{__make} test

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitelib}/%{pdir}/*.pm
%{_mandir}/man3/*
