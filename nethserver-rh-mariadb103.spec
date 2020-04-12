Summary: NethServer mariadb103 configuration and templates.
Name: nethserver-rh-mariadb103
Version: 0.0.1
Release: 1%{?dist}
License: GPL
Group: Networking/Daemons
Source: %{name}-%{version}.tar.gz
BuildArch: noarch
Requires: rh-mariadb103
Requires: nethserver-base
Requires: nethserver-lib >= 1.0.1
Requires: procps-ng
BuildRequires: nethserver-devtools
AutoReq: no


%description
This package adds necessary startup and configuration items for
mysql.

%prep
%setup

%build
%{__mkdir} -p root/etc/e-smith/sql/init103
%{__mkdir} -p root/var/lib/rh-mariadb103
%{__mkdir} -p root/var/log/rh-mariadb103

perl createlinks

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
%{genfilelist} \
    --dir   /var/log/rh-mariadb103 'attr(0755,mysql,mysql)' \
    --dir   /var/lib/rh-mariadb103 'attr(0755,mysql,mysql)' \
    --file  /usr/bin/mysql103 'attr(0755,root,root)' \
    --file  /usr/bin/mysqladmin103 'attr(0755,root,root)' \
    --file  /usr/bin/mysqlbinlog103 'attr(0755,root,root)' \
    --file  /usr/bin/mysqlcheck103 'attr(0755,root,root)' \
    --file  /usr/bin/mysql_config_editor103 'attr(0755,root,root)' \
    --file  /usr/bin/mysqld_multi103 'attr(0755,root,root)' \
    --file  /usr/bin/mysqldump103 'attr(0755,root,root)' \
    --file  /usr/bin/mysqlimport103 'attr(0755,root,root)' \
    --file  /usr/bin/mysql_plugin103 'attr(0755,root,root)' \
    --file  /usr/bin/mysqlshow103 'attr(0755,root,root)' \
    --file  /usr/bin/mysqlslap103 'attr(0755,root,root)' \
$RPM_BUILD_ROOT \
    > %{name}-%{version}-filelist
echo "%doc COPYING"          >> %{name}-%{version}-filelist

%clean 
rm -rf $RPM_BUILD_ROOT


%preun

%post
/usr/bin/systemctl enable rh-mariadb103-mariadb

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)
%dir %{_nseventsdir}/%{name}-update

%changelog
* Sun Apr 12  2020 stephane de Labrusse <stephdl@de-labrusse.fr> 0.0.1
- Release for rh-mariadb103
