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
Istnieje mo¿liwo¶æ przypadkowego odziedziczenia metody AUTOLOAD.  Czêsto
zdarzy siê to, gdy jedna z ³añcucha klas stosuje AutoLoader lub definiuje
w³asn±.  Mo¿e to spowodowaæ dziwne komunikaty b³êdów, gdy odszukanie metody
nie powiedzie siê.

Czasami chcesz unikn±æ przypadkowego dziedziczenia.  W takim wypadku,
odziedzicz po Class::WhiteHole.  Ka¿de wywo³anie nieistniej±cej metody
spowoduje zwyczajn± informacjê o b³êdzie perla.


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
