Name:		check-tcp-syn
Version:	%{version}
Release:	%{release}%{?dist}
Summary:	TCP half-open check script for keepalived's MISC_CHECK

Group:		System Environment/Tools
License:	GPLv2
URL:		https://github.com/ivoronin/check-tcp-syn
Source0:	%{name}-%{version}.tar.gz

Requires:	nmap, libxml2 >= 2.9.1
BuildRequires:	redhat-rpm-config

%description
TCP half-open check script for keepalived's MISC_CHECK

%prep
%setup

%install
install -m 0755 -D check_tcp_syn %{buildroot}/usr/bin/check_tcp_syn

%files
/usr/bin/check_tcp_syn
