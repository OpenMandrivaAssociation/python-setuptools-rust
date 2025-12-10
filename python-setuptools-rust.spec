%bcond_with tests

Name:		python-setuptools-rust
Version:	1.12.0
Release:	1
Summary:	Setuptools Rust extension plugin
License:	MIT
URL:		https://github.com/PyO3/setuptools-rust
Source0:	https://pypi.io/packages/source/s/setuptools_rust/setuptools_rust-%{version}.tar.gz
BuildArch:	noarch
ExclusiveArch:	%{rust_arches}

BuildSystem:	python
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(semantic-version) >= 2.6
BuildRequires:  python%{pyver}dist(typing-extensions)
BuildRequires:	python%{pyver}dist(toml) >= 0.9.0
BuildRequires:  python%{pyver}dist(tomli)
BuildRequires:	python%{pyver}dist(setuptools-scm) >= 3.4.3
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	rust-packaging >= 1.45
Requires:	rust-packaging >= 1.45

%description
Setuptools helpers for Rust Python extensions. Compile and distribute Python
extensions written in Rust as easily as if they were written in C.

%prep -a
# Remove bundled egg-info
rm -rf setuptools-rust.egg-info

%check
PYTHONPATH=%{buildroot}%{python_sitelib} \
    %{__python} -c "from setuptools_rust import RustExtension, version"

%if %{with tests}
cd examples/tomlgen
%cargo_prep
sed -i 's/"0\.[0-9.]*"/"^0"/g' setup.cfg
PYTHONPATH=%{buildroot}%{python_sitelib} %{__python} setup.py build
cd ../..
%endif

%files
%doc README.md CHANGELOG.md
%license LICENSE
%dir %{python_sitelib}/setuptools_rust
%{python_sitelib}/setuptools_rust/*
%{python_sitelib}/setuptools_rust*.*-info
