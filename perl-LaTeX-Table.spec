%define upstream_name    LaTeX-Table
%define upstream_version v1.0.6

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

License:	GPL+ or Artistic
Group:		Development/Perl
Summary:	Automatic generation of LaTeX tables
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/LaTeX/%{upstream_name}-%{upstream_version}.tar.gz

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
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README Changes LICENSE
%{_mandir}/man1/*
%{_mandir}/man3/*
%{perl_vendorlib}/*
%{_bindir}/csv2pdf
%{_bindir}/ltpretty

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 1.0.6-2mdv2011.0
+ Revision: 656934
- rebuild for updated spec-helper

* Sat Nov 13 2010 Jérôme Quelin <jquelin@mandriva.org> 1.0.6-1mdv2011.0
+ Revision: 597103
- update to v1.0.6

* Sat Aug 28 2010 Jérôme Quelin <jquelin@mandriva.org> 1.0.5-1mdv2011.0
+ Revision: 573786
- update to v1.0.5

  + Funda Wang <fwang@mandriva.org>
    - revert dup changes
    - BR MooseX::FollowPBP for test

* Tue Jul 27 2010 Jérôme Quelin <jquelin@mandriva.org> 1.0.2-1mdv2011.0
+ Revision: 561567
- adding missing buildrequires:
- update to v1.0.2

* Tue Mar 02 2010 Jérôme Quelin <jquelin@mandriva.org> 1.0.1-1mdv2011.0
+ Revision: 513469
- update to v1.0.1

* Wed Sep 09 2009 Jérôme Quelin <jquelin@mandriva.org> 1.0.0-1mdv2010.0
+ Revision: 435708
- update to v1.0.0

* Mon Jul 27 2009 Jérôme Quelin <jquelin@mandriva.org> 0.9.17-1mdv2010.0
+ Revision: 400629
- update to 0.9.17

* Wed Jul 15 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.9.16-1mdv2010.0
+ Revision: 396222
- update to new version 0.9.16

* Sat May 30 2009 Jérôme Quelin <jquelin@mandriva.org> 0.9.15-1mdv2010.0
+ Revision: 381277
-update to 0.9.15
- using %%perl_convert_version
- sanitized license & description fields

* Fri May 15 2009 Jérôme Quelin <jquelin@mandriva.org> 0.9.14-2mdv2010.0
+ Revision: 376053
- fixing %%files section in man1
- rebuild

* Sat Apr 11 2009 Olivier Thauvin <nanardon@mandriva.org> 0.9.14-1mdv2009.1
+ Revision: 366291
- import perl-LaTeX-Table


* Sat Apr 11 2009 cpan2dist 0.9.14-1mdv
- initial mdv release, generated with cpan2dist

