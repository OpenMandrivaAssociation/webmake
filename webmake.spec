%define name	webmake
%define version	2.4
%define release 4mdk
%define	module	HTML-WebMake

Name: 	 	%{name}
Summary: 	Content management and web templating system
Version: 	%{version}
Release: 	%{release}

Source0:	%{module}-%{version}.tar.bz2
URL:		http://webmake.taint.org/
License:	GPL
Group:		Networking/WWW
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	perl-devel
Requires:	perl-IO-String perl-Image-Size perl-Text-EtText
Requires:	perl-DB_File perl-HTML-Parser
Provides:	perl(HTML::WebMake::PerlCodeLibrary)
BuildArch:	noarch

%description
WebMake is a simple content management system, based around a templating
system for HTML documents and an emphasis on page generation.

What makes it different from the many other templating engines out there,
is that it's been designed to have lots of built-in smarts about what a
"typical" informational website needs in the way of functionality: metadata
support, dynamic index generation from metadata, automatically-generated
sitemaps and navigational aids, user-defined tags, and support for non-HTML
input and output -- and, of course, embedded Perl code. ;)

%prep
%setup -q -n %{module}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make
										
%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
mkdir -p %buildroot/%_datadir/vim/syntax
cp *.vim %buildroot/%_datadir/vim/syntax
cd %buildroot
rm -fr `find -name 'perllocal.pod'`

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README Changes LICENSE TODO *.cgi doc
%{_bindir}/%name
%{_bindir}/%{name}_cvs_import
%{_mandir}/man1/*
%{_mandir}/man3*/*
%{perl_vendorlib}/HTML/WebMake*
%{_datadir}/vim/syntax/%name.vim

