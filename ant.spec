# TODO
# - review config files in /etc/ant.d. Something seems to be broken there.
# - prepare all BR and test the full build
#   TODO:
#   - stylebook: http://svn.apache.org/viewcvs.cgi/xml/stylebook/
#   - starteam: http://www.borland.com/downloads/download_starteam.html (30-day trial, needs registration)
#   - weblogic: http://www.bea.com/ ? (needs registration)
#
# Conditional build:
%bcond_with	bootstrap	# minimal build for bootstrap
%bcond_with	nonfree		# build tasks with non-distributable dependencies
%bcond_without	antlr		# disable building antlr optional task(s)
%bcond_without	apache_bcel	# disable building apache-bcel optional task(s)
%bcond_without	apache_bsf	# disable building apache-bsf optional task(s)
%bcond_without	apache_log4j	# disable building log4j optional task(s)
%bcond_without	apache_oro	# disable building apache-oro optional task(s)
%bcond_without	apache_regexp	# disable building apache-regexp optional task(s)
%bcond_without	apache_resolver	# disable building apache-resolver optional task(s)
%bcond_without	commons_logging	# disable building commons-logging optional task(s)
%bcond_without	commons_net	# disable building commons-net optional task(s)
%bcond_without	jai		# disable building jai optional task(s)
%bcond_without	javamail	# disable building javamail optional task(s)
%bcond_without	jdepend		# disable building jdepend optional task(s)
%bcond_without	jsch		# disable building jsch optional task(s)
%bcond_without	junit		# disable building junit optional task(s)
%bcond_without	netrexx		# disable building netrexx optional taks(s)

%if %{without nonfree}
%undefine	with_jai
%endif
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
%undefine	with_jai
%undefine	with_javamail
%undefine	with_jdepend
%undefine	with_jsch
%undefine	with_netrexx
%endif

%include	/usr/lib/rpm/macros.java

%define		_rel	9
Summary:	Ant build tool for Java
Summary(fr.UTF-8):	Outil de compilation pour java
Summary(it.UTF-8):	Tool per la compilazione di programmi java
Summary(pl.UTF-8):	Ant - narzędzie do budowania w Javie
Name:		ant
Version:	1.7.1
Release:	%{bootstrap_release %_rel}
License:	Apache
Group:		Development/Languages/Java
Source0:	http://www.apache.org/dist/ant/source/apache-%{name}-%{version}-src.tar.bz2
# Source0-md5:	0d68db4a1ada5c91bcbf53cefd0c2fd7
Source1:	%{name}.conf
Patch0:		%{name}-antRun.patch
# patch1 has been applied to ant sources in svn. It won't be needed for the
# next release of ant.
Patch1:		%{name}-gcjtask.patch
URL:		http://ant.apache.org/
%{?with_antlr:BuildRequires:	antlr}
%{!?with_bootstrap:BuildRequires:	ant}
%{?with_javamail:BuildRequires:	java(jaf)}
%{?with_jai:BuildRequires:	java(jai)}
%{?with_javamail:BuildRequires:	java(javamail)}
%{?with_apache_bcel:BuildRequires:	java-bcel}
%{?with_apache_bsf:BuildRequires:	java-beanshell}
%{?with_apache_bsf:BuildRequires:	java-bsf}
%{?with_commons_logging:BuildRequires:	java-commons-logging}
%{?with_commons_net:BuildRequires:	java-commons-net1}
%{?with_jdepend:BuildRequires:	java-jdepend}
%{?with_jsch:BuildRequires:	java-jsch >= 0.1.21}
%{?with_junit:BuildRequires:	java-junit}
%{?with_apache_log4j:BuildRequires:	java-log4j >= 1.2}
%{?with_netrexx:BuildRequires:	java-netrexx}
%{?with_apache_oro:BuildRequires:	java-oro}
%{?with_apache_regexp:BuildRequires:	java-regexp}
BuildRequires:	java-xerces
%{?with_apache_resolver:BuildRequires:	java-xml-commons-resolver}
BuildRequires:	jdk
BuildRequires:	jpackage-utils
%{?with_apache_bsf:BuildRequires:	jython}
BuildRequires:	rpm >= 4.4.9-56
BuildRequires:	rpm-javaprov
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	jpackage-utils
Obsoletes:	jakarta-ant
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	ant_home 	%{_datadir}/ant

