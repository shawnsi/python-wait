Name:           python-wait
Version:        0.0.3
Release:        1%{?dist}
Summary:        Python Wait

License:        MIT
Source0:        python-wait-%{version}.tar.gz

Requires:       python
BuildRequires:  python-setuptools
BuildArch:      noarch

%description
Python Wait

%prep
%setup -q -c -n python-wait-%{version}

%build
%{__python} setup.py build

%install
%{__python} setup.py install --skip-build --root $RPM_BUILD_ROOT

%files
%{python_sitelib}/wait
%{python_sitelib}/wait-*.egg-info

%changelog
* Tue Jul 14 2014 Shawn Siefkas <shawn@siefk.as> - 0.0.3-1
- Deferred Log Waits
- TCP Waits

* Mon Jul 14 2014 Shawn Siefkas <shawn@siefk.as> - 0.0.2-1
- Adding Log Existence Check

* Mon Jul 14 2014 Shawn Siefkas <shawn@siefk.as> - 0.0.1-1
- Initial Spec File
