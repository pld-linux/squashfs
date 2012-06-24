Summary:	Set of tools which creates squashfs filesystem
Summary(pl):	Zestaw narz�dzi do tworzenia systemu plik�w squashfs
Name:		squashfs
Version:	3.2
Release:	1
License:	GPL
Group:		Base/Utilities
Source0:	http://dl.sourceforge.net/squashfs/%{name}%{version}.tar.gz
# Source0-md5:	e4818dbd8a81519ade8a41d26587c3f5
URL:		http://squashfs.sourceforge.net/
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir	/sbin

%description
This package contains utilities for squashfs filesystem.

Squashfs is a highly compressed read-only filesystem for Linux (kernel
2.4.x and 2.6.x). It uses zlib compression to compress both files,
inodes and directories. Inodes in the system are very small and all
blocks are packed to minimise data overhead. Block sizes greater than
4K are supported up to a maximum of 64K.

Squashfs is intended for general read-only filesystem use, for
archival use (i.e. in cases where a .tar.gz file may be used), and in
constrained block device/memory systems (e.g. embedded systems) where
low overhead is needed.

%description -l pl
Zestaw narz�dzi do tworzenia systemu plik�w squashfs.

Squashfs jest systemem plik�w tylko do odczytu z du�ym wsp�czynnikiem
kompresji dla Linuksa (j�dra 2.4.x i 2.6.x). U�ywa kompresji zlib do
plik�w, i-w�z��w oraz katalog�w. I-w�z�y s� bardzo ma�e, a wszystkie
bloki s� pakowane, aby zmniejszy� obj�to��. Rozmiary blok�w powy�ej
4kB s� obs�ugiwane - maksymalnie do 64kB.

Squashfs ma s�u�y� jako system plik�w tylko do odczytu og�lnego
przeznaczenia, do sk�adowania archiw�w (w tych przypadkach, kiedy
mo�na u�ywa� plik�w .tar.gz) oraz w systemach z du�ymi ograniczeniami
pami�ci i urz�dze� blokowych (np. systemach wbudowanych).

%prep
%setup -q -n %{name}%{version}

%build
%{__make} -C squashfs-tools \
	CC="%{__cc}" \
	CFLAGS="-I. %{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

install -D squashfs-tools/mksquashfs $RPM_BUILD_ROOT%{_sbindir}/mksquashfs
install    squashfs-tools/unsquashfs $RPM_BUILD_ROOT%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *README* ACKNOWLEDGEMENTS CHANGES
%attr(755,root,root) %{_sbindir}/*