%description
Platform-independent build tool for Java. Ant is a Java based build
system. Ant is used by apache jakarta & xml projects.

%description -l fr.UTF-8
Ant est un outil de compilation multi-plateformes pour java. Il est
utilisé par les projets apache-jakarta et apache-xml.

%description -l it.UTF-8
Ant e' un tool indipendente dalla piattaforma creato per faciltare la
compilazione di programmi java. Allo stato attuale viene utilizzato
dai progetti apache jakarta ed apache xml.

%description -l pl.UTF-8
Niezależne od platformy narzędzie do budowania w Javie. Ant jest
używany przez projekty apache jakarta i xml.

%package antlr
Summary:	Optional antlr tasks for %{name}
Summary(fr.UTF-8):	Taches antlr optionelles pour %{name}
Summary(pl.UTF-8):	Opcjonalne zadania antlr dla anta
Group:		Development/Languages/Java
Requires:	%{name} = %{version}-%{release}
Requires:	antlr
Conflicts:	ant-optional-clean
Conflicts:	ant-optional-full

%description antlr
Optional antlr tasks for %{name}.

%description antlr -l fr.UTF-8
Taches antlr optionelles pour %{name}.

%description antlr -l pl.UTF-8
Opcjonalne zadania antlr dla anta.

%package apache-bcel
Summary:	Optional apache bcel tasks for %{name}
Summary(fr.UTF-8):	Taches apache bcel optionelles pour %{name}
Summary(pl.UTF-8):	Opcjonalne zadania apache bcel dla anta
Group:		Development/Languages/Java
Requires:	%{name} = %{version}-%{release}
Requires:	jakarta-bcel
Provides:	ant-jakarta-bcel = %{version}-%{release}
Obsoletes:	ant-jakarta-bcel
Conflicts:	ant-optional-clean
Conflicts:	ant-optional-full

%description apache-bcel
Optional apache bcel tasks for %{name}.

%description apache-bcel -l fr.UTF-8
Taches apache bcel optionelles pour %{name}.

%description apache-bcel -l pl.UTF-8
Opcjonalne zadania apache bcel dla anta.

%package apache-bsf
Summary:	Optional apache bsf tasks for %{name}
Summary(fr.UTF-8):	Taches apache bsf optionelles pour %{name}
Summary(pl.UTF-8):	Opcjonalne zadania apache bsf dla anta
Group:		Development/Languages/Java
Requires:	%{name} = %{version}-%{release}
Requires:	bsf
Conflicts:	ant-optional-clean
Conflicts:	ant-optional-full

%description apache-bsf
Optional apache bsf tasks for %{name}.

%description apache-bsf -l fr.UTF-8
Taches apache bsf optionelles pour %{name}.

%description apache-bsf -l pl.UTF-8
Opcjonalne zadania apache bsf dla anta.

%package apache-log4j
Summary:	Optional apache log4j tasks for %{name}
Summary(fr.UTF-8):	Taches apache log4j optionelles pour %{name}
Summary(pl.UTF-8):	Opcjonalne zadania apache log4j dla anta
Group:		Development/Languages/Java
Requires:	%{name} = %{version}-%{release}
Requires:	java-log4j >= 1.2
Provides:	ant-jakarta-log4j = %{version}-%{release}
Obsoletes:	ant-jakarta-log4j
Conflicts:	ant-optional-clean
Conflicts:	ant-optional-full

%description apache-log4j
Optional apache log4j tasks for %{name}.

%description apache-log4j -l fr.UTF-8
Taches apache log4j optionelles pour %{name}.

%description apache-log4j -l pl.UTF-8
Opcjonalne zadania apache log4j dla anta.

%package apache-oro
Summary:	Optional apache oro tasks for %{name}
Summary(fr.UTF-8):	Taches apache oro optionelles pour %{name}
Summary(pl.UTF-8):	Opcjonalne zadania apache oro dla anta
Group:		Development/Languages/Java
Requires:	%{name} = %{version}-%{release}
Requires:	java-oro
Provides:	ant-jakarta-oro = %{version}-%{release}
Obsoletes:	ant-jakarta-oro
Conflicts:	ant-optional-clean
Conflicts:	ant-optional-full

%description apache-oro
Optional apache oro tasks for %{name}.

%description apache-oro -l fr.UTF-8
Taches apache oro optionelles pour %{name}.

