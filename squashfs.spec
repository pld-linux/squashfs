Summary:	Set of tools which creates squashfs filesystem
Summary(pl.UTF-8):	Zestaw narzędzi do tworzenia systemu plików squashfs
Name:		squashfs
Version:	4.3
Release:	2
License:	GPL v2+
Group:		Base/Utilities
Source0:	http://downloads.sourceforge.net/squashfs/%{name}%{version}.tar.gz
# Source0-md5:	d92ab59aabf5173f2a59089531e30dbf
URL:		http://squashfs.sourceforge.net/
BuildRequires:	attr-devel
BuildRequires:	lz4-devel
BuildRequires:	lzo-devel >= 2.04
BuildRequires:	xz-devel >= 5.0.0
BuildRequires:	zlib-devel
%ifarch %{x8664}
Requires:	libgcc_s.so.1()(64bit)
%else
Requires:	libgcc_s.so.1
%endif
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
%setup -q -n %{name}%{version}
sed -i -e 's/^#XZ_SUPPORT.*=.*/XZ_SUPPORT = 1/'  squashfs-tools/Makefile
sed -i -e 's/^#LZO_SUPPORT.*=.*/LZO_SUPPORT = 1/' squashfs-tools/Makefile
sed -i -e 's/^#LZ4_SUPPORT.*=.*/LZ4_SUPPORT = 1/' squashfs-tools/Makefile
sed -i -e "s/-O2 -Wall/%{rpmcflags}/" squashfs-tools/Makefile

%build
%{__make} -C squashfs-tools \
	CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -p squashfs-tools/mksquashfs $RPM_BUILD_ROOT%{_bindir}
install -p squashfs-tools/unsquashfs $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mksquashfs
%attr(755,root,root) %{_bindir}/unsquashfs
