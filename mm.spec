%define	major 14
%define libname %mklibname mm %{major}

Summary:	OSSP mm (Shared Memory Allocation)
Name:		mm
Version:	1.4.2
Release:	11
Group:		System/Libraries
License:	BSD-Style
URL:		http://www.ossp.org/pkg/lib/mm/
Source0:	ftp://ftp.ossp.org/pkg/lib/mm/mm-%{version}.tar.bz2
Patch0:		mm-1.4.2-LDFLAGS.diff
BuildRequires:	autoconf automake libtool

%description
The MM library is a 2-layer abstraction library which simplifies the usage of
shared memory between forked (and this way strongly related) processes under
Unix platforms. On the first layer it hides all platform dependent
implementation details (allocation and locking) when dealing with shared
memory segments and on the second layer it provides a high-level malloc(3)-
style API for a convenient and well known way to work with data-structures
inside those shared memory segments.

The library is released under the term of an open-source (BSD-style) license
because it's originally written for a proposed use inside next versions of
the Apache webserver as a base library for providing shared memory pools to
Apache modules (because currently Apache modules can only use heap-allocated
memory which isn't shared accross the pre-forked server processes). The
requirement actually comes from comprehensive modules like mod_ssl, mod_perl
and mod_php which would benefit a lot from easy to use shared memory pools.
Mostly all functionality (except for shared locks in addition to exclusive
locks and multi-segment memory areas instead of single-segment memory areas)
is already implemented and the library already works fine under FreeBSD,
Linux and Solaris and should also adjust itself for most other Unix platforms
with it's GNU Autoconf and GNU Libtool based configuration and compilation
procedure. 

%package -n	%{libname}
Summary:	OSSP mm (Shared Memory Allocation) Library
Group:		Development/C
Obsoletes:	mm
Provides:	mm = %{version}-%{release}

%description -n %{libname}
The MM library is a 2-layer abstraction library which simplifies the usage of
shared memory between forked (and this way strongly related) processes under
Unix platforms. On the first layer it hides all platform dependent
implementation details (allocation and locking) when dealing with shared
memory segments and on the second layer it provides a high-level malloc(3)-
style API for a convenient and well known way to work with data-structures
inside those shared memory segments.

The library is released under the term of an open-source (BSD-style) license
because it's originally written for a proposed use inside next versions of
the Apache webserver as a base library for providing shared memory pools to
Apache modules (because currently Apache modules can only use heap-allocated
memory which isn't shared accross the pre-forked server processes). The
requirement actually comes from comprehensive modules like mod_ssl, mod_perl
and mod_php which would benefit a lot from easy to use shared memory pools.
Mostly all functionality (except for shared locks in addition to exclusive
locks and multi-segment memory areas instead of single-segment memory areas)
is already implemented and the library already works fine under FreeBSD,
Linux and Solaris and should also adjust itself for most other Unix platforms
with it's GNU Autoconf and GNU Libtool based configuration and compilation
procedure. 

%package -n	%{libname}-devel
Summary:	Development files for the OSSP mm (Shared Memory Allocation) Library
Group:		Development/C
Requires:	%{libname} >= %{version}-%{release}
Obsoletes:	mm-devel
Provides:	libmm-devel = %{version}-%{release}
Provides:	mm-devel = %{version}-%{release}

%description -n	%{libname}-devel
The MM library is a 2-layer abstraction library which simplifies the usage of
shared memory between forked (and this way strongly related) processes under
Unix platforms. On the first layer it hides all platform dependent
implementation details (allocation and locking) when dealing with shared
memory segments and on the second layer it provides a high-level malloc(3)-
style API for a convenient and well known way to work with data-structures
inside those shared memory segments.

This package contain files that are needed to develop applications which use
the MM shared memory library.

%prep

%setup -q
%patch0 -p0

%build

%configure2_5x

%make

%check
make test

%install
rm -rf %{buildroot}

%makeinstall

perl -pi -e "s|/(.*)buildroot||g;" %{buildroot}/usr/bin/mm-config


%multiarch_binaries %{buildroot}%{_bindir}/mm-config

# cleanup
rm -f %{buildroot}%{_libdir}/*.*a

%files -n %{libname}
%{_libdir}/*.so.*

%files -n %{libname}-devel
%doc README LICENSE ChangeLog INSTALL PORTING THANKS
%{multiarch_bindir}/mm-config
%{_bindir}/mm-config
%{_libdir}/*.so
%{_includedir}/*
%{_mandir}/man1/*
%{_mandir}/man3/*
