Summary:	Static OpenSLP Tool for embedded systems
Name:		slptool-static
Version:	1.0.11
Release:	%mkrel 3
License:	BSD
Group:		Networking/Other
URL:		http://www.openslp.org/
Source0:	ftp://openslp.org/pub/openslp/openslp-%{version}/openslp-%{version}.tar.bz2
Patch0:		slptool-add-lifetime.diff
BuildRequires:	uClibc-devel
BuildRequires:	uClibc-static-devel
BuildRequires:	libtool
BuildRequires:	automake
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
Service Location Protocol is an IETF standards track protocol that provides a
framework to allow networking applications to discover the existence, location,
and configuration of networked services in enterprise networks.

OpenSLP is an open source implementation of the SLPv2 protocol as defined by
RFC 2608 and RFC 2614.  

This package includes a statically linked version of slptool, suitable for
embedded systems.

%prep

%setup -q -n openslp-%{version}
%patch0 -p0

%build
#libtoolize --copy --force; autoheader; aclocal-1.7; automake-1.7 --add-missing --copy; autoconf
libtoolize --copy --force
autoreconf

./configure --enable-shared=no

perl -pi -e "s/lresolv/lresolv -all-static/" slptool/Makefile
uclibc make
cp slptool/slptool ./slptool-static

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_bindir}
install -m0755 slptool-static %{buildroot}%{_bindir}/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%attr(0755,root,root) %{_bindir}/slptool-static


