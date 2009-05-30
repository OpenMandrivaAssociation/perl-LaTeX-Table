%define upstream_name    LaTeX-Table
%define upstream_version 0.9.15

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

License:    GPL+ or Artistic
Group:      Development/Perl
Summary:    Automatic generation of LaTeX tables
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/LaTeX/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Module::Pluggable)
BuildRequires: perl(Moose)
BuildRequires: perl(Moose::Policy::FollowPBP)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Template)
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::NoWarnings)
BuildRequires: perl(Text::Wrap)
BuildRequires: perl(version)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
LaTeX makes professional typesetting easy. Unfortunately, this is not
entirely true for tables and the standard LaTeX table macros have a rather
limited functionality. This module supports many CTAN packages and hides
the complexity of using them behind an easy and intuitive API.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README Changes LICENSE
%{_mandir}/man1/*
%{_mandir}/man3/*
%perl_vendorlib/*
/usr/bin/csv2pdf
/usr/bin/ltpretty

