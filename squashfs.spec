%define	snap	20091213
Summary:	Set of tools which creates squashfs filesystem
Summary(pl.UTF-8):	Zestaw narzędzi do tworzenia systemu plików squashfs
Name:		squashfs
Version:	4.1
Release:	0.%{snap}.1
License:	GPL
Group:		Base/Utilities
# Source0:	http://dl.sourceforge.net/squashfs/%{name}%{version}.tar.gz
Source0:	%{name}-%{snap}.tar.bz2
# Source0-md5:	595391e4ae095e82214e7f96d53bc505
Source1:	http://downloads.sourceforge.net/sevenzip/lzma465.tar.bz2
# Source1-md5:	29d5ffd03a5a3e51aef6a74e9eafb759
URL:		http://squashfs.sourceforge.net/
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir	/sbin

%description
This package contains utilities for squashfs filesystem.

Squashfs is a highly compressed read-only filesystem for Linux (kernel
2.6.29 and above). It uses zlib compression to compress both files,
inodes and directories. Inodes in the system are very small and all
blocks are packed to minimise data overhead. Block sizes greater than
4K are supported up to a maximum of 64K.

Squashfs is intended for general read-only filesystem use, for
archival use (i.e. in cases where a .tar.gz file may be used), and in
constrained block device/memory systems (e.g. embedded systems) where
low overhead is needed.

%description -l pl.UTF-8
Zestaw narzędzi do tworzenia systemu plików squashfs.

Squashfs jest systemem plików tylko do odczytu z dużym współczynnikiem
kompresji dla Linuksa (2.6.29 i nowsze). Używa kompresji zlib do
plików, i-węzłów oraz katalogów. I-węzły są bardzo małe, a wszystkie
bloki są pakowane, aby zmniejszyć objętość. Rozmiary bloków powyżej
4kB są obsługiwane - maksymalnie do 64kB.

Squashfs ma służyć jako system plików tylko do odczytu ogólnego
przeznaczenia, do składowania archiwów (w tych przypadkach, kiedy
można używać plików .tar.gz) oraz w systemach z dużymi ograniczeniami
pamięci i urządzeń blokowych (np. systemach wbudowanych).

%prep
%setup -q -n %{name} -a1
sed -i -e 's#^\#LZMA_SUPPORT.*=.*#LZMA_SUPPORT=1#g' squashfs-tools/Makefile
sed -i -e "s#^LZMA_DIR.*=.*#LZMA_DIR = $(pwd)#g" squashfs-tools/Makefile

%build
%{__make} -C squashfs-tools \
	CC="%{__cc}" \
	CFLAGS="-I. -I$(pwd)/C -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_GNU_SOURCE -DLZMA_SUPPORT=1 -DCOMP_DEFAULT=\\\"gzip\\\" %{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

install -D squashfs-tools/mksquashfs $RPM_BUILD_ROOT%{_sbindir}/mksquashfs
install    squashfs-tools/unsquashfs $RPM_BUILD_ROOT%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/*
