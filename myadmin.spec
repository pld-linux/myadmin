Summary:	Myadmin - web-based mysql administration
Summary(pl):	Myadmin - administracja bazami mysql przez WWW
Name:		myadmin
Version:	0.4
Release:	1
License:	GPL
Group:		Applications/Databases/Interfaces
Group(de):	Applikationen/Dateibanken/Schnittstellen
Group(pl):	Aplikacje/Bazy danych/Interfejsy
Source0:	ftp://myadmin.cheapnet.net/pub/myadmin/%{name}-%{version}.tar.gz
Url:		http://myadmin.cheapnet.net
Requires:	mysql
Requires:	perl
Requires:	webserver
Buildarch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_cgibindir	/home/httpd/cgi-bin

%description
MyAdmin is a web cgi written in perl to fully administer the MySQL
database created by www.tcx.se SQL interface, imports and export via
the web. It can administrate any database on any server that the cgi
host has permissions to connect.

%description -l pl
MyAdmin jest napisanym w perl'u skryptem cgi s³u¿±cym do administowania
bazami danych MySQL. Interfejs SQL tworzony zosta³ przez www.tcx.se.
Potrafi zarz±dzaæ ka¿d± baz± danych, do której host ma mo¿liwo¶æ siê
po³±czyæ.

%prep
%setup -q 

%build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_cgibindir}

cp myadmin.cgi $RPM_BUILD_ROOT%{_cgibindir}/myadmin.cgi

gzip -9nf CHANGES TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_cgibindir}/myadmin.cgi
