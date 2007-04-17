%include	/usr/lib/rpm/macros.java
Summary:	ant build tool for Java
Summary(pl):	ant - narzêdzie do budowania w Javie
Name:		jakarta-ant
Version:	1.5.1
Release:	0.1
License:	Apache
Group:		Development/Languages/Java
Source0:	http://archive.apache.org/dist/ant/source/%{name}-%{version}-src.zip
# Source0-md5:	9559f9a3b6f110dd9f297e604d00c22c
URL:		http://jakarta.apache.org/ant/
BuildRequires:	jdk
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	jdk
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javadir	/usr/share/java

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
%setup -q

%build
export JAVA_HOME="%{java_home}"

sh build.sh

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_javadir}
install bootstrap/bin/{ant,antRun,runant.pl,runant.py} $RPM_BUILD_ROOT%{_bindir}
install bootstrap/lib/*.jar $RPM_BUILD_ROOT%{_javadir}

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
