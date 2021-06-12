%bcond_with tests

Name:           python-setuptools-rust
Version:        0.12.1
Release:        1
Summary:        Setuptools Rust extension plugin

License:        MIT
URL:            https://github.com/PyO3/setuptools-rust
Source0:	https://files.pythonhosted.org/packages/12/22/6ba3031e7cbd6eb002e13ffc7397e136df95813b6a2bd71ece52a8f89613/setuptools-rust-%{version}.tar.gz
BuildArch:      noarch
ExclusiveArch:  %{rust_arches}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(semantic-version) >= 2.6
BuildRequires:  python3dist(toml) >= 0.9.0
BuildRequires:  python3dist(setuptools-scm) >= 3.4.3
BuildRequires:  python3dist(wheel)
BuildRequires:  rust-packaging >= 1.45
Requires:       rust-packaging >= 1.45


%description
Setuptools helpers for Rust Python extensions. Compile and distribute Python
extensions written in Rust as easily as if they were written in C.

%prep
%autosetup -n setuptools-rust-%{version}
# Remove bundled egg-info
rm -rf setuptools-rust.egg-info

%build
%py3_build

%install
%py3_install

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} \
    %{__python3} -c "from setuptools_rust import RustExtension, version"

%if %{with tests}
cd examples/tomlgen
%cargo_prep
sed -i 's/"0\.[0-9.]*"/"^0"/g' setup.cfg
PYTHONPATH=%{buildroot}%{python3_sitelib} %{__python3} setup.py build
cd ../..
%endif

	
%files
%doc README.md CHANGELOG.md
%license LICENSE
%{python3_sitelib}/setuptools_rust/
%{python3_sitelib}/setuptools_rust-%{version}-py%{python3_version}.egg-info/
	
 
