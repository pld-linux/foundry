# TODO: deviced plugin (BR: libdeviced >= 3.27.4, <https://gitlab.gnome.org/chergert/deviced>)
#
# Conditional build:
%bcond_without	apidocs		# API documentation
#
Summary:	Framework for Developer Tooling
Summary(pl.UTF-8):	Szkielet narzędzi programistycznych
Name:		foundry
Version:	1.1.1
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	https://download.gnome.org/sources/foundry/1.1/%{name}-%{version}.tar.xz
# Source0-md5:	75ff5a9b145c7f51e1068e3d2a61ba60
URL:		https://gitlab.gnome.org/GNOME/foundry
BuildRequires:	cmark-devel >= 0.29.0
BuildRequires:	editorconfig-devel
BuildRequires:	flatpak-devel
BuildRequires:	gcc >= 6:4.7
%{?with_apidocs:BuildRequires:	gi-docgen}
BuildRequires:	glib2-devel >= 1:2.82
BuildRequires:	gobject-introspection-devel
BuildRequires:	gom-devel >= 0.5.0
BuildRequires:	gtk-webkit6-devel
BuildRequires:	gtk4-devel >= 4.20
BuildRequires:	gtksourceview5-devel >= 5.18
BuildRequires:	json-glib-devel >= 1.0
BuildRequires:	libadwaita-devel >= 1.7
BuildRequires:	libdex-devel >= 1.1
BuildRequires:	libgit2-devel >= 1.6
BuildRequires:	libpeas2-devel >= 2.0
BuildRequires:	libsecret-devel
BuildRequires:	libsoup3-devel >= 3.0
BuildRequires:	libspelling-devel >= 0.4
BuildRequires:	libssh2-devel
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	meson >= 1.1
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 2.042
BuildRequires:	sysprof-devel >= 3.38
BuildRequires:	tar >= 1:1.22
BuildRequires:	template-glib-devel >= 1.0
BuildRequires:	vte-gtk4-devel >= 0.80
BuildRequires:	xz
BuildRequires:	yaml-devel >= 0.1
Requires:	glib2 >= 1:2.82
Requires:	gom >= 0.5.0
Requires:	json-glib >= 1.0
Requires:	libdex >= 1.1
Requires:	libgit2 >= 1.6
Requires:	sysprof-libs >= 3.38
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This tool aims to extract much of what makes GNOME Builder an IDE into
a library and companion command-line tool in order to bring many of
the automatic IDE features of Builder to a command line environment.

%description -l pl.UTF-8
To narzędzie ma na celu wyciągnięcie elementów IDE z GNOME Buildera do
biblioteki współdzielonej i towarzyszącego polecenia, aby udostępnić
wiele automatycznych funkcji IDE z poziomu linii poleceń.

%package devel
Summary:	Header files for Foundry library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Foundry
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	editorconfig-devel
Requires:	flatpak-devel
Requires:	glib2-devel >= 1:2.82
Requires:	gom-devel >= 0.5.0
Requires:	json-glib-devel >= 1.0
Requires:	libdex-devel >= 1.1
Requires:	libgit2-devel >= 1.6
Requires:	libpeas2-devel >= 2.0
Requires:	libsecret-devel
Requires:	libsoup3-devel >= 3.0
Requires:	libssh2-devel
Requires:	libxml2-devel >= 2.0
Requires:	sysprof-devel >= 3.38
Requires:	template-glib-devel >= 1.0
Requires:	yaml-devel >= 0.1

%description devel
Header files for Foundry library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Foundry.

%package apidocs
Summary:	API documentation for Foundry library
Summary(pl.UTF-8):	Dokumentacja API biblioteki Foundry
Group:		Documentation
BuildArch:	noarch

%description apidocs
API documentation for Foundry library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki Foundry.

%package gtk
Summary:	Integrate libfoundry into GTK applications
Summary(pl.UTF-8):	Integracja libfoundry w aplikacjach GTK
Group:		X11/Libraries
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	cmark-lib >= 0.29.0
Requires:	gtk4 >= 4.20
Requires:	gtksourceview5 >= 5.18
Requires:	libspelling >= 0.4
Requires:	vte-gtk4 >= 0.80

%description gtk
Integrate libfoundry into GTK applications.

%description gtk -l pl.UTF-8
Integracja libfoundry w aplikacjach GTK.

%package gtk-devel
Summary:	Header files for Foundry GTK library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Foundry GTK
Group:		X11/Development/Libraries
Requires:	%{name}-devel%{?_isa} = %{version}-%{release}
Requires:	%{name}-gtk%{?_isa} = %{version}-%{release}
Requires:	cmark-devel >= 0.29.0
Requires:	gtk-webkit6-devel
Requires:	gtk4-devel >= 4.20
Requires:	gtksourceview5-devel >= 5.18
Requires:	libspelling-devel >= 0.4
Requires:	vte-gtk4-devel >= 0.80

%description gtk-devel
Header files for Foundry GTK library.

Pliki nagłówkowe biblioteki Foundry GTK.

