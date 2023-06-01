#
# spec file for package skelcd-control-SLE_HPC
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

%define         skelcd_name SLE_HPC

Name:           skelcd-control-%{skelcd_name}
# xsltproc for converting SLES control file to SLES-for-VMware
BuildRequires:  libxslt-tools
# xmllint (for validation)
BuildRequires:  libxml2-tools
# Added skelcd macros
BuildRequires:  yast2-installation-control >= 4.1.5

# USe FHS compliant path
Requires:       yast2 >= 4.1.41

Provides:       system-installation() = SLE_HPC
# For migrations from SLE-HPC 12
Provides:       system-installation() = SLE-HPC

#
######################################################################

Url:            https://github.com/yast/skelcd-control-SLE_HPC
AutoReqProv:    off
Version:        15.6.1
Release:        3
Summary:        SLE_HPC control file needed for installation
License:        MIT
Group:          Metapackages
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        installation.xml

# SUSEConnect does not build for i586 and s390 and is not supported on those architectures
# bsc#1088552
ExcludeArch:    %ix86 s390

%description
SLE_HPC control file needed for installation

%prep

%build
cp %{SOURCE0} .

%check
#
# Verify syntax
#
xmllint --noout --relaxng /usr/share/YaST2/control/control.rng installation.xml

%install
#
# Add installation file
#
mkdir -p $RPM_BUILD_ROOT/%{skelcd_control_datadir}
install -m 644 installation.xml $RPM_BUILD_ROOT/%{skelcd_control_datadir}/%{skelcd_name}.xml

%files
%defattr(644,root,root,755)
%{skelcd_control_datadir}

%changelog
