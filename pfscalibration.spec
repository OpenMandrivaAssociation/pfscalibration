%define name     pfscalibration
%define version  1.3
%define release %mkrel 3

Summary: Photometric Calibration of HDR and LDR Cameras
Name:           %{name}
Version:        %{version}
Release:        %{release}
License: GPL
Group: Graphics
Source: http://heanet.dl.sourceforge.net/sourceforge/pfstools/%{name}-%{version}.tar.bz2
URL: http://www.mpi-inf.mpg.de/resources/hdr/calibration/
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: pfstools-devel autoconf
Requires: jhead

%description
A photographic camera with a standard CCD sensor is able to acquire an image
with simultaneous dynamic range of not more than 1:1000. The basic idea to
create an image with a higher dynamic range is to combine multiple images with
different exposure settings, thus making use of available sequential dynamic
range.

%prep
%setup -q

%build
%configure
%make

%install
%makeinstall

rm -f %{buildroot}/usr/share/man/man1/pfscat.1
rm -f %{buildroot}/usr/bin/pfscat

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc AUTHORS COPYING INSTALL README TODO
%{_bindir}/*
%{_mandir}/man?/*

