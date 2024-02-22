%define mate_ver	%(echo %{version}|cut -d. -f1,2)
%define _disable_ld_no_undefined 1

Summary:	Plugins for pluma
Name:		pluma-plugins
Version:	1.28.0
Release:	1
License:	GPLv2+
Group:		Editors 
Url:		https://www.mate-desktop.org
Source0:	https://pub.mate-desktop.org/releases/%{mate_ver}/%{name}-%{version}.tar.xz

BuildRequires: intltool
BuildRequires: mate-common
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(dbus-python)
BuildRequires: pkgconfig(vte-2.91)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(pluma) >= 1.6.0
BuildRequires: pkgconfig(pygobject-2.0)
BuildRequires: pkgconfig(gtksourceview-4)
BuildRequires: pkgconfig(libpeas-1.0)
BuildRequires: yelp-devel
BuildRequires: yelp-tools
BuildRequires: python

Requires:	pluma

%description
Pluma is a small but powerful text editor designed expressly
for MATE.

It includes such features as split-screen mode, a plugin
API, which allows Pluma to be extended to support many
features while remaining small at its core, multiple
document editing through the use of a 'tabbed' notebook and
many more functions.


This package contains some extra plugins for Pluma, extending Pluma
functionality.

%files -f %{name}.lang
%doc COPYING AUTHORS
%{_datadir}/pluma/plugins/*
%{_libdir}/pluma/plugins/*
%{_datadir}/glib-2.0/schemas/org.mate.pluma.plugins.*
%{_datadir}/metainfo/pluma-*

#---------------------------------------------------------------------------

%prep
%autosetup -p1

%build
#NOCONFIGURE=1 ./autogen.sh
%configure\
	--with-plugins=all \
	--enable-python	\
	--enable-deprecations

%make_build LIBS='-lm -lgmodule-2.0'
#make_build

%install
%make_install

# locales
%find_lang %{name} --with-gnome --all-name

