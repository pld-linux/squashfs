Summary:	Set of tools which creates squashfs filesytem
Summary(pl):	Zestaw narzêdzi do tworzenia systemu plików squashfs
Name:		squashfs
Version:	1.0
Release:	1
License:	GPL
Group:		Base/Utilities
Source0:	http://belnet.dl.sourceforge.net/sourceforge/squashfs/%{name}%{version}b.tar.gz
URL:		http://squashfs.sourceforge.net/
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir	/sbin

%description
Squashfs is a highly compressed read-only filesystem for Linux (kernel
2.4.x). It uses zlib compression to compress both files, inodes and
directories. Inodes in the system are very small and all blocks are
packed to minimise data overhead. Block sizes greater than 4K are
supported up to a maximum of 32K.

Squashfs is intended for general read-only filesystem use, for
archival use (i.e. in cases where a .tar.gz file may be used), and in
constrained block device/memory systems (e.g. embedded systems) where
low overhead is needed.

%description -l pl
Zestaw narzêdzi do tworzenia systemu plików squashfs.

%prep
%setup -q -n squashfs1.0b

%build
cd squashfs-tools
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -lz"

%install
rm -rf $RPM_BUILD_ROOT

install -D squashfs-tools/mksquashfs $RPM_BUILD_ROOT%{_sbindir}/mksquashfs

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_sbindir}
