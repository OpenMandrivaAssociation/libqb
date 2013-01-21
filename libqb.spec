%define version	0.14.4
%define release	1
%define develname %mklibname -d qb
%define name	%mklibname qb

Name:           %name
Version:        %version
Release:        %release
Summary:        An IPC library for high performance servers
Group:          System/Libraries
License:        LGPLv2+
URL:            https://github.com/asalkeld/libqb/wiki
Source0:        https://fedorahosted.org/releases/q/u/quarterback/libqb-%{version}.tar.gz

BuildRequires:  autoconf automake libtool doxygen procps check-devel

%description
%{name} provides high performance client server reusable features.
Initially these are IPC and poll.


%package 	devel
Group:		Development/C
Summary:	Development files for libqb
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{name} = %{version}

%description 	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}

%files devel
%doc README.markdown
%{_includedir}/qb/
%{_libdir}/libqb.so
%{_libdir}/pkgconfig/libqb.pc
%{_mandir}/man3/qb*3*
%{_mandir}/man8/qb*8*
%{_sbindir}/qb-blackbox

%prep
%setup -q -n libqb-%{version}

%build
./autogen.sh
%configure2_5x --disable-static 
%make

%install
#make install DESTDIR=%{buildroot}
%makeinstall_std
find %{buildroot} -name '*.la' -exec rm -f {} ';'
rm -rf %{buildroot}/%{_docdir}/*

%files
%doc COPYING
%{_libdir}/libqb.so.*

%changelog
* Thu Feb 09 2012 Anton Kirilenko <anton.kirilenko@rosalab.ru> 0.10.0-0
+ Revision: 772333
- new upstream version

* Wed Jan 11 2012 Anton Kirilenko <anton.kirilenko@rosalab.ru> 0.8.1-1.14
+ Revision: 759702
- New upstream release: updated to 0.8.1

* Wed Dec 14 2011 Anton Kirilenko <anton.kirilenko@rosalab.ru> 0.7.0-1.13
+ Revision: 741160
- Initial package
- Created package structure for libqb.
