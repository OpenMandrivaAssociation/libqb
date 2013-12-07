%define major	0
%define libname	%mklibname qb %{major}
%define devname	%mklibname -d qb

Summary:	An IPC library for high performance servers
Name:		libqb
Version:	0.16.0
Release:	3
Group:		System/Libraries
License:	LGPLv2+
Url:		https://github.com/asalkeld/libqb/wiki
Source0:	https://fedorahosted.org/releases/q/u/quarterback/%{name}-%{version}.tar.gz

BuildRequires:	doxygen
BuildRequires:	libtool
BuildRequires:	procps
BuildRequires:	pkgconfig(check)

%description
%{name} provides high performance client server reusable features.
Initially these are IPC and poll.

%package -n %{libname}
Summary:	An IPC library for high performance servers
Group:		System/Libraries

%description -n %{libname}
%{name} provides high performance client server reusable features.
Initially these are IPC and poll.

%package -n %{devname}
Summary:	Development files for libqb
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{_lib}qb0 < 0.14.4-2

%description -n %{devname}
This package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q
./autogen.sh

%build
%configure2_5x --disable-static 
%make

%install
%makeinstall_std
rm -rf %{buildroot}/%{_docdir}/*

%files -n %{libname}
%{_libdir}/libqb.so.%{major}*

%files -n %{devname}
%doc COPYING README.markdown
%{_sbindir}/qb-blackbox
%{_includedir}/qb/
%{_libdir}/libqb.so
%{_libdir}/pkgconfig/libqb.pc
%{_mandir}/man3/qb*3*
%{_mandir}/man8/qb*8*

