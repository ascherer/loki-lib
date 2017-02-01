# Welcome to the C++ library Loki.

Loki is a C++ library of designs, containing flexible implementations of common
design patterns and idioms. 

This is a specfile for packaging the [Loki C++
Library](http://loki-lib.sourceforge.net/) in the **deb** and **rpm** formats.
It has been built and tested with **debbuild 17.1.2** and **rpmbuild
4.12.0.1**.

Download [the SOURCE
package](https://downloads.sourceforge.net/project/loki-lib/Loki/Loki%200.1.7/loki-0.1.7.tar.bz2),
put **loki.spec** in the **SPECS** directory and run

    debbuild -ba SPECS/loki.spec
    rpmbuild -ba SPECS/loki.spec