%description apache-oro -l pl.UTF-8
Opcjonalne zadania apache oro dla anta.

%package apache-regexp
Summary:	Optional apache regexp tasks for %{name}
Summary(fr.UTF-8):	Taches apache regexp optionelles pour %{name}
Summary(pl.UTF-8):	Opcjonalne zadania apache regexp dla anta
Group:		Development/Languages/Java
Requires:	%{name} = %{version}-%{release}
Requires:	java-regexp
Obsoletes:	ant-jakarta-regexp
Conflicts:	ant-optional-clean
Conflicts:	ant-optional-full

%description apache-regexp
Optional apache regexp tasks for %{name}.

%description apache-regexp -l fr.UTF-8
Taches apache regexp optionelles pour %{name}.

%description apache-regexp -l pl.UTF-8
Opcjonalne zadania apache regexp dla anta.

%package apache-resolver
Summary:	Optional apache resolver tasks for %{name}
Summary(fr.UTF-8):	Taches apache resolver optionelles pour %{name}
Summary(pl.UTF-8):	Opcjonalne zadania apache resolver dla anta
Group:		Development/Languages/Java
Requires:	%{name} = %{version}-%{release}
Requires:	java-xml-commons-resolver
Provides:	ant-apache-resolver = %{version}-%{release}
Conflicts:	ant-optional-clean
Conflicts:	ant-optional-full

%description apache-resolver
Optional apache resolver tasks for %{name}.

%description apache-resolver -l fr.UTF-8
Taches apache resolver optionelles pour %{name}.

%package commons-logging
Summary:	Optional commons logging tasks for %{name}
Summary(fr.UTF-8):	Taches commons logging optionelles pour %{name}
Summary(pl.UTF-8):	Opcjonalne zadania commons logging dla anta
Group:		Development/Languages/Java
Requires:	%{name} = %{version}-%{release}
Requires:	jakarta-commons-logging
Conflicts:	ant-optional-clean
Conflicts:	ant-optional-full

%description commons-logging
Optional commons logging tasks for %{name}.

%description commons-logging -l fr.UTF-8
Taches commons logging optionelles pour %{name}.

%description commons-logging -l pl.UTF-8
Opcjonalne zadania commons logging dla anta.

%package commons-net
Summary:	Optional commons net tasks for %{name}
Summary(fr.UTF-8):	Taches commons net optionelles pour %{name}
Summary(pl.UTF-8):	Opcjonalne zadania commons net dla anta
Group:		Development/Languages/Java
Requires:	%{name} = %{version}-%{release}
Requires:	java-commons-net1
Conflicts:	ant-optional-clean
Conflicts:	ant-optional-full

%description commons-net
Optional commons net tasks for %{name}.

%description commons-net -l fr.UTF-8
Taches commons net optionelles pour %{name}.

%description commons-net -l pl.UTF-8
Opcjonalne zadania commons net dla anta.

%package jai
Summary:	Optional jai tasks for %{name}
Summary(fr.UTF-8):	Taches jai optionelles pour %{name}
Summary(pl.UTF-8):	Opcjonalne zadania jai dla anta
Group:		Development/Languages/Java
Requires:	%{name} = %{version}-%{release}
Requires:	jai
Conflicts:	ant-optional-clean
Conflicts:	ant-optional-full

%description jai
Optional jai tasks for %{name}.

%description jai -l fr.UTF-8
Taches jai optionelles pour %{name}.

%description jai -l pl.UTF-8
Opcjonalne zadania jai dla anta.

%package javamail
Summary:	Optional javamail tasks for %{name}
Summary(fr.UTF-8):	Taches javamail optionelles pour %{name}
Summary(pl.UTF-8):	Opcjonalne zadania javamail dla anta
Group:		Development/Languages/Java
Requires:	%{name} = %{version}-%{release}
Requires:	java(jaf)
Requires:	java(javamail) >= 1.2
Conflicts:	ant-optional-clean
Conflicts:	ant-optional-full

%description javamail
Optional javamail tasks for %{name}.

%description javamail -l fr.UTF-8
Taches javamail optionelles pour %{name}.

%description javamail -l pl.UTF-8
Opcjonalne zadania javamail dla anta.

