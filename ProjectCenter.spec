Summary:	ProjectCenter - the GNUstep IDE
Summary(pl.UTF-8):	ProjectCenter - IDE dla środowiska GNUstep
Name:		ProjectCenter
Version:	0.5.0
Release:	1
License:	GPL
Group:		X11/Development/Tools
Source0:	ftp://ftp.gnustep.org/pub/gnustep/dev-apps/%{name}-%{version}.tar.gz
# Source0-md5:	acaabf63b627246f853bdd14d2455e4a
Patch0:		%{name}-link.patch
URL:		http://www.gnustep.org/experience/ProjectCenter.html
BuildRequires:	gnustep-gui-devel >= 0.10.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is ProjectCenter, the GNUstep IDE (Integrated Development
Environment) which is part of the GNUstep project.

%description -l pl.UTF-8
To jest ProjectCenter - IDE (Integrated Development Environment -
zintegrowane środowisko programisty) dla GNUstepa, będące częścią
projektu GNUstep.

%prep
%setup -q
#%patch0 -p1

%build
export GNUSTEP_MAKEFILES=%{_datadir}/GNUstep/Makefiles
export GNUSTEP_FLATTENED=yes

%{__make} \
	OPTFLAG="%{rpmcflags}" \
	messages=yes

%install
rm -rf $RPM_BUILD_ROOT
export GNUSTEP_MAKEFILES=%{_datadir}/GNUstep/Makefiles
export GNUSTEP_FLATTENED=yes

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc Documentation/{ANNOUNCE,AUTHORS,ChangeLog*,README*,TODO}

%dir %{_prefix}/lib/GNUstep/Applications/ProjectCenter.app
%attr(755,root,root) %{_prefix}/lib/GNUstep/Applications/ProjectCenter.app/ProjectCenter
%dir %{_prefix}/lib/GNUstep/Applications/ProjectCenter.app/Resources
%{_prefix}/lib/GNUstep/Applications/ProjectCenter.app/Resources/*.desktop
%{_prefix}/lib/GNUstep/Applications/ProjectCenter.app/Resources/*.plist
%{_prefix}/lib/GNUstep/Applications/ProjectCenter.app/Resources/*.tiff
%dir %{_prefix}/lib/GNUstep/Applications/ProjectCenter.app/Resources/*.editor
%{_prefix}/lib/GNUstep/Applications/ProjectCenter.app/Resources/*.project
%attr(755,root,root) %{_prefix}/lib/GNUstep/Applications/ProjectCenter.app/ProjectCenter

%dir %{_prefix}/lib/GNUstep/Frameworks/ProjectCenter.framework
%dir %{_prefix}/lib/GNUstep/Frameworks/ProjectCenter.framework/Versions
%{_prefix}/lib/GNUstep/Frameworks/ProjectCenter.framework/Versions/Current
%dir %{_prefix}/lib/GNUstep/Frameworks/ProjectCenter.framework/Versions/%{version}
%{_prefix}/lib/GNUstep/Frameworks/ProjectCenter.framework/Versions/%{version}/Headers
%{_prefix}/lib/GNUstep/Frameworks/ProjectCenter.framework/Versions/%{version}/Resources
%attr(755,root,root) %{_prefix}/lib/GNUstep/Frameworks/ProjectCenter.framework/Versions/%{version}

%{_includedir}/ProjectCenter

%attr(755,root,root) %{_prefix}/lib/lib*.so*
%attr(755,root,root) %{_bindir}/ProjectCenter
%{_libdir}/GNUstep/Applications/ProjectCenter.app/Resources/English.lproj/*.gorm
%{_libdir}/GNUstep/Applications/ProjectCenter.app/Resources/*.editor
%{_libdir}/GNUstep/Applications/ProjectCenter.app/Resources/*.parser
%{_libdir}/GNUstep/Frameworks/ProjectCenter.framework/Headers
%{_libdir}/GNUstep/Frameworks/ProjectCenter.framework/ProjectCenter
%{_libdir}/GNUstep/Frameworks/ProjectCenter.framework/Resources
%{_libdir}/GNUstep/Frameworks/ProjectCenter.framework/libProjectCenter.so
