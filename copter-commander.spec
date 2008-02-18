%define name copter-commander
%define version 1.8
%define release %mkrel 4

Summary: A 2d networked helicopter game
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
Patch0:  %name-makefile-destdir.patch
Patch1:  copter-commander-1.8-lvalue.patch
Source10: %name-16.png
Source11: %name-32.png
Source12: %name-48.png
License: GPL
Group: Games/Strategy
Url: http://sourceforge.net/projects/coco/
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
%patch -p0
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

%post
%{update_menus}
%if %mdkversion > 200600
%update_icon_cache hicolor
%update_icon_cache locolor
%endif

%postun
%{clean_menus}
%if %mdkversion > 200600
%clean_icon_cache hicolor
%clean_icon_cache locolor
%endif

%files
%defattr(-,root,root)
%doc DEVEL GNOME-HACKS ChangeLog INSTALL copyright
%_gamesbindir/*
%_gamesdatadir/%name
%_liconsdir/%name.png
%_iconsdir/%name.png
%_miconsdir/%name.png
%{_datadir}/applications/*.desktop
