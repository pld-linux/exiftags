Summary:	A digital camera image meta-data (Exif) parser.
Name:		exiftags
Version:	0.96
Release:	1
License:	BSD
Group:		Applications/Multimedia
Source0:	http://johnst.org/sw/exiftags/%{name}-%{version}.tar.gz
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

%prep
%setup -q

%build
%{__make} RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT

install -D exiftags $RPM_BUILD_ROOT%{_bindir}/exiftags
install -D exifcom $RPM_BUILD_ROOT%{_bindir}/exifcom
install -D exiftags.1 $RPM_BUILD_ROOT%{_mandir}/man1/exiftags.1
install -D exifcom.1 $RPM_BUILD_ROOT%{_mandir}/man1/exifcom.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGES

%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