%package jdepend
Summary:	Optional jdepend tasks for %{name}
Summary(fr.UTF-8):	Taches jdepend optionelles pour %{name}
Summary(pl.UTF-8):	Opcjonalne zadania jdepend dla anta
Group:		Development/Languages/Java
Requires:	%{name} = %{version}-%{release}
Requires:	jdepend
Conflicts:	ant-optional-clean
Conflicts:	ant-optional-full

%description jdepend
Optional jdepend tasks for %{name}.

%description jdepend -l fr.UTF-8
Taches jdepend optionelles pour %{name}.

%description jdepend -l pl.UTF-8
Opcjonalne zadania jdepend dla anta.

%package jmf
Summary:	Optional jmf tasks for %{name}
Summary(fr.UTF-8):	Taches jmf optionelles pour %{name}
Summary(pl.UTF-8):	Opcjonalne zadania jmf dla anta
Group:		Development/Languages/Java
Requires:	%{name} = %{version}-%{release}
Conflicts:	ant-optional-clean
Conflicts:	ant-optional-full

%description jmf
Optional jmf tasks for %{name}.

%description jmf -l fr.UTF-8
Taches jmf optionelles pour %{name}.

%description jmf -l pl.UTF-8
Opcjonalne zadania jmf dla anta.

%package jsch
Summary:	Optional jsch tasks for %{name}
Summary(fr.UTF-8):	Taches jsch optionelles pour %{name}
Summary(pl.UTF-8):	Opcjonalne zadania jsch dla anta
Group:		Development/Languages/Java
Requires:	%{name} = %{version}-%{release}
Requires:	jsch >= 0.1.21
Conflicts:	ant-optional-clean
Conflicts:	ant-optional-full

%description jsch
Optional jsch tasks for %{name}.

%description jsch -l fr.UTF-8
Taches jsch optionelles pour %{name}.

%description jsch -l pl.UTF-8
Opcjonalne zadania jsch dla anta.

%package junit
Summary:	Optional junit tasks for %{name}
Summary(fr.UTF-8):	Taches junit optionelles pour %{name}
Summary(pl.UTF-8):	Opcjonalne zadania junit dla anta
Group:		Development/Languages/Java
Requires:	%{name} = %{version}-%{release}
Requires:	java-junit
Conflicts:	ant-optional-clean
Conflicts:	ant-optional-full

%description junit
Optional junit tasks for %{name}.

%description junit -l fr.UTF-8
Taches junit optionelles pour %{name}.

%description junit -l pl.UTF-8
Opcjonalne zadania junit dla anta.

%package netrexx
Summary:	Optional netrexx tasks for %{name}
Summary(fr.UTF-8):	Taches netrexx optionelles pour %{name}
Summary(pl.UTF-8):	Opcjonalne zadania netrexx dla anta
Group:		Development/Languages/Java
Requires:	%{name} = %{version}-%{release}
Conflicts:	ant-optional-clean
Conflicts:	ant-optional-full

%description netrexx
Optional netrexx tasks for %{name}.

%description netrexx -l fr.UTF-8
Taches netrexx optionelles pour %{name}.

%description netrexx -l pl.UTF-8
Opcjonalne zadania netrexx dla anta.

%package nodeps
Summary:	Optional tasks for %{name}
Summary(fr.UTF-8):	Taches optionelles pour %{name}
Summary(pl.UTF-8):	Opcjonalne zadania dla anta
Group:		Development/Languages/Java
Requires:	%{name} = %{version}-%{release}
Conflicts:	ant-optional-clean
Conflicts:	ant-optional-full

%description nodeps
Optional tasks for %{name}.

%description nodeps -l fr.UTF-8
Taches optionelles pour %{name}.

%description nodeps -l pl.UTF-8
Opcjonalne zadania dla anta.

%package swing
Summary:	Optional swing tasks for %{name}
Summary(fr.UTF-8):	Taches swing optionelles pour %{name}
Summary(pl.UTF-8):	Opcjonalne zadania swing dla anta
Group:		Development/Languages/Java
Requires:	%{name} = %{version}-%{release}
Conflicts:	ant-optional-clean
Conflicts:	ant-optional-full

%description swing
Optional swing tasks for %{name}.

%description swing -l fr.UTF-8
Taches swing optionelles pour %{name}.

%description swing -l pl.UTF-8
Opcjonalne zadania swing dla anta.

