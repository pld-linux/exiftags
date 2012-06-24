Summary:	A digital camera image meta-data (Exif) parser
Summary(pl):	Analizator metadanych (Exif) obraz�w z aparat�w cyfrowych
Name:		exiftags
Version:	1.00
Release:	1
License:	BSD
Group:		Applications/Multimedia
Source0:	http://johnst.org/sw/exiftags/%{name}-%{version}.tar.gz
# Source0-md5:	5dedd2336914f5a7c6ed3289cb7a3b1b
URL:		http://johnst.org/sw/exiftags/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
exiftags parses a JPEG file looking for Exif (Exchangeable Image File)
data, formatting and printing image properties. Digital cameras
typically add Exif data to the image files they produce containing
information about the camera and digitized image. exiftags includes
support for some camera manufacturer-specific properties.

An included companion utility, exifcom, displays and writes the
UserComment Exif tag that some cameras include in the image metadata
they create. This program is useful for recording caption or location
information in the image file itself.

%description -l pl
exiftags analizuje plik JPEG poszukuj�c danych Exif (Exchangeable
Image File), formatuj�c i wypisuj�c w�asno�ci obrazu. Aparaty cyfrowe
zwykle dodaj� do produkowanych przez siebie plik�w graficznych dane
Exif, zawieraj�ce informacje o aparacie i obrazie cyfrowym. exiftags
obs�uguje niekt�re w�asno�ci specyficzne dla poszczeg�lnych
producent�w aparat�w.

Do��czone narz�dzie towarzysz�ce, exifcom, wy�wietla i zapisuje
znacznik Exif UserComment, do��czany przez niekt�re aparaty. Ten
program jest przydatny do zapisywania podpis�w lub informacji 
o miejscu w samym obrazku.

%prep
%setup -q

%build
%{__make} RPM_OPT_FLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

install -D exiftags $RPM_BUILD_ROOT%{_bindir}/exiftags
install -D exifcom $RPM_BUILD_ROOT%{_bindir}/exifcom
install -D exiftime $RPM_BUILD_ROOT%{_bindir}/exiftime
install -D exiftags.1 $RPM_BUILD_ROOT%{_mandir}/man1/exiftags.1
install -D exifcom.1 $RPM_BUILD_ROOT%{_mandir}/man1/exifcom.1
install -D exiftime.1 $RPM_BUILD_ROOT%{_mandir}/man1/exiftime.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGES
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
