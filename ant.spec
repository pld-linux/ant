Summary:	ant build tool for Java
Summary(pl):	ant - narzędzie do budowania w Javie
Name:		jakarta-ant
Version:	1.5.1
Release:	1
License:	Apache
Group:		Development/Languages/Java
Source0:	http://jakarta.apache.org/builds/%{name}/release/v%{version}/src/%{name}-%{version}-src.tar.gz
Patch0:		%{name}-ANT_HOME.patch
URL:		http://jakarta.apache.org/ant/
BuildRequires:	jdk
Requires:	jdk
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javalibdir	/usr/share/java

%description
Platform-independent build tool for Java. Ant is a Java based build
system. Ant is used by apache jakarta & xml projects.

%description -l pl
Niezależne od platformy narzędzie do budowania w Javie. Ant jest
używany przez projekty apache jakarta i xml.

%package doc
Summary:	Online manual for ant
Summary(pl):	Dokumentacja online do ant
Group:		Documentation
Obsoletes:	ant-doc

%description doc
Documentation for ant, platform-independent build tool for Java. Used
by Apache Group for jakarta and xml projects.

%description doc -l pl
Dokumentacja do ant - niezależnego od platformy narzędzia do budowania
w Javie.

%prep
%setup -q
%patch0 -p1

%build
if [ -z "$JAVA_HOME" ]; then
	JAVA_HOME=/usr/lib/java
fi
export JAVA_HOME

sh build.sh

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_javalibdir}
install bootstrap/bin/{ant,antRun,runant.pl,runant.py} $RPM_BUILD_ROOT%{_bindir}
install bootstrap/lib/*.jar $RPM_BUILD_ROOT%{_javalibdir}

# this looks strange
ln -sf . $RPM_BUILD_ROOT%{_javalibdir}/lib

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc KEYS LICENSE README WHATSNEW
%attr(755,root,root) %{_bindir}/ant
%attr(755,root,root) %{_bindir}/antRun
%attr(755,root,root) %{_bindir}/runant.pl
%attr(755,root,root) %{_bindir}/runant.py
%{_javalibdir}/lib
%{_javalibdir}/*.jar

%files doc
%defattr(644,root,root,755)
%doc docs
