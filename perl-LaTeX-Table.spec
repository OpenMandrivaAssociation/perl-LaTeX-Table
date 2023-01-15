%define upstream_name    LaTeX-Table

Name:		perl-%{upstream_name}
Version:	1.0.6
Release:	2

License:	GPL+ or Artistic
Group:		Development/Perl
Summary:	Automatic generation of LaTeX tables
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/LaTeX/%{upstream_name}-v%{version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Module::Pluggable)
BuildRequires:	perl(Moose)
BuildRequires:	perl(Moose::Policy::FollowPBP)
BuildRequires:	perl(MooseX::FollowPBP)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Template)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::NoWarnings)
BuildRequires:	perl(Text::CSV)
BuildRequires:	perl(Text::Wrap)
BuildRequires:	perl(version)

BuildArch:	noarch

%description
LaTeX makes professional typesetting easy. Unfortunately, this is not
entirely true for tables and the standard LaTeX table macros have a rather
limited functionality. This module supports many CTAN packages and hides
the complexity of using them behind an easy and intuitive API.

%prep
%autosetup -p1 -n %{upstream_name}-v%{version}
perl Makefile.PL INSTALLDIRS=vendor

%build
%make_build

%check
%make test

%install
%make_install

%files
%doc README Changes LICENSE
%{_mandir}/man1/*
%{_mandir}/man3/*
%{perl_vendorlib}/*
%{_bindir}/csv2pdf
%{_bindir}/ltpretty
