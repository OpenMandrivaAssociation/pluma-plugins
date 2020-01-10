%define url_ver %(echo %{version}|cut -d. -f1,2)
%define oname mate-text-editor-plugins

Summary:       Plugins for pluma
Name:          pluma-plugins
Version:       1.2.0
Release:       2
License:       GPLv2+
Group:         Editors 
URL:           https://github.com/cygwinports/mate-text-editor-plugins
# Git source:
Source0:       %{oname}-master.zip
Patch0:        mate-text-editor-plugins-1.2.0-mga-remove-obsolated-plugins.patch

BuildRequires: intltool
BuildRequires: mate-common
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(dbus-python)
BuildRequires: pkgconfig(vte)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gtk+-2.0)
BuildRequires: pkgconfig(pluma) >= 1.6.0
BuildRequires: pkgconfig(pygobject-2.0)
BuildRequires: pkgconfig(pygtk-2.0)
BuildRequires: pkgconfig(pygtksourceview-2.0)
BuildRequires: python

Requires:      pluma >= 1.6.0
Requires:      python-gtksourceview

%rename %{oname}

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

%prep
%setup -q -n %{oname}-master
%autopatch -p1

%build
NOCONFIGURE=1 ./autogen.sh
%configure2_5x --with-plugins=all

%make LIBS='-lm -lgmodule-2.0'

%install

%makeinstall_std

%{find_lang} %{name}

%files  -f %{name}.lang
%doc README COPYING AUTHORS
%{_datadir}/pluma/plugins/*
%{_libdir}/pluma/plugins/*

