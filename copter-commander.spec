%define name copter-commander
%define version 1.8
%define release 10

Summary: A 2d networked helicopter game
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
Patch0:  %{name}-makefile-destdir.patch
Patch1:  copter-commander-1.8-lvalue.patch
Source10: %name-16.png
Source11: %name-32.png
Source12: %name-48.png
License: GPLv2+
Group: Games/Arcade
Url: https://sourceforge.net/projects/coco/
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: libgnome-devel
BuildRequires: libtiff-devel
BuildRequires: libgtkglarea-devel = 1.2.3 

%description
A unique blend of arcade action and real time strategy, Copter Commander
is fun for novices but surprisingly deep. It supports one to four players 
via Internet play and is based on the game design of Rescue Raiders/Armor
Alley.

%prep
%setup -q
%patch0 -p0
%patch1 -p0 -b .lvalue

%build

%make \
    CFLAGS="$RPM_OPT_FLAGS" \
    COCO_OPTIMIZATION_FLAGS="-O2" \
    COCO_INSTALL_DIRECTORY=%_prefix \
    COCO_BIN_DIRECTORY=%_gamesbindir \
    COCO_SHARE_DIRECTORY=%_gamesdatadir/%name/%version

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall_std \
    COCO_INSTALL_DIRECTORY=%_prefix \
    COCO_BIN_DIRECTORY=%_gamesbindir \
    COCO_SHARE_DIRECTORY=%_gamesdatadir/%name/%version

(
cd %buildroot%_gamesbindir
ln -s glx-%name %name-glx
)

mkdir -p %buildroot{%_miconsdir,%_iconsdir,%_liconsdir}
cp %SOURCE10 %buildroot%_miconsdir/%name.png
cp %SOURCE11 %buildroot%_iconsdir/%name.png
cp %SOURCE12 %buildroot%_liconsdir/%name.png


mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Copter Commander
Comment=Copter Commander
Exec=%_gamesbindir/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Game;ArcadeGame;X-MandrivaLinux-MoreApplications-Games-Arcade;
EOF

cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}-glx.desktop << EOF
[Desktop Entry]
Name=Copter-Commander Glx
Comment=Copter Commander OpenGL
Exec=%_gamesbindir/glx-%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Game;ArcadeGame;X-MandrivaLinux-MoreApplications-Games-Arcade;
EOF

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root)
%doc DEVEL GNOME-HACKS ChangeLog INSTALL copyright
%_gamesbindir/*
%_gamesdatadir/%name
%_liconsdir/%name.png
%_iconsdir/%name.png
%_miconsdir/%name.png
%{_datadir}/applications/*.desktop


%changelog
* Thu May 14 2009 Samuel Verschelde <stormi@mandriva.org> 1.8-8mdv2010.0
+ Revision: 375634
- fix Licence
- fix Group (#49502)
- fix spec file (Patch0 was not applied)

* Fri Aug 15 2008 Götz Waschk <waschk@mandriva.org> 1.8-7mdv2009.0
+ Revision: 272473
- remove icon cache call, locolor has no icon theme (bug #42852)

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 1.8-6mdv2009.0
+ Revision: 243637
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Mon Feb 18 2008 Olivier Thauvin <nanardon@mandriva.org> 1.8-4mdv2008.1
+ Revision: 172117
- create directory for icons
- kill partial changelog rest

  + Thierry Vignaud <tv@mandriva.org>
    - drop old menu
    - kill re-definition of %%buildroot on Pixel's request
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Mon Jul 17 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 2006-07-17 09:54:07 (41417)
- add patch1

* Mon Jul 17 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 2006-07-17 09:53:28 (41416)
- fix build (patch1)
- xdg menu
- fix old menu section

* Mon Jul 17 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 2006-07-17 09:32:28 (41415)
Import copter-commander

* Thu Jan 08 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 1.8-2mdk
- DIRM fix
- set RPM_OPT_FLAGS

* Mon Oct 13 2003 Olivier Thauvin <thauvin@aerov.jussieu.fr> 1.8-1mdk
- 1st mdk package

