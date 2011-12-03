Summary: A program for faxing using a Class 1, 2 or 2.0 fax modem.
Name: efax
Version: 0.9a
Release: 8%{?dist}
License: GPLv2+
Group: Applications/Communications
Url: http://www.cce.com/efax/
Source: http://www.cce.com/efax/download/%{name}-%{version}-001114.tar.gz
Patch0: efax-0.9-config.patch
Patch1: efax-0.9-numlines.patch
Patch2: efax08a-time.patch
Patch3: efax-0.9-manpage.patch
Patch5: efax-0.9-nullptr.patch
Patch6: efax-0.9-misc.patch
Patch7: efax-0.9-viewcmd.patch
Patch8: efax-0.9-quote.patch
Patch9: efax-0.9-msg-va_list.patch
Patch10: efax-0.9a-001114-crash.patch

ExcludeArch: s390 s390x
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: make
Requires: netpbm-progs

%description
Efax is a small ANSI C/POSIX program that sends and receives faxes
using any Class 1, 2 or 2.0 fax modem.

You need to install efax if you want to send faxes and you have a
Class 1, 2 or 2.0 fax modem.

%prep
%setup -q -n %{name}-%{version}-001114

%patch0 -p1 -b .config
%patch1 -p1 -b .numlines
%patch2 -p1 -b .time
%patch3 -p0 -b .manpage
%patch5 -p1 -b .nullptr
%patch6 -p1 -b .misc
%patch7 -p1 -b .viewcmd
%patch8 -p1 -b .quote
%patch9 -p1 -b .msg-va_list
%patch10 -p1 -b .crash

%build
export RPM_OPT_FLAGS="-ansi $RPM_OPT_FLAGS -fno-strict-aliasing"

make %{?_smp_mflags}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_localstatedir}/spool/fax
mkdir -p %{buildroot}%{_localstatedir}/log/fax

make BINDIR=%{buildroot}%{_bindir} MANDIR=%{buildroot}%{_mandir} install

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%doc README COPYING
%{_bindir}/*
%{_mandir}/*/*
%dir %{_localstatedir}/spool/fax
%dir %{_localstatedir}/log/fax

%changelog
* Tue Jun 29 2010 Than Ngo <than@redhat.com> - 0.9a-8
- Resolves: bz#605149, rebuilt with -fno-strict-aliasing

* Thu Jan 07 2010 Than Ngo <than@redhat.com> - 0.9a-7.1115
- fix source path

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.9a-6.1115
- Rebuilt for RHEL 6

* Mon Sep 07 2009 Than Ngo <than@redhat.com> - 0.9a-6.001114
- fix a crash in efix

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9a-5.001114
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9a-4.001114
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Oct 24 2008 Than Ngo <than@redhat.com> 0.9a-3.001114
- fix efax segfaults while sending fax, thanks to Jeff Bastian

* Thu Jul 17 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.9a-2.001114
- fix license tag

* Fri Feb 15 2008 Than Ngo <than@redhat.com> 0.9a-1.001114
- 0.9a-001114

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 0.9-27.2.1
- rebuild

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 0.9-27.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 0.9-27.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Tue Jan 17 2006 Than Ngo <than@redhat.com> 0.9-27
- apply patch to fix #177892

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Wed Nov 23 2005 Than Ngo <than@redhat.com> 0.9-26
- fix for modular X #173707

* Mon Oct 10 2005 Than Ngo <than@redhat.com> 0.9-25
- use pnmtoxwd instead xloadimage which is not in the core anymore #169413
  
* Sat Mar 05 2005 Than Ngo <than@redhat.com> 0.9-24
- rebuilt

* Wed Feb 09 2005 Than Ngo <than@redhat.com> 0.9-23
- rebuilt

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue May 20 2003 Than Ngo <than@redhat.com> 0.9-19
- fix bug #79635

* Wed Nov 20 2002 Florian La Roche <Florian.LaRoche@redhat.de>
- do not build on mainframe

* Wed Aug  7 2002 Than Ngo <than@redhat.com> 0.9-16
- Fixed a bug in manpage (bug #70935)

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild
- Copyright->License

* Tue Jun 18 2002 Than Ngo <than@redhat.com> 0.9-14
- don't forcibly strip binaries
- add valid Url

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Tue Feb 26 2002 Than Ngo <than@redhat.com> 0.9-12
- rebuild in new enviroment

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Sun Jun 24 2001 Elliot Lee <sopwith@redhat.com>
- Bump release + rebuild.

* Wed Aug 30 2000 Preston Brown <pbrown@redhat.com>
- fix -l option for efix (#16898)

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Mon Jun 12 2000 Preston Brown <pbrown@redhat.com>
- FHS paths

* Thu May 11 2000 Nalin Dahyabhai <nalin@redhat.com>
- add dependency on make (bug #11268)

* Thu Feb 03 2000 Preston Brown <pbrown@redhat.com>
- add /var/spool/fax and /var/log/fax
- /usr/bin/fax not a config file.  Use .efaxrc instead.

* Wed Feb 02 2000 Cristian Gafton <gafton@redhat.com>
- fix description. Oops about the last one.

* Wed Jan 12 2000 Preston Brown <pbrown@redhat.com>
- no you didn't Cristian.  You said you did but didn't. :) I did. Now.

* Tue Jun 29 1999 Cristian Gafton <gafton@redhat.com>
- updated to 0.9 (#3808)

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 11)

* Wed Feb 24 1999 Preston Brown <pbrown@redhat.com>
- Injected new description and group.

* Tue Feb 02 1999 Preston Brown <pbrown@redhat.com>
- patch to fix null ptr dereference
- added -ansi flag; fixes efix problem (produced bad tiff files)

* Fri Dec 18 1998 Preston Brown <pbrown@redhat.com>
- bumped spec number for initial rh 6.0 build

* Tue Aug 11 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Oct 22 1997 Michael Fulbright <msf@redhat.com>
- cleaned spec file to new standard, confirmed package is up to date

* Tue Mar 25 1997 Erik Troan <ewt@redhat.com>
- Added efax-08a-64bit.patch from David Mosberger
