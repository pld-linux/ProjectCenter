Summary:	ProjectCenter - the GNUstep IDE
Summary(pl):	ProjectCenter - IDE dla ¶rodowiska GNUstep
Name:		ProjectCenter
Version:	0.3.5
Release:	0.1
License:	GPL
Group:		X11/Development/Tools
Source0:	ftp://ftp.gnustep.org/pub/gnustep/dev-apps/%{name}-%{version}.tar.gz
# Source0-md5:	a8a6f17ea9d2cd1bc1ac7dea53e350c6
URL:		http://www.gnustep.org/experience/ProjectCenter.html
BuildRequires:	gnustep-extensions-devel
BuildRequires:	gnustep-gui-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _prefix         /usr/lib/GNUstep

%define		libcombo	gnu-gnu-gnu
%define		gsos		linux-gnu
%ifarch %{ix86}
%define		gscpu		ix86
%else
# also s/alpha.*/alpha/, but we use only "alpha" arch for now
%define		gscpu		%{_target_cpu}
%endif

%description
This is ProjectCenter, the GNUstep IDE (Integrated Development
Environment) which is part of the GNUstep project.

%description -l pl
To jest ProjectCenter - IDE (Integrated Development Environment -
zintegrowane ¶rodowisko programisty) dla GNUstepa, bêd±ce czê¶ci±
projektu GNUstep.

%prep
%setup -q -n %{name}

%build
. %{_prefix}/System/Library/Makefiles/GNUstep.sh
%{__make} \
	OPTFLAG="%{rpmcflags}" \
	messages=yes

%install
rm -rf $RPM_BUILD_ROOT
. %{_prefix}/System/Library/Makefiles/GNUstep.sh

%{__make} install \
	GNUSTEP_INSTALLATION_DIR=$RPM_BUILD_ROOT%{_prefix}/System

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ANNOUNCE AUTHORS ChangeLog README* TODO

%dir %{_prefix}/System/Applications/ProjectCenter.app
%attr(755,root,root) %{_prefix}/System/Applications/ProjectCenter.app/ProjectCenter
%dir %{_prefix}/System/Applications/ProjectCenter.app/Resources
%{_prefix}/System/Applications/ProjectCenter.app/Resources/*.desktop
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

%{_prefix}/System/Library/Headers/ProjectCenter

%{_prefix}/System/Library/Libraries/%{gscpu}/%{gsos}/%{libcombo}/lib*.so*
