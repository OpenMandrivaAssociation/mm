# debug package is empty and rpmlint rejects build
%define _enable_debug_packages %{nil}
%define debug_package %{nil}

%define	major 14
%define libname %mklibname mm %{major}

Summary:	OSSP mm (Shared Memory Allocation)
Name:		mm
Version:	1.4.2
Release:	13
Group:		System/Libraries
License:	BSD-Style
URL:		http://www.ossp.org/pkg/lib/mm/
Source0:	ftp://ftp.ossp.org/pkg/lib/mm/mm-%{version}.tar.bz2
Patch0:		mm-1.4.2-LDFLAGS.diff
BuildRequires:	libtool
BuildRequires:	autoconf2.5

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
Provides:	mm = %{version}

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
Requires:	%{libname} = %{version}
Provides:	libmm-devel = %{version}
Provides:	mm-devel = %{version}

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

%package -n	%{libname}-static-devel
Group:		Development/C
Summary:	Development files for the OSSP mm (Shared Memory Allocation) Library
Requires:	%{libname} = %{version}
Provides:	libmm-static-devel = %{version}
Provides:	mm-static-devel = %{version}

%description -n	%{libname}-static-devel
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

%files -n %{libname}-static-devel
%{_libdir}/*.a


%changelog
* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 1.4.2-10mdv2011.0
+ Revision: 661704
- multiarch fixes

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 1.4.2-9mdv2011.0
+ Revision: 606652
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 1.4.2-8mdv2010.1
+ Revision: 523325
- rebuilt for 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.4.2-7mdv2010.0
+ Revision: 426155
- rebuild

* Sun Dec 21 2008 Oden Eriksson <oeriksson@mandriva.com> 1.4.2-6mdv2009.1
+ Revision: 317113
- use %%ldflags (P0)

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.4.2-5mdv2009.0
+ Revision: 223299
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 1.4.2-4mdv2008.1
+ Revision: 153164
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Aug 29 2007 Oden Eriksson <oeriksson@mandriva.com> 1.4.2-2mdv2008.0
+ Revision: 74370
- fix group
- bump release


* Tue Oct 31 2006 Oden Eriksson <oeriksson@mandriva.com> 1.4.2-1mdv2007.0
+ Revision: 74521
- 1.4.2
- fix deps and spec file
- Import mm

* Thu Dec 29 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 1.4.0-1mdk
- 1.4.0
- new url, new, major, etc...

* Tue Feb 15 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 1.3.1-1mdk
- 1.3.1
- new url
- rediffed P0

* Wed Jan 26 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 1.3.0-6mdk
- fix conditional %%multiarch

* Wed Nov 24 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 1.3.0-5mdk
- nuke redundant provides
- misc spec file fixes

* Thu Jun 10 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 1.3.0-4mdk
- rebuilt with gcc-3.4.1

