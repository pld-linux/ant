Summary:	ant build tool for Java
Summary(pl):	ant - narzêdzie do budowania w Javie
Name:		jakarta-ant
Version:	1.4.1
Release:	1
License:	Apache Software License
Group:		Development/Languages/Java
Group(de):	Entwicklung/Sprachen/Java
Group(pl):	Programowanie/Jêzyki/Java
Source0:	http://jakarta.apache.org/builds/%{name}/release/v%{version}/src/%{name}-%{version}-src.tar.gz
Source1:	http://jakarta.apache.org/builds/%{name}/release/v%{version}/bin/%{name}-%{version}-optional.jar
URL:		http://jakarta.apache.org/ant/
BuildRequires:	ibm-java-sdk
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javalibdir	/usr/share/java

%description
Platform-independent build tool for Java. Ant is a Java based build
system. Ant is used by apache jakarta & xml projects.

%description -l pl
Niezale¿ne od platformy narzêdzie do budowania w Javie. Ant jest
u¿ywany przez projekty apache jakarta i xml.

%package doc
Summary:	Online manual for ant
Summary(pl):	Dokumentacja online do ant
Group:		Documentation
Group(de):	Dokumentation
Group(es):	Documentación
Group(pl):	Dokumentacja
Obsoletes:	ant-doc

%description doc
Documentation for ant, platform-independent build tool for Java. Used
by Apache Group for jakarta and xml projects.

%description doc -l pl
Dokumentacja do ant - niezale¿nego od platformy narzêdzia do budowania
w Javie.

%prep
%setup -q

%build
JAVA_HOME="%{_libdir}/IBMJava2-13"
CLASSPATH="$CLASSPATH:$JAVA_HOME/jre/lib/rt.jar"
CLASSPATH="$CLASSPATH:$RPM_BUILD_DIR/%{name}-%{version}/%{name}-1.3-optional.jar"
export JAVA_HOME CLASSPATH

cp -f %{SOURCE1} .
sh build.sh

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_javalibdir}
install bootstrap/bin/{ant,antRun,runant.pl,runant.py} $RPM_BUILD_ROOT%{_bindir}
install bootstrap/lib/*.jar $RPM_BUILD_ROOT%{_javalibdir}

ln -sf %{_javalibdir} $RPM_BUILD_ROOT%{_javalibdir}/lib

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
