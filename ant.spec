# TODO: consider using external xerces-j
Summary:	ant build tool for Java
Summary(fr):	Outil de compilation pour java
Summary(it):	Tool per la compilazione di programmi java
Summary(pl):	ant - narzêdzie do budowania w Javie
Name:		jakarta-ant
Version:	1.6.2
Release:	1
License:	Apache
Group:		Development/Languages/Java
Source0:	http://www.apache.org/dist/ant/source/apache-ant-%{version}-src.tar.bz2
# Source0-md5:	83c3adefdbf90bcbc4b804d4c55c0778
#Source0:	http://cvs.apache.org/dist/ant/v%{version}%{_beta}/src/apache-ant-%{version}%{_beta}-src.tar.bz2
Patch0:		%{name}-ANT_HOME.patch
URL:		http://ant.apache.org/
BuildRequires:	jdk
Requires:	jdk
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
if [ -z "$JAVA_HOME" ]; then
	JAVA_HOME=%{_libdir}/java
fi
export JAVA_HOME
sh build.sh

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_javadir}}

install bootstrap/bin/{ant,antRun,runant.pl,runant.py} $RPM_BUILD_ROOT%{_bindir}
install bootstrap/lib/ant-*.jar $RPM_BUILD_ROOT%{_javadir}
install bootstrap/lib/ant.jar $RPM_BUILD_ROOT%{_javadir}/ant-%{version}.jar
ln -sf ant-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/ant.jar

# xerces-j 2.6.2
install bootstrap/lib/xercesImpl.jar $RPM_BUILD_ROOT%{_javadir}
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
