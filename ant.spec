# TODO: consider using external xerces-j
#
# Conditional build:
%bcond_with	basic_functionality	# generates package with only
					# basic functionality, i.e. no deps
%bcond_without	junit			# build without (commonly used) junit support
#
Summary:	ant build tool for Java
Summary(fr):	Outil de compilation pour java
Summary(it):	Tool per la compilazione di programmi java
Summary(pl):	ant - narzêdzie do budowania w Javie
Name:		jakarta-ant
Version:	1.6.5
%if %{with basic_functionality}
Release:	0.basic.1
%else
Release:	1
%endif
License:	Apache
Group:		Development/Languages/Java
Source0:	http://www.apache.org/dist/ant/source/apache-ant-%{version}-src.tar.bz2
# Source0-md5:	80a7ad191c40b7d8c82533524b282b6b
Patch0:		%{name}-ANT_HOME.patch
URL:		http://ant.apache.org/
BuildRequires:	jdk
%{?with_junit:BuildRequires:	junit}
%if %{without basic_functionality}
BuildRequires:	antlr
BuildRequires:	beanshell
BuildRequires:	bsf >= 2.3.0
BuildRequires:	jaf
BuildRequires:	jakarta-bcel
BuildRequires:	jakarta-commons-logging
BuildRequires:	jakarta-commons-net >= 1.2.2
BuildRequires:	jakarta-log4j
BuildRequires:	jakarta-oro >= 2.0.7
BuildRequires:	jakarta-regexp >= 1.3
BuildRequires:	javamail
BuildRequires:	jsch
BuildRequires:	netrexx
BuildRequires:	xalan-j
BuildRequires:	rhino >= 1.5R3
BuildRequires:	xml-commons-resolver >= 1.1
BuildRequires:	rpm-pythonprov
# TODO: icontract, jai, jdepend, starteam, stylebook, vaj, weblogic, xslp
%endif
Requires:	jdk
%{?with_junit:Provides:	jakarta-ant(junit) = %{version}}
Provides:	jaxp_parser_impl
Provides:	xerces-j = 2.6.2
Obsoletes:	xerces-j
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Platform-independent build tool for Java. Ant is a Java based build
system. Ant is used by apache jakarta & xml projects.

%description -l fr
Ant est un outil de compilation multi-plateformes pour java. Il est
utilisé par les projets apache-jakarta et apache-xml.

%description -l it
Ant e' un tool indipendente dalla piattaforma creato per faciltare la
compilazione di programmi java.
Allo stato attuale viene utilizzato dai progetti apache jakarta ed
apache xml.

%description -l pl
Niezale¿ne od platformy narzêdzie do budowania w Javie. Ant jest
u¿ywany przez projekty apache jakarta i xml.

%package doc
Summary:	Online manual for ant
Summary(pl):	Dokumentacja online do ant
Group:		Documentation
Obsoletes:	ant-doc

%description doc
Documentation for ant, platform-independent build tool for Java. Used
by Apache Group for jakarta and xml projects.

%description doc -l pl
Dokumentacja do ant - niezale¿nego od platformy narzêdzia do budowania
w Javie.

%prep
%setup -q -n apache-ant-%{version}
%patch0 -p1

%build
export JAVA_HOME=%{_libdir}/java
# the same is probably needed for all other optional packages
%{?with_junit:export CLASSPATH=%{_javadir}/junit.jar}
sh build.sh

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_javadir}}

install dist/bin/{ant,antRun,runant.pl,runant.py} $RPM_BUILD_ROOT%{_bindir}
install dist/lib/ant-*.jar $RPM_BUILD_ROOT%{_javadir}
install dist/lib/ant.jar $RPM_BUILD_ROOT%{_javadir}/ant-%{version}.jar
ln -sf ant-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/ant.jar

# xerces-j 2.6.2
install dist/lib/x*.jar $RPM_BUILD_ROOT%{_javadir}
ln -sf xercesImpl.jar $RPM_BUILD_ROOT%{_javadir}/jaxp_parser_impl.jar

# this looks strange
ln -sf . $RPM_BUILD_ROOT%{_javadir}/lib

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc KEYS LICENSE README WHATSNEW
%attr(755,root,root) %{_bindir}/ant
%attr(755,root,root) %{_bindir}/antRun
%attr(755,root,root) %{_bindir}/runant.pl
%attr(755,root,root) %{_bindir}/runant.py
%{_javadir}/lib
%{_javadir}/*.jar

%files doc
%defattr(644,root,root,755)
%doc docs
