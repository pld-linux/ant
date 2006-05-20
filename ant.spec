%include /usr/lib/rpm/macros.java
#
# TODO:
#	- prepare all BR and test the full build
# Conditional build:
%bcond_with	bootstrap	# minimal build for bootstrap
%bcond_without	antlr		# disable building antlr optional task(s)
%bcond_without	apache_bcel	# disable building apache-bcel optional task(s)
%bcond_without	apache_bsf	# disable building apache-bsf optional task(s)
%bcond_without	apache_log4j	# disable building apache-log4j optional task(s)
%bcond_without	apache_oro	# disable building apache-oro optional task(s)
%bcond_without	apache_regexp	# disable building apache-regexp optional task(s)
%bcond_without	apache_resolver	# disable building apache-resolver optional task(s)
%bcond_without	commons-logging	# disable building commons-logging optional task(s)
%bcond_without	commons-net	# disable building commons-net optional task(s)
%bcond_with	jai		# enable building jai optional task(s)
%bcond_without	javamail	# disable building javamail optional task(s)
%bcond_with	jdepend		# enable building jdepend optional task(s)
%bcond_without	jsch		# disable building jsch optional task(s)
%bcond_without	junit		# disable building junit optional task(s)
#
%if %{with bootstrap}
%undefine	with_antlr
%undefine	with_apache_bcel
%undefine	with_apache_bsf
%undefine	with_apache_log4j
%undefine	with_apache_oro
%undefine	with_apache_regexp
%undefine	with_apache_resolver
%undefine	with_commons_logging
%undefine	with_commons_net
%undefine	with_javamail
%undefine	with_jsch
%endif
#
#
Summary:	Ant build tool for Java
Summary(fr):	Outil de compilation pour java
Summary(it):	Tool per la compilazione di programmi java
Summary(pl):	Ant - narzêdzie do budowania w Javie
Name:		ant
Version:	1.6.5
Release:	1.1
License:	Apache
Group:		Development/Languages/Java
Source0:	http://www.apache.org/dist/ant/source/apache-%{name}-%{version}-src.tar.bz2
# Source0-md5:	80a7ad191c40b7d8c82533524b282b6b
Source1:	%{name}.conf
Patch0:		%{name}-ant_d.patch
URL:		http://ant.apache.org/
%{?with_antlr:BuildRequires:	antlr}
%{?with_bsf:BuildRequires:	beanshell}
%{?with_bsf:BuildRequires:	bsf}
%{?with_bcel:BuildRequires:	jakarta-bcel}
%{?with_commons_logging:BuildRequires:	jakarta-commons-logging}
%{?with_commons_net:BuildRequires:	jakarta-commons-net}
%{?with_apache_log4j:BuildRequires:	jakarta-log4j}
%{?with_apache_oro:BuildRequires:	jakarta-oro}
%{?with_apache_regexp:BuildRequires:	jakarta-regexp}
%{?with_javamail:BuildRequires:	jaf}
%{?with_javamail:BuildRequires:	javamail}
BuildRequires:	jdk
%{?with_jsch:BuildRequires:	jsch}
%{?with_junit:BuildRequires:	junit}
%{?with_bsf:BuildRequires:	jython}
BuildRequires:	jaxp_parser_impl
BuildRequires:	jpackage-utils
BuildRequires:	rpm-pythonprov
Requires:	jdk
Requires:	jpackage-utils
Obsoletes:	jakarta-ant
BuildArch:	noarch
ExclusiveArch:	i586 i686 pentium3 pentium4 athlon %{x8664} noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%define 	ant_home 	%{_datadir}/ant

%description
Platform-independent build tool for Java. Ant is a Java based build
system. Ant is used by apache jakarta & xml projects.

%description -l fr
Ant est un outil de compilation multi-plateformes pour java. Il est
utilisé par les projets apache-jakarta et apache-xml.

%description -l it
Ant e' un tool indipendente dalla piattaforma creato per faciltare la
compilazione di programmi java. Allo stato attuale viene utilizzato
dai progetti apache jakarta ed apache xml.

%description -l pl
Niezale¿ne od platformy narzêdzie do budowania w Javie. Ant jest
u¿ywany przez projekty apache jakarta i xml.

%package antlr
Summary:	Optional antlr tasks for %{name}
Group:		Development/Languages/Java
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	antlr
Provides:	ant-antlr = %{epoch}:%{version}-%{release}
Conflicts:	ant-optional-clean, ant-optional-full

