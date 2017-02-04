%bcond_without doc

%define source_name loki
Name: %{source_name}-lib
Summary: Loki C++ Library
License: MIT License
URL: http://loki-lib.sourceforge.net/

Version: 0.1.7
Release: 2
Packager: Andreas Scherer <https://ascherer.github.io/>

%if %{_vendor} == "debbuild"
Group: devel
Distribution: Kubuntu 16.04 (x86_64)
%else
Group: Productivity/Development
Distribution: openSUSE 42 (x86_64)
%global __echo `which echo`
%endif

Source0: https://downloads.sourceforge.net/project/loki-lib/Loki/Loki%200.1.7/%{source_name}-%{version}.tar.bz2
Patch1: 0001-Clean-build-of-LevelMutex.patch
Patch2: 0002-Clear-CachedFactoryTest.patch
Patch3: 0003-Suppress-GCC-warning-in-Dependencies.patch
Patch4: 0004-Hard-type-conversion-in-timer.patch
Patch5: 0005-Suppress-two-GCC-warnings-in-main.patch
Patch6: 0006-Several-GCC-warnings-fixed-in-strong.patch
Patch7: 0007-Ignore-return-value-GCC-style.patch
Patch8: 0008-Type-conversion-in-template-of-main.patch
Patch9: 0009-Fix-GCC-warning-in-AssocVectortTest.patch
Patch10: 0010-Un-use-locally-defined-typedef-in-headers.patch
Patch11: 0011-Fix-SmallObjBench.patch

BuildRoot: %{_tmppath}/%{name}-%{version}-root

%package devel
Summary: The Loki C++ headers and development libraries
Group: System Environment/Libraries

%if %{with doc}
%package doc
Summary: The Loki C++ html docs
Group: System Environment/Libraries
%endif

%description
A C++ library of designs, containing flexible implementations of common design
patterns and idioms.

%description devel
Headers, static libraries, and shared object symlinks for the Loki C++ Library

%if %{with doc}
%description doc
HTML documentation files for the Loki C++ Library
%endif

%prep
%autosetup -n %{source_name}-%{version} -p1

%build
%{__make} build-static build-shared check
%if %{with doc}
cd doc; doxygen Doxyfile
%endif

%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}%{_includedir}
%{__cp} -a include/%{source_name} %{buildroot}%{_includedir}
%{__mkdir_p} %{buildroot}%{_libdir}
%{__cp} -a lib/lib%{source_name}.* %{buildroot}%{_libdir}
(cd %{buildroot}%{_libdir} && ln -s lib%{source_name}.so.%{version} lib%{source_name}.so)
%{__mkdir_p} %{buildroot}%{_sysconfdir}/ld.so.conf.d
%{__echo} "%{_libdir}/%{name}" > \
	%{buildroot}%{_sysconfdir}/ld.so.conf.d/%{name}.conf
%if %{with doc}
%{__mkdir_p} %{buildroot}%{_docdir}/%{name}-%{version}
%{__cp} -a doc/{flex,html,yasli} %{buildroot}%{_docdir}/%{name}-%{version}
%endif

%files
%defattr(755,root,root)
%{_libdir}/lib%{source_name}.so
%{_libdir}/lib%{source_name}.so.%{version}
%{_sysconfdir}/ld.so.conf.d/%{name}.conf

%files devel
%defattr(644,root,root,755)
%{_includedir}/%{source_name}
%{_libdir}/lib%{source_name}.a

%if %{with doc}
%files doc
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}-%{version}
%endif

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%changelog
* Tue Feb 01 2017 Andreas Scherer <andreas_github@freenet.de>
- Update for rpmbuild 4.12.0.1 and debbuild 17.1.2

* Thu Mar 16 2006 Regis Desgroppes <rdesgroppes@besancon.parkeon.com>
- Renamed package to loki-lib (SourceForge project name) as there is another package named loki (Biology)
- Created devel and doc subpackages
- Also building shared library
- Removed LF chars so that rpmbuild generated scriptlets work

* Fri Jan 06 2006 Andreas Scherer <andreas_hacker@freenet.de>
- Initial build
