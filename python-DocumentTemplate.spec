%define pp_subname DocumentTemplate
Summary:       Document creation system based on templates to create HTML and other documents.
Name:          python-%{pp_subname}
Version:       2.3.0
Release:       1
Copyright:     Zope Public Licence
Group:         Development/Languages/Python 
Group(pl):     Programowanie/Jêzyki/Python
Source:        ZTemplates-%{version}.tar.gz
Patch:         ztemplate-bld.patch
Requires:      python >= 1.5 
BuildRoot:	   /tmp/%{name}-%{version}-root
Icon:          linux-python-small.gif
#BuildRequires: python-devel >= 1.5, sed

%description
DocumentTemplates (ZTemplates) provide for creation of textual 
documents, such as HTML pages, from template source by inserting data 
from python objects and name-spaces.  DocumentTemplates are especially 
useful when it is desirable to separate template text from python 
program source.  For example, HTML templates may be edited by people 
who know HTML, and don't know python, while associated python code may 
be edited by people who know python but not HTML.

%prep
%setup -n ZTemplates-2.3.0
%patch -p1

%build
cd DocumentTemplate
make -f Makefile.pre.in boot
make
python -O *.py

python - <<END
import py_compile, os, fnmatch

for f in os.listdir("."):
	if fnmatch.fnmatch(f, "*.py"):
		print "Byte compiling "+f+"..."
		py_compile.compile(f)
END

%install
install -d -m 755 $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/%{pp_subname}
echo %{pp_subname} > $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/%{pp_subname}.pth
install -m 644 $RPM_BUILD_DIR/ZTemplates-2.3.0/DocumentTemplate/*.py $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/%{pp_subname}
install -m 644 $RPM_BUILD_DIR/ZTemplates-2.3.0/DocumentTemplate/*.py{c,o} $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/%{pp_subname}
install -m 755 $RPM_BUILD_DIR/ZTemplates-2.3.0/DocumentTemplate/*.so $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/%{pp_subname}

gzip -9nf CHANGES.txt LICENSE.txt README.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc {CHANGES.txt,LICENSE.txt,README.txt}.gz
%{_libdir}/python1.5/site-packages/%{pp_subname}
%{_libdir}/python1.5/site-packages/%{pp_subname}.pth
