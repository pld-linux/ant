Summary:	ant build tool for Java
Summary(pl):	ant - narzędzie do budowania w Javie
Name:		jakarta-ant
Version:	1.4.1
Release:	2
License:	Apache Software License
Group:		Development/Languages/Java
Source0:	http://jakarta.apache.org/builds/%{name}/release/v%{version}/src/%{name}-%{version}-src.tar.gz
Source1:	http://jakarta.apache.org/builds/%{name}/release/v%{version}/bin/%{name}-%{version}-optional.jar
Patch0:		%{name}-ANT_HOME.patch
URL:		http://jakarta.apache.org/ant/
BuildRequires:	jdk
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
JAVA_HOME="%{_libdir}/java"
CLASSPATH="$JAVA_HOME/jre/lib/rt.jar:%{SOURCE1}"
export JAVA_HOME CLASSPATH

cp -f %{SOURCE1} .
sh build.sh

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_javalibdir}
install bootstrap/bin/{ant,antRun,runant.pl,runant.py} $RPM_BUILD_ROOT%{_bindir}
install bootstrap/lib/*.jar $RPM_BUILD_ROOT%{_javalibdir}

# this looks strange
ln -sf . $RPM_BUILD_ROOT%{_javalibdir}/lib

gzip -9nf KEYS LICENSE README WHATSNEW

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/ant
%attr(755,root,root) %{_bindir}/antRun
%attr(755,root,root) %{_bindir}/runant.pl
%attr(755,root,root) %{_bindir}/runant.py
%{_javalibdir}/lib
%{_javalibdir}/*.jar

%files doc
%defattr(644,root,root,755)
%doc docs