%description antlr
Optional antlr tasks for %{name}.

%description antlr -l fr
Taches antlr optionelles pour %{name}.

%package apache-bsf
Summary:	Optional apache bsf tasks for %{name}
Group:		Development/Languages/Java
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	bsf
Provides:	ant-apache-bsf = %{epoch}:%{version}-%{release}
Conflicts:	ant-optional-clean, ant-optional-full

%description apache-bsf
Optional apache bsf tasks for %{name}.

%description apache-bsf -l fr
Taches apache bsf optionelles pour %{name}.

%package apache-resolver
Summary:	Optional apache resolver tasks for %{name}
Group:		Development/Languages/Java
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	xml-commons-resolver
Provides:	ant-apache-resolver = %{epoch}:%{version}-%{release}
Conflicts:	ant-optional-clean, ant-optional-full

%description apache-resolver
Optional apache resolver tasks for %{name}.

%description apache-resolver -l fr
Taches apache resolver optionelles pour %{name}.

%package commons-logging
Summary:	Optional commons logging tasks for %{name}
Group:		Development/Languages/Java
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	jakarta-commons-logging
Provides:	ant-commons-logging = %{epoch}:%{version}-%{release}
Conflicts:	ant-optional-clean, ant-optional-full

%description commons-logging
Optional commons logging tasks for %{name}.

%description commons-logging -l fr
Taches commons logging optionelles pour %{name}.

%package commons-net
Summary:	Optional commons net tasks for %{name}
Group:		Development/Languages/Java
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	jakarta-commons-net
Provides:	ant-commons-net = %{epoch}:%{version}-%{release}
Conflicts:	ant-optional-clean, ant-optional-full

%description commons-net
Optional commons net tasks for %{name}.

%description commons-net -l fr
Taches commons net optionelles pour %{name}.

%package jai
Summary:	Optional jai tasks for %{name}
Group:		Development/Languages/Java
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	jai
Provides:	ant-jai = %{epoch}:%{version}-%{release}
Conflicts:	ant-optional-clean, ant-optional-full

%description jai
Optional jai tasks for %{name}.

%description jai -l fr
Taches jai optionelles pour %{name}.

%package apache-bcel
Summary:	Optional apache bcel tasks for %{name}
Group:		Development/Languages/Java
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	bcel
Provides:	ant-apache-bcel = %{epoch}:%{version}-%{release}
Provides:	ant-jakarta-bcel = %{epoch}:%{version}-%{release}
Obsoletes:	ant-jakarta-bcel
Conflicts:	ant-optional-clean, ant-optional-full

%description apache-bcel
Optional apache bcel tasks for %{name}.

%description apache-bcel -l fr
Taches apache bcel optionelles pour %{name}.

%package apache-log4j
Summary:	Optional apache log4j tasks for %{name}
Group:		Development/Languages/Java
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	log4j
Provides:	ant-apache-log4j = %{epoch}:%{version}-%{release}
Provides:	ant-jakarta-log4j = %{epoch}:%{version}-%{release}
Obsoletes:	ant-jakarta-log4j
Conflicts:	ant-optional-clean, ant-optional-full

%description apache-log4j
Optional apache log4j tasks for %{name}.

%description apache-log4j -l fr
Taches apache log4j optionelles pour %{name}.

%package apache-oro
Summary:	Optional apache oro tasks for %{name}
Group:		Development/Languages/Java
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	oro
Provides:	ant-apache-oro = %{epoch}:%{version}-%{release}
Provides:	ant-jakarta-oro = %{epoch}:%{version}-%{release}
Obsoletes:	ant-jakarta-oro
Conflicts:	ant-optional-clean, ant-optional-full

%description apache-oro
Optional apache oro tasks for %{name}.

%description apache-oro -l fr
Taches apache oro optionelles pour %{name}.

%package apache-regexp
Summary:	Optional apache regexp tasks for %{name}
Group:		Development/Languages/Java
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	regexp
Provides:	ant-apache-regexp = %{epoch}:%{version}-%{release}
Provides:	ant-jakarta-regexp = %{epoch}:%{version}-%{release}
Obsoletes:	ant-jakarta-regexp
Conflicts:	ant-optional-clean, ant-optional-full

