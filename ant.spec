Summary:	ant build tool for Java
Summary(pl):	ant - narzêdzie do budowania w Javie
Name:		jakarta-ant
Version:	1.5.4
Release:	1
License:	Apache
Group:		Development/Languages/Java
Source0:	http://www.apache.org/dist/ant/source/apache-ant-%{version}-src.tar.bz2
# Source0-md5:	bfac23721c24e77d0b1c383200327ff6
Patch0:		%{name}-ANT_HOME.patch
URL:		http://ant.apache.org/
BuildRequires:	jdk
Requires:	jdk
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javaclassdir	%{_datadir}/java

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
	JAVA_HOME=/usr/lib/java
fi
export JAVA_HOME

sh build.sh

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_javaclassdir}
install bootstrap/bin/{ant,antRun,runant.pl,runant.py} $RPM_BUILD_ROOT%{_bindir}
install bootstrap/lib/optional.jar $RPM_BUILD_ROOT%{_javaclassdir}
install bootstrap/lib/ant.jar $RPM_BUILD_ROOT%{_javaclassdir}/ant-%{version}.jar
ln -sf ant-%{version}.jar $RPM_BUILD_ROOT%{_javaclassdir}/ant.jar

# this looks strange
ln -sf . $RPM_BUILD_ROOT%{_javaclassdir}/lib

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc KEYS LICENSE README WHATSNEW
%attr(755,root,root) %{_bindir}/ant
%attr(755,root,root) %{_bindir}/antRun
%attr(755,root,root) %{_bindir}/runant.pl
%attr(755,root,root) %{_bindir}/runant.py
%{_javaclassdir}/lib
%{_javaclassdir}/*.jar

%files doc
%defattr(644,root,root,755)
%doc docs
