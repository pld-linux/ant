Summary: 	ant build tool for java
Summary(pl):	ant narzedzie do budowania w javie
Name:		jakarta-ant
Version:	1.4
Release:	1
License:	Apache Software License
Group:		Development/Languages/Java
Group(de):	Entwicklung/Sprachen/Java
Group(pl):	Programowanie/Jêzyki/Java
Source0:	http://jakarta.apache.org/builds/%{name}/release/v%{version}/src/%{name}-%{version}-src.tar.gz
Source1:	%{name}-1.3-optional.jar
URL:		http://jakarta.apache.org
BuildRequires:	ibm-java-sdk
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javalibdir	/usr/share/java

%description
Platform-independent build tool for java.
Ant is a Java based build system
Ant is used by apache jakarta&xml projects.

%package doc
Group: 			Documentation
Requires: 		webserver
Summary: 		Online manual for ant
Obsoletes:		ant-doc

%description doc
Documentation for ant, Platform-independent build tool for java.
Used by Apache Group for jakarta and xml projects.

%prep
%setup -q

%build
export JAVA_HOME="/usr/lib/IBMJava2-13"
export CLASSPATH="$CLASSPATH:$JAVA_HOME/jre/lib/rt.jar"
export CLASSPATH="$CLASSPATH:$RPM_BUILD_DIR/%{name}-%{version}/%{name}-1.3-optional.jar"
cp %{SOURCE1} .
sh build.sh

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/%{_bindir}
install -d $RPM_BUILD_ROOT/%{_javalibdir}
cp bootstrap/bin/{ant,antRun,runant.pl,runant.py} $RPM_BUILD_ROOT/%{_bindir}
cp bootstrap/lib/*.jar $RPM_BUILD_ROOT/%{_javalibdir}

ln -sf %{_javalibdir} $RPM_BUILD_ROOT/%{_javalibdir}/lib

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
