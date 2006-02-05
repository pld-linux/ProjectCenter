Summary:	ProjectCenter - the GNUstep IDE
Summary(pl):	ProjectCenter - IDE dla ¶rodowiska GNUstep
Name:		ProjectCenter
Version:	0.4.3
Release:	1
License:	GPL
Group:		X11/Development/Tools
Source0:	ftp://ftp.gnustep.org/pub/gnustep/dev-apps/%{name}-%{version}.tar.gz
# Source0-md5:	d7751435e4a94a6d198d7fa627a634f5
Patch0:		%{name}-link.patch
URL:		http://www.gnustep.org/experience/ProjectCenter.html
BuildRequires:	gnustep-gui-devel >= 0.10.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/%{_lib}/GNUstep

%define		libcombo	gnu-gnu-gnu
%define		gsos		linux-gnu
%ifarch %{ix86}
%define		gscpu		ix86
%else
# also s/alpha.*/alpha/, but we use only "alpha" arch for now
%define		gscpu		%(echo %{_target_cpu} | sed -e 's/amd64/x86_64/;s/ppc/powerpc/')
%endif

%description
This is ProjectCenter, the GNUstep IDE (Integrated Development
Environment) which is part of the GNUstep project.

%description -l pl
To jest ProjectCenter - IDE (Integrated Development Environment -
zintegrowane ¶rodowisko programisty) dla GNUstepa, bêd±ce czê¶ci±
projektu GNUstep.

%prep
%setup -q
%patch0 -p1

%build
export GNUSTEP_MAKEFILES=%{_prefix}/System/Library/Makefiles
export GNUSTEP_TARGET_DIR=%{gscpu}/linux-gnu

%{__make} \
	OPTFLAG="%{rpmcflags}" \
	messages=yes

%install
rm -rf $RPM_BUILD_ROOT
export GNUSTEP_MAKEFILES=%{_prefix}/System/Library/Makefiles
export GNUSTEP_TARGET_DIR=%{gscpu}/linux-gnu

%{__make} install \
	GNUSTEP_INSTALLATION_DIR=$RPM_BUILD_ROOT%{_prefix}/System

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc Documentation/{ANNOUNCE,AUTHORS,ChangeLog*,README*,TODO}

%dir %{_prefix}/System/Applications/ProjectCenter.app
%attr(755,root,root) %{_prefix}/System/Applications/ProjectCenter.app/ProjectCenter
%dir %{_prefix}/System/Applications/ProjectCenter.app/Resources
%{_prefix}/System/Applications/ProjectCenter.app/Resources/*.desktop
%{_prefix}/System/Applications/ProjectCenter.app/Resources/*.gorm
%{_prefix}/System/Applications/ProjectCenter.app/Resources/*.plist
%{_prefix}/System/Applications/ProjectCenter.app/Resources/*.tiff
%dir %{_prefix}/System/Applications/ProjectCenter.app/Resources/*.bundle
%{_prefix}/System/Applications/ProjectCenter.app/Resources/*.bundle/Resources
%attr(755,root,root) %{_prefix}/System/Applications/ProjectCenter.app/Resources/*.bundle/%{gscpu}
%dir %{_prefix}/System/Applications/ProjectCenter.app/%{gscpu}
%dir %{_prefix}/System/Applications/ProjectCenter.app/%{gscpu}/%{gsos}
%dir %{_prefix}/System/Applications/ProjectCenter.app/%{gscpu}/%{gsos}/%{libcombo}
%attr(755,root,root) %{_prefix}/System/Applications/ProjectCenter.app/%{gscpu}/%{gsos}/%{libcombo}/ProjectCenter
%{_prefix}/System/Applications/ProjectCenter.app/%{gscpu}/%{gsos}/%{libcombo}/*.openapp

%dir %{_prefix}/System/Library/Frameworks/ProjectCenter.framework
%dir %{_prefix}/System/Library/Frameworks/ProjectCenter.framework/Versions
%{_prefix}/System/Library/Frameworks/ProjectCenter.framework/Versions/Current
%dir %{_prefix}/System/Library/Frameworks/ProjectCenter.framework/Versions/%{version}
%{_prefix}/System/Library/Frameworks/ProjectCenter.framework/Versions/%{version}/Headers
%{_prefix}/System/Library/Frameworks/ProjectCenter.framework/Versions/%{version}/Resources
%attr(755,root,root) %{_prefix}/System/Library/Frameworks/ProjectCenter.framework/Versions/%{version}/%{gscpu}

%{_prefix}/System/Library/Headers/%{libcombo}/ProjectCenter

%{_prefix}/System/Library/Libraries/%{gscpu}/%{gsos}/%{libcombo}/lib*.so*