%description apache-regexp
Optional apache regexp tasks for %{name}.

%description apache-regexp -l fr
Taches apache regexp optionelles pour %{name}.

%package javamail
Summary:	Optional javamail tasks for %{name}
Group:		Development/Languages/Java
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	jaf >= 0:1.0.1-5jpp
Requires:	javamail >= 0:1.2-5jpp
Provides:	ant-javamail = %{epoch}:%{version}-%{release}
Conflicts:	ant-optional-clean, ant-optional-full

%description javamail
Optional javamail tasks for %{name}.

%description javamail -l fr
Taches javamail optionelles pour %{name}.

%package jdepend
Summary:	Optional jdepend tasks for %{name}
Group:		Development/Languages/Java
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	jdepend
Provides:	ant-jdepend = %{epoch}:%{version}-%{release}
Conflicts:	ant-optional-clean, ant-optional-full

%description jdepend
Optional jdepend tasks for %{name}.

%description jdepend -l fr
Taches jdepend optionelles pour %{name}.

%package jmf
Summary:	Optional jmf tasks for %{name}
Group:		Development/Languages/Java
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	ant-jmf = %{epoch}:%{version}-%{release}
Conflicts:	ant-optional-clean, ant-optional-full

%description jmf
Optional jmf tasks for %{name}.

%description jmf -l fr
Taches jmf optionelles pour %{name}.

%package jsch
Summary:	Optional jsch tasks for %{name}
Group:		Development/Languages/Java
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	jsch
Provides:	ant-jsch = %{epoch}:%{version}-%{release}
Conflicts:	ant-optional-clean, ant-optional-full

%description jsch
Optional jsch tasks for %{name}.

%description jsch -l fr
Taches jsch optionelles pour %{name}.

%package junit
Summary:	Optional junit tasks for %{name}
Group:		Development/Languages/Java
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	junit
Provides:	ant-junit = %{epoch}:%{version}-%{release}
Conflicts:	ant-optional-clean, ant-optional-full

%description junit
Optional junit tasks for %{name}.

%description junit -l fr
Taches junit optionelles pour %{name}.

%package nodeps
Summary:	Optional tasks for %{name}
Group:		Development/Languages/Java
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	ant-nodeps = %{epoch}:%{version}-%{release}
Conflicts:	ant-optional-clean, ant-optional-full

%description nodeps
Optional tasks for %{name}.

%description nodeps -l fr
Taches optionelles pour %{name}.

%package swing
Summary:	Optional swing tasks for %{name}
Group:		Development/Languages/Java
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	ant-swing = %{epoch}:%{version}-%{release}
Conflicts:	ant-optional-clean, ant-optional-full

%description swing
Optional swing tasks for %{name}.

%description swing -l fr
Taches swing optionelles pour %{name}.

%package trax
Summary:	Optional trax tasks for %{name}
Group:		Development/Languages/Java
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	jaxp_transform_impl
Provides:	ant-trax = %{epoch}:%{version}-%{release}
# The ant-xalan jar has been merged into the ant-trax one
Obsoletes:	ant-xalan2
Conflicts:	ant-optional-clean, ant-optional-full

%description trax
Optional trax tasks for %{name}.

%description trax -l fr
Taches trax optionelles pour %{name}.

%package scripts
Summary:	Additional scripts for %{name}
Group:		Development/Languages/Java
AutoReqProv:	no
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	/usr/bin/perl
Requires:	/usr/bin/python

%description scripts
Additional Perl and Python scripts for %{name}.

%description scripts -l fr
Scripts additionels pour %{name}.

%package doc
Summary:	Manual for %{name}
Group:		Development/Languages/Java

%description doc
Documentation for %{name}.

%description doc -l it
Documentazione di %{name}.

%description doc -l fr
Documentation pour %{name}.


%package javadoc
Summary:	Online manual for ant
Summary(pl):	Dokumentacja online do ant
Group:		Documentation
Obsoletes:	jakarta-ant-doc

%description javadoc
Documentation for ant, platform-independent build tool for Java. Used
by Apache Group for jakarta and xml projects.

%description javadoc -l pl
Dokumentacja do ant - niezale¿nego od platformy narzêdzia do budowania
w Javie.

%prep
%setup -q -n apache-%{name}-%{version}
%patch0 -p1

# clean jar files
find . -name "*.jar" -exec rm -f {} \;

