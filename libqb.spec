
%define version	0.10.0
%define release	0
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
%defattr(-,root,root,-)
%doc README.markdown
%{_includedir}/qb/
%{_libdir}/libqb.so
%{_libdir}/pkgconfig/libqb.pc
%{_mandir}/man3/qb*3*

%prep
%setup -q -n libqb-%{version}

%build
./autogen.sh
%configure --disable-static 
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
rm -rf $RPM_BUILD_ROOT/%{_docdir}/*

%clean
rm -rf $RPM_BUILD_ROOT
%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc COPYING
%{_libdir}/libqb.so.*