%package gtk-apidocs
Summary:	API documentation for Foundry GTK library
Summary(pl.UTF-8):	Dokumentacja API biblioteki Foundry GTK
Group:		Documentation
BuildArch:	noarch

%description gtk-apidocs
API documentation for Foundry GTK library.

%description gtk-apidocs -l pl.UTF-8
Dokumentacja API biblioteki Foundry GTK.

%package adw
Summary:	Integrate libfoundry into GNOME applications
Summary(pl.UTF-8):	Integracja libfoundry w aplikacjach GNOME
Group:		X11/Libraries
Requires:	%{name}-gtk%{?_isa} = %{version}-%{release}
Requires:	libadwaita >= 1.7

%description adw
Integrate libfoundry into GNOME applications.

%description adw -l pl.UTF-8
Integracja libfoundry w aplikacjach GNOME.

%package adw-devel
Summary:	Header files for Foundry Adw library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Foundry Adw
Group:		X11/Development/Libraries
Requires:	%{name}-adw%{?_isa} = %{version}-%{release}
Requires:	%{name}-gtk-devel%{?_isa} = %{version}-%{release}
Requires:	libadwaita-devel >= 1.7

%description adw-devel
Header files for Foundry Adw library.

%description adw-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Foundry Adw.

%package adw-apidocs
Summary:	API documentation for Foundry Adw library
Summary(pl.UTF-8):	Dokumentacja API biblioteki Foundry Adw
Group:		Documentation
BuildArch:	noarch

%description adw-apidocs
API documentation for Foundry Adw library.

%description adw-apidocs -l pl.UTF-8
Dokumentacja API biblioteki Foundry Adw.

%prep
%setup -q

%build
# --default-library=both is not supported, foundry (as of 1.2.0) uses static libs internally
%meson \
	--default-library=shared \
	%{?with_apidocs:-Ddocs=true}

# TODO in 1.2.0
#	-Dsysprof=%{__enabled_disabled sysprof}

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%if %{with apidocs}
install -d $RPM_BUILD_ROOT%{_gidocdir}
%{__mv} $RPM_BUILD_ROOT%{_docdir}/foundry*-1 $RPM_BUILD_ROOT%{_gidocdir}
%endif

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
%glib_compile_schemas

%postun
/sbin/ldconfig
%glib_compile_schemas

%post	gtk -p /sbin/ldconfig
%postun	gtk -p /sbin/ldconfig

%post	adw -p /sbin/ldconfig
%postun	adw -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS README.md
%attr(755,root,root) %{_bindir}/foundry
%{_libdir}/libfoundry-1.so.*.*.*
%ghost %{_libdir}/libfoundry-1.so.1
%{_libdir}/girepository-1.0/Foundry-1.typelib
%{_datadir}/foundry
%{_datadir}/glib-2.0/schemas/org.gnome.foundry.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.foundry.build.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.foundry.ctags.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.foundry.distcc.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.foundry.flatpak.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.foundry.forge.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.foundry.gitlab.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.foundry.lsp.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.foundry.network.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.foundry.ollama.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.foundry.project.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.foundry.run.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.foundry.terminal.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.foundry.text.gschema.xml
%{_datadir}/metainfo/org.gnome.Foundry.metainfo.xml
%{bash_compdir}/foundry
%{_mandir}/man1/foundry.1*

%files devel
%defattr(644,root,root,755)
%{_libdir}/libfoundry-1.so
%{_includedir}/libfoundry-1
%dir %{_libdir}/libfoundry-1
%{_libdir}/libfoundry-1/include
%{_datadir}/gir-1.0/Foundry-1.gir
%{_pkgconfigdir}/libfoundry-1.pc

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gidocdir}/foundry-1
%endif

%files gtk
%defattr(644,root,root,755)
%{_libdir}/libfoundry-gtk-1.so.*.*.*
%ghost %{_libdir}/libfoundry-gtk-1.so.1
%{_libdir}/girepository-1.0/FoundryGtk-1.typelib

%files gtk-devel
%defattr(644,root,root,755)
%{_libdir}/libfoundry-gtk-1.so
%{_includedir}/libfoundry-gtk-1
%{_datadir}/gir-1.0/FoundryGtk-1.gir
%{_pkgconfigdir}/libfoundry-gtk-1.pc

%if %{with apidocs}
%files gtk-apidocs
%defattr(644,root,root,755)
%{_gidocdir}/foundry-gtk-1
%endif

%files adw
%defattr(644,root,root,755)
%{_libdir}/libfoundry-adw-1.so.*.*.*
%ghost %{_libdir}/libfoundry-adw-1.so.1
%{_libdir}/girepository-1.0/FoundryAdw-1.typelib

%files adw-devel
%defattr(644,root,root,755)
%{_libdir}/libfoundry-adw-1.so
%{_includedir}/libfoundry-adw-1
%{_datadir}/gir-1.0/FoundryAdw-1.gir
%{_pkgconfigdir}/libfoundry-adw-1.pc

%if %{with apidocs}
%files adw-apidocs
%defattr(644,root,root,755)
%{_gidocdir}/foundry-adw-1
%endif