%build

unset JAVA_HOME
export JAVA_HOME="%{java_home}" 

required_jars="jaxp_parser_impl"
%{?with_junit:required_jars="$required_jars junit"}
%{?with_antlr:required_jars="$required_jars antlr"}
%{?with_bsf:required_jars="$required_jars bsf jython beanshell"}
%{?with_apache_resolver:required_jars="$required_jars xml-commons-resolver"}
%{?with_commons_logging:required_jars="$required_jars jakarta-commons-logging"}
%{?with_commons_net:required_jars="$required_jars jakarta-commons-net"}
%{?with_jai:required_jars="$required_jars jait"}
%{?with_apache_bcel:required_jars="$required_jars bcel"}
%{?with_apache_log4j:required_jars="$required_jars log4j"}
%{?with_apache_oro:required_jars="$required_jars oro"}
%{?with_apache_regexp:required_jars="$required_jars regexp"}
%{?with_javamail:required_jars="$required_jars javamail/mailapi jaf"}
%{?with_jdepend:required_jars="$required_jars jdepend"}
%{?with_jsch:required_jars="$required_jars jsch"}

export CLASSPATH="`/usr/bin/build-classpath $required_jars`"

sh build.sh --noconfig main javadocs

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sysconfdir}/%{name}.d} \
		$RPM_BUILD_ROOT{%{_javadir}/%{name},%{ant_home}/{lib,etc}}

install dist/bin/{ant,antRun,runant.pl,runant.py} $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.conf

