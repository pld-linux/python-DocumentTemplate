%define pp_subname DocumentTemplate
Summary:	Document creation system based on templates to create HTML and other documents
Summary(pl):	System tworzenia dokumentów HTML i innych bazuj±cy na wzorcach
Name:		python-%{pp_subname}
Version:	2.3.0
Release:	2
License:	Zope Public License (ZPL)
Group:		Development/Languages/Python
Source0:	ZTemplates-%{version}.tar.gz
Patch0:		ztemplate-bld.patch
#BuildRequires:	python-devel >= 1.5, sed
Requires:	python >= 1.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Icon:		linux-python-small.gif

%description
DocumentTemplates (ZTemplates) provide for creation of textual
documents, such as HTML pages, from template source by inserting data
from python objects and name-spaces. DocumentTemplates are especially
useful when it is desirable to separate template text from python
program source. For example, HTML templates may be edited by people
who know HTML, and don't know python, while associated python code may
be edited by people who know python but not HTML.

%description -l pl
DocumentTemplates (ZTemplates) pozwalaj± tworzyæ tekstowe dokumenty,
takie jak strony HTML, ze wzorca przez wstawianie danych z obiektów i
przestrzeni nazw Pythona. DocumentTemplates s± przydatne zw³aszcza do
oddzielenia tekstu wzorca od ¼róde³ programu w Pythonie. Na przyk³ad,
wzorce HTML mog± byæ modyfikowane przez ludzi znaj±cych HTML, a nie
znaj±cych Pythona, natomiast kod w Pythonie mo¿e byæ modyfikowany
przez znaj±cych Pythona, ale nie HTML.

%prep
%setup -q -n ZTemplates-2.3.0
%patch -p1

%build
cd DocumentTemplate
%{__make} -f Makefile.pre.in boot
%{__make}
python -O *.py

python - <<END
import py_compile, os, fnmatch

for f in os.listdir("."):
	if fnmatch.fnmatch(f, "*.py"):
		print "Byte compiling "+f+"..."
		py_compile.compile(f)
END

%install
rm -rf $RPM_BUILD_ROOT
install -d -m 755 $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/%{pp_subname}
echo %{pp_subname} > $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/%{pp_subname}.pth
install $RPM_BUILD_DIR/ZTemplates-2.3.0/DocumentTemplate/*.py $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/%{pp_subname}
install $RPM_BUILD_DIR/ZTemplates-2.3.0/DocumentTemplate/*.py{c,o} $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/%{pp_subname}
install -m 755 $RPM_BUILD_DIR/ZTemplates-2.3.0/DocumentTemplate/*.so $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/%{pp_subname}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.txt LICENSE.txt README.txt
%{_libdir}/python1.5/site-packages/%{pp_subname}
%{_libdir}/python1.5/site-packages/%{pp_subname}.pth
