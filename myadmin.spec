Summary:	Myadmin - web-based MySQL administration
Summary(pl.UTF-8):	Myadmin - administracja bazami MySQL przez WWW
Name:		myadmin
Version:	0.4
Release:	1
License:	GPL
Group:		Applications/Databases/Interfaces
Source0:	ftp://myadmin.cheapnet.net/pub/myadmin/%{name}-%{version}.tar.gz
# Source0-md5:	9915ce0cf36c9e33bf4bf8a600a6d85d
Patch0:		%{name}-perlpath.patch
URL:		http://myadmin.cheapnet.net/
Requires:	mysql
Requires:	perl
Requires:	perl-CGI
Requires:	perl-DBI
Requires:	perl-Msql-Mysql-modules
Requires:	webserver
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_cgibindir	/home/services/httpd/cgi-bin

%description
MyAdmin is a web cgi written in perl to fully administer the MySQL
database created by http://www.tcx.se/ SQL interface, imports and
export via the web. It can administrate any database on any server
that the cgi host has permissions to connect.

%description -l pl.UTF-8
MyAdmin jest napisanym w perl'u skryptem cgi służącym do
administrowania bazami danych MySQL. Interfejs SQL tworzony został
przez http://www.tcx.se/. Potrafi zarządzać każdą bazą danych, do
której host ma możliwość się połączyć.

%prep
%setup -q
%patch -P0 -p1

%build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_cgibindir}

cp myadmin.cgi $RPM_BUILD_ROOT%{_cgibindir}/myadmin.cgi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES TODO
%attr(755,root,root) %{_cgibindir}/myadmin.cgi