# XSLs
cp -p src%{_sysconfdir}/*.xsl $RPM_BUILD_ROOT%{ant_home}%{_sysconfdir}

# base jars
install dist/lib/%{name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
install dist/lib/%{name}-launcher.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-launcher-%{version}.jar

# optional jars
install build/lib/%{name}-nodeps.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-nodeps-%{version}.jar
install build/lib/%{name}-trax.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-trax-%{version}.jar
install build/lib/%{name}-jmf.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-jmf-%{version}.jar
install build/lib/%{name}-swing.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-swing-%{version}.jar
echo "ant/ant-jmf" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/jmf
echo "ant/ant-nodeps" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/nodeps
echo "ant/ant-swing" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/swing
echo "jaxp_transform_impl ant/ant-trax" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/trax

%if %{with junit}
install build/lib/%{name}-junit.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-junit-%{version}.jar
echo "junit ant/ant-junit" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/junit
%else
rm $RPM_BUILD_ROOT%{ant_home}%{_sysconfdir}/junit-{no,}frames.xml
%endif

%if %{with antlr}
install build/lib/%{name}-antlr.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-antlr-%{version}.jar
echo "antlr ant/ant-antlr" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/antlr
%endif

%if %{with bsf}
install build/lib/%{name}-apache-bsf.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-apache-bsf-%{version}.jar
echo "bsf ant/ant-apache-bsf" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/apache-bsf
%endif

%if %{with apache_resolver}
install build/lib/%{name}-apache-resolver.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-apache-resolver-%{version}.jar
echo "xml-commons-resolver ant/ant-apache-resolver" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/apache-resolver
%endif

%if %{with commons_logging}
install build/lib/%{name}-commons-logging.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-commons-logging-%{version}.jar
echo "jakarta-commons-logging ant/ant-commons-logging" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/commons-logging
%endif

%if %{with commons_net}
install build/lib/%{name}-commons-net.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-commons-net-%{version}.jar
echo "jakarta-commons-net ant/ant-commons-net" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/commons-net
%endif

%if %{with jai}
install build/lib/%{name}-jai.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-jai-%{version}.jar
echo "jai ant/ant-jai" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/jai
%endif

%if %{with apache_bcel}
install build/lib/%{name}-apache-bcel.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-apache-bcel-%{version}.jar
ln -sf %{name}-apache-bcel.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-jakarta-bcel.jar
echo "bcel ant/ant-apache-bcel" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/apache-bcel
%endif

%if %{with apache_log4j}
install build/lib/%{name}-apache-log4j.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-apache-log4j-%{version}.jar
ln -sf %{name}-apache-log4j.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-jakarta-log4j.jar
echo "log4j ant/ant-apache-log4j" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/apache-log4j
%endif

%if %{with apache_oro}
install build/lib/%{name}-apache-oro.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-apache-oro-%{version}.jar
ln -sf %{name}-apache-oro.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-jakarta-oro.jar
echo "oro ant/ant-apache-oro" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/apache-oro
%else
rm $RPM_BUILD_ROOT%{ant_home}%{_sysconfdir}/maudit-frames.xsl
%endif

%if %{with apache_regexp}
install build/lib/%{name}-apache-regexp.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-apache-regexp-%{version}.jar
echo "regexp ant/ant-apache-regexp" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/apache-regexp
ln -sf %{name}-apache-regexp.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-jakarta-regexp.jar
%endif

%if %{with javamail}
install build/lib/%{name}-javamail.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-javamail-%{version}.jar
echo "javamail/mailapi jaf ant/ant-javamail" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/javamail
%endif

%if %{with jdepend}
install build/lib/%{name}-jdepend.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-jdepend-%{version}.jar
echo "jdepend ant/ant-jdepend" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/jdepend
%else
rm $RPM_BUILD_ROOT%{ant_home}%{_sysconfdir}/jdepend*
%endif

%if %{with jsch}
install build/lib/%{name}-jsch.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-jsch-%{version}.jar
echo "jsch ant/ant-jsch" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/jsch
%endif

# jar aliases
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)
(cd $RPM_BUILD_ROOT%{_javadir}/%{name} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

# javadoc
install -d $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr build/javadocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}

# fix link between manual and javadoc
cd docs/manual
ln -sf %{_javadocdir}/%{name}-%{version} api
cd ..

%clean
rm -rf $RPM_BUILD_ROOT

%post javadoc
rm -f %{_javadocdir}/%{name}
ln -s %{name}-%{version} %{_javadocdir}/%{name}

%postun javadoc
if [ "$1" = "0" ]; then
  rm -f %{_javadocdir}/%{name}
fi

%files
%defattr(644,root,root,755)
%doc KEYS LICENSE* README WHATSNEW
%attr(755,root,root) %{_bindir}/ant
%attr(755,root,root) %{_bindir}/antRun
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-launcher.jar
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}-launcher-%{version}.jar
%dir %{ant_home}
%dir %{ant_home}%{_sysconfdir}
%{ant_home}%{_sysconfdir}/ant-update.xsl
%{ant_home}%{_sysconfdir}/changelog.xsl
%{ant_home}%{_sysconfdir}/log.xsl
%{ant_home}%{_sysconfdir}/tagdiff.xsl
%{ant_home}%{_sysconfdir}/junit-frames-xalan1.xsl
%dir %{ant_home}/lib
%dir %{_sysconfdir}/%{name}.d
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.conf

%files nodeps
%defattr(644,root,root,755)
%{_javadir}/%{name}/%{name}-nodeps.jar
%{_javadir}/%{name}/%{name}-nodeps-%{version}.jar
%{_sysconfdir}/%{name}.d/nodeps

%files swing
%defattr(644,root,root,755)
%{_javadir}/%{name}/%{name}-swing.jar
%{_javadir}/%{name}/%{name}-swing-%{version}.jar
%{_sysconfdir}/%{name}.d/swing

%files trax
%defattr(644,root,root,755)
%{_javadir}/%{name}/%{name}-trax.jar
%{_javadir}/%{name}/%{name}-trax-%{version}.jar
%{_sysconfdir}/%{name}.d/trax
%{ant_home}%{_sysconfdir}/mmetrics-frames.xsl
%{ant_home}%{_sysconfdir}/coverage-frames.xsl

%files jmf
%defattr(644,root,root,755)
%{_javadir}/%{name}/%{name}-jmf.jar
%{_javadir}/%{name}/%{name}-jmf-%{version}.jar
%{_sysconfdir}/%{name}.d/jmf

%files scripts
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*.pl
%attr(755,root,root) %{_bindir}/*.py

%files doc
%defattr(644,root,root,755)
%doc docs/*

%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/%{name}-%{version}

%if %{with junit}
%files junit
%defattr(644,root,root,755)
%{_javadir}/%{name}/%{name}-junit.jar
%{_javadir}/%{name}/%{name}-junit-%{version}.jar
%{_sysconfdir}/%{name}.d/junit
%{ant_home}%{_sysconfdir}/junit-frames.xsl
%{ant_home}%{_sysconfdir}/junit-noframes.xsl
%endif

%if %{with antlr}
%files antlr
%defattr(644,root,root,755)
%{_javadir}/%{name}/%{name}-antlr.jar
%{_javadir}/%{name}/%{name}-antlr-%{version}.jar
%{_sysconfdir}/%{name}.d/antlr
%endif

%if %{with apache_bsf}
%files apache-bsf
%defattr(644,root,root,755)
%{_javadir}/%{name}/%{name}-apache-bsf.jar
%{_javadir}/%{name}/%{name}-apache-bsf-%{version}.jar
%{_sysconfdir}/%{name}.d/apache-bsf
%endif

%if %{with apache_resolver}
%files apache-resolver
%defattr(644,root,root,755)
%{_javadir}/%{name}/%{name}-apache-resolver.jar
%{_javadir}/%{name}/%{name}-apache-resolver-%{version}.jar
%{_sysconfdir}/%{name}.d/apache-resolver
%endif

%if %{with commons_logging}
%files commons-logging
%defattr(644,root,root,755)
%{_javadir}/%{name}/%{name}-commons-logging.jar
%{_javadir}/%{name}/%{name}-commons-logging-%{version}.jar
%{_sysconfdir}/%{name}.d/commons-logging
%endif

%if %{with commons_net}
%files commons-net
%defattr(644,root,root,755)
%{_javadir}/%{name}/%{name}-commons-net.jar
%{_javadir}/%{name}/%{name}-commons-net-%{version}.jar
%{_sysconfdir}/%{name}.d/commons-net
%endif

%if %{with jai}
%files jai
%defattr(644,root,root,755)
%{_javadir}/%{name}/%{name}-jai.jar
%{_javadir}/%{name}/%{name}-jai-%{version}.jar
%{_sysconfdir}/%{name}.d/jai
%endif

%if %{with apache_bcel}
%files apache-bcel
%defattr(644,root,root,755)
%{_javadir}/%{name}/%{name}-apache-bcel.jar
%{_javadir}/%{name}/%{name}-apache-bcel-%{version}.jar
%{_javadir}/%{name}/%{name}-jakarta-bcel.jar
%{_sysconfdir}/%{name}.d/apache-bcel
%endif

%if %{with apache_log4j}
%files apache-log4j
%defattr(644,root,root,755)
%{_javadir}/%{name}/%{name}-apache-log4j.jar
%{_javadir}/%{name}/%{name}-apache-log4j-%{version}.jar
%{_javadir}/%{name}/%{name}-jakarta-log4j.jar
%{_sysconfdir}/%{name}.d/apache-log4j
%endif

%if %{with apache_oro}
%files apache-oro
%defattr(644,root,root,755)
%{_javadir}/%{name}/%{name}-apache-oro.jar
%{_javadir}/%{name}/%{name}-apache-oro-%{version}.jar
%{_javadir}/%{name}/%{name}-jakarta-oro.jar
%{_sysconfdir}/%{name}.d/apache-oro
%{ant_home}%{_sysconfdir}/maudit-frames.xsl
%endif

%if %{with apache_regexp}
%files apache-regexp
%defattr(644,root,root,755)
%{_javadir}/%{name}/%{name}-apache-regexp.jar
%{_javadir}/%{name}/%{name}-apache-regexp-%{version}.jar
%{_javadir}/%{name}/%{name}-jakarta-regexp.jar
%{_sysconfdir}/%{name}.d/apache-regexp
%endif

%if %{with javamail}
%files javamail
%defattr(644,root,root,755)
%{_javadir}/%{name}/%{name}-javamail.jar
%{_javadir}/%{name}/%{name}-javamail-%{version}.jar
%{_sysconfdir}/%{name}.d/javamail
%endif

%if %{with jdepend}
%files jdepend
%defattr(644,root,root,755)
%{_javadir}/%{name}/%{name}-jdepend.jar
%{_javadir}/%{name}/%{name}-jdepend-%{version}.jar
%{_sysconfdir}/%{name}.d/jdepend
%{ant_home}%{_sysconfdir}/jdepend.xsl
%{ant_home}%{_sysconfdir}/jdepend-frames.xsl
%endif

%if %{with jsch}
%files jsch
%defattr(644,root,root,755)
%{_javadir}/%{name}/%{name}-jsch.jar
%{_javadir}/%{name}/%{name}-jsch-%{version}.jar
%{_sysconfdir}/%{name}.d/jsch
%endif
