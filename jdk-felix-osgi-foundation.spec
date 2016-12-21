Name     : jdk-felix-osgi-foundation
Version  : 1.2.0
Release  : 1
URL      : http://repo.maven.apache.org/maven2/org/apache/felix/org.osgi.foundation/1.2.0/org.osgi.foundation-1.2.0.jar
Source0  : http://repo.maven.apache.org/maven2/org/apache/felix/org.osgi.foundation/1.2.0/org.osgi.foundation-1.2.0.jar
Source1  : http://repo.maven.apache.org/maven2/org/apache/felix/org.osgi.foundation/1.2.0/org.osgi.foundation-1.2.0.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
BuildRequires : javapackages-tools
BuildRequires : lxml
BuildRequires : openjdk-dev
BuildRequires : python3
BuildRequires : six

%description
No detailed description available

%prep

%build

%install
mkdir -p %{buildroot}/usr/share/maven-poms
mkdir -p %{buildroot}/usr/share/maven-metadata
mkdir -p %{buildroot}/usr/share/java

mv %{SOURCE0} %{buildroot}/usr/share/java/felix-osgi-foundation.jar
mv %{SOURCE1} %{buildroot}/usr/share/maven-poms/felix-osgi-foundation.pom

# Creates metadata
python3 /usr/share/java-utils/maven_depmap.py \
-n "" \
--pom-base %{buildroot}/usr/share/maven-poms \
--jar-base %{buildroot}/usr/share/java \
%{buildroot}/usr/share/maven-metadata/felix-osgi-foundation.xml \
%{buildroot}/usr/share/maven-poms/felix-osgi-foundation.pom \
%{buildroot}/usr/share/java/felix-osgi-foundation.jar \

%files
%defattr(-,root,root,-)
/usr/share/maven-metadata/felix-osgi-foundation.xml
/usr/share/maven-poms/felix-osgi-foundation.pom
/usr/share/java/felix-osgi-foundation.jar