%package trax
Summary:	Optional trax tasks for %{name}
Summary(fr.UTF-8):	Taches trax optionelles pour %{name}
Summary(pl.UTF-8):	Dodatkowe zadania trax dla anta
Group:		Development/Languages/Java
Requires:	%{name} = %{version}-%{release}
Requires:	java(jaxp_transform_impl)
# The ant-xalan jar has been merged into the ant-trax one
Obsoletes:	ant-xalan2
Conflicts:	ant-optional-clean
Conflicts:	ant-optional-full

%description trax
Optional trax tasks for %{name}.

%description trax -l fr.UTF-8
Taches trax optionelles pour %{name}.

%description trax -l pl.UTF-8
Dodatkowe zadania trax dla anta.

%package scripts
Summary:	Additional scripts for %{name}
Summary(fr.UTF-8):	Scripts additionels pour %{name}
Summary(pl.UTF-8):	Dodatkowe skrypty dla anta
Group:		Development/Languages/Java
Requires:	%{name} = %{version}-%{release}
Requires:	/usr/bin/perl
Requires:	/usr/bin/python
AutoReqProv:	no

%description scripts
Additional Perl and Python scripts for %{name}.

%description scripts -l fr.UTF-8
Scripts additionels pour %{name}.

%description scripts -l pl.UTF-8
Dodatkowe skrypty dla anta.

%package doc
Summary:	Manual for %{name}
Summary(fr.UTF-8):	Documentation pour %{name}
Summary(it.UTF-8):	Documentazione di %{name}
Summary(pl.UTF-8):	Podręcznik dla anta
Group:		Development/Languages/Java

%description doc
Documentation for %{name}.

%description doc -l fr.UTF-8
Documentation pour %{name}.

%description doc -l it.UTF-8
Documentazione di %{name}.

%description doc -l pl.UTF-8
Dokumentacja do anta.

%package javadoc
Summary:	Online manual for ant
Summary(pl.UTF-8):	Dokumentacja online do ant
Group:		Documentation
Requires:	jpackage-utils
Obsoletes:	jakarta-ant-doc

%description javadoc
Documentation for ant, platform-independent build tool for Java. Used
by Apache Group for jakarta and xml projects.

%description javadoc -l pl.UTF-8
Dokumentacja do anta - niezależnego od platformy narzędzia do
budowania w Javie. Jest ono używane przez Apache Group w projektach
jakarta i xml.

%prep
%setup -q -n apache-%{name}-%{version}
%patch0 -p1
%patch1 -p1

# clean jar files
find . -name "*.jar" -exec rm -f {} \;

sed -i -e 's|@BINDIR@|%{_bindir}|g' \
	src/main/org/apache/tools/ant/taskdefs/Exec.java \
	src/main/org/apache/tools/ant/taskdefs/Execute.java

# fix link between manual and javadoc
ln -sf %{_javadocdir}/%{name}-%{version} docs/manual/api

%build
export JAVA_HOME="%{java_home}"

required_jars="jaxp_parser_impl"
%{?with_junit:required_jars="$required_jars junit"}
%{?with_antlr:required_jars="$required_jars antlr"}
%{?with_apache_bsf:required_jars="$required_jars bsf jython bsh"}
%{?with_apache_resolver:required_jars="$required_jars resolver"}
%{?with_commons_logging:required_jars="$required_jars commons-logging"}
%{?with_commons_net:required_jars="$required_jars commons-net1"}
%{?with_jai:required_jars="$required_jars jai_core jai_codec"}
%{?with_apache_bcel:required_jars="$required_jars bcel"}
%{?with_apache_log4j:required_jars="$required_jars log4j"}
%{?with_apache_oro:required_jars="$required_jars oro"}
%{?with_apache_regexp:required_jars="$required_jars regexp"}
%{?with_javamail:required_jars="$required_jars mail activation"}
%{?with_jdepend:required_jars="$required_jars jdepend"}
%{?with_jsch:required_jars="$required_jars jsch"}
%{?with_netrexx:required_jars="$required_jars NetRexxC"}

CLASSPATH=$(build-classpath $required_jars)
export CLASSPATH

export SHELL=/bin/sh

%if %{with bootstrap}
sh build.sh --noconfig main javadocs
%else
%ant -Dbuild.compiler=extJavac main javadocs
%endif

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

%if %{with apache_bsf}
install build/lib/%{name}-apache-bsf.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-apache-bsf-%{version}.jar
echo "bsf ant/ant-apache-bsf" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/apache-bsf
%endif

