
%define realname   LaTeX-Table
%define version    0.9.14
%define release    %mkrel 1

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Automatic generation of LaTeX tables
Source:     http://www.cpan.org/modules/by-module/LaTeX/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel
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

%description
LaTeX makes professional typesetting easy. Unfortunately, this is not
entirely true for tables and the standard LaTeX table macros have a rather
limited functionality. This module supports many CTAN packages and hides
the complexity of using them behind an easy and intuitive API.





%prep
%setup -q -n %{realname}-%{version} 

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
%{_mandir}/man3/*
%perl_vendorlib/*
/usr/bin/csv2pdf
/usr/bin/ltpretty
/usr/share/man/man1/csv2pdf.1.lzma
/usr/share/man/man1/ltpretty.1.lzma