%if %{with apache_resolver}
install build/lib/%{name}-apache-resolver.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-apache-resolver-%{version}.jar
echo "resolver ant/ant-apache-resolver" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/apache-resolver
%endif

%if %{with commons_logging}
install build/lib/%{name}-commons-logging.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-commons-logging-%{version}.jar
echo "commons-logging ant/ant-commons-logging" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/commons-logging
%endif

%if %{with commons_net}
install build/lib/%{name}-commons-net.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-commons-net-%{version}.jar
echo "commons-net1 ant/ant-commons-net" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/commons-net
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
echo "log4j ant/ant-log4j" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/apache-log4j
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
echo "mail jaf ant/ant-javamail" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/javamail
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

%if %{with netrexx}
install build/lib/%{name}-netrexx.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-netrexx-%{version}.jar
echo "netrexx ant/ant-netrexx" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/netrexx
%endif

# jar aliases
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)
(cd $RPM_BUILD_ROOT%{_javadir}/%{name} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

# javadoc
install -d $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr build/javadocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

%clean
rm -rf $RPM_BUILD_ROOT

%post javadoc
ln -nfs %{name}-%{version} %{_javadocdir}/%{name}

%files
%defattr(644,root,root,755)
%doc KEYS LICENSE* README WHATSNEW
%attr(755,root,root) %{_bindir}/ant
%attr(755,root,root) %{_bindir}/antRun
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-launcher.jar
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}-launcher-%{version}.jar
%dir %{_javadir}/%{name}
%dir %{ant_home}
%dir %{ant_home}%{_sysconfdir}
%{ant_home}%{_sysconfdir}/ant-update.xsl
%{ant_home}%{_sysconfdir}/changelog.xsl
%{ant_home}%{_sysconfdir}/common2master.xsl
%{ant_home}%{_sysconfdir}/log.xsl
%{ant_home}%{_sysconfdir}/tagdiff.xsl
%{ant_home}%{_sysconfdir}/junit-frames-xalan1.xsl
%dir %{ant_home}/lib
%dir %{_sysconfdir}/%{name}.d
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.conf

%if %{with antlr}
%files antlr
%defattr(644,root,root,755)
%{_javadir}/%{name}/%{name}-antlr.jar
%{_javadir}/%{name}/%{name}-antlr-%{version}.jar
%{_sysconfdir}/%{name}.d/antlr
%endif

%if %{with apache_bcel}
%files apache-bcel
%defattr(644,root,root,755)
%{_javadir}/%{name}/%{name}-apache-bcel.jar
%{_javadir}/%{name}/%{name}-apache-bcel-%{version}.jar
%{_javadir}/%{name}/%{name}-jakarta-bcel.jar
%{_sysconfdir}/%{name}.d/apache-bcel
%endif

%if %{with apache_bsf}
%files apache-bsf
%defattr(644,root,root,755)
%{_javadir}/%{name}/%{name}-apache-bsf.jar
%{_javadir}/%{name}/%{name}-apache-bsf-%{version}.jar
%{_sysconfdir}/%{name}.d/apache-bsf
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

%files jmf
%defattr(644,root,root,755)
%{_javadir}/%{name}/%{name}-jmf.jar
%{_javadir}/%{name}/%{name}-jmf-%{version}.jar
%{_sysconfdir}/%{name}.d/jmf

%if %{with jsch}
%files jsch
%defattr(644,root,root,755)
%{_javadir}/%{name}/%{name}-jsch.jar
%{_javadir}/%{name}/%{name}-jsch-%{version}.jar
%{_sysconfdir}/%{name}.d/jsch
%endif

%if %{with junit}
%files junit
%defattr(644,root,root,755)
%{_javadir}/%{name}/%{name}-junit.jar
%{_javadir}/%{name}/%{name}-junit-%{version}.jar
%{_sysconfdir}/%{name}.d/junit
%{ant_home}%{_sysconfdir}/junit-frames.xsl
%{ant_home}%{_sysconfdir}/junit-noframes.xsl
%endif

%if %{with netrexx}
%files netrexx
%defattr(644,root,root,755)
%{_javadir}/%{name}/%{name}-netrexx.jar
%{_javadir}/%{name}/%{name}-netrexx-%{version}.jar
%{_sysconfdir}/%{name}.d/netrexx
%endif

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
%ghost %{_javadocdir}/%{name}
