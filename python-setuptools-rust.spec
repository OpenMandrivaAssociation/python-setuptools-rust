%bcond_with tests

Name:		python-setuptools-rust
Version:	1.5.1
Release:	1
Summary:	Setuptools Rust extension plugin
License:	MIT
URL:		https://github.com/PyO3/setuptools-rust
Source0:	 https://pypi.io/packages/source/s/setuptools-rust/setuptools-rust-%{version}.tar.gz
BuildArch:	noarch
ExclusiveArch:	%{rust_arches}

BuildRequires:	pkgconfig(python)
BuildRequires:	python3dist(setuptools)
BuildRequires:	python3dist(semantic-version) >= 2.6
BuildRequires:  python3dist(typing-extensions)
BuildRequires:	python3dist(toml) >= 0.9.0
BuildRequires:  python3dist(tomli)
BuildRequires:	python3dist(setuptools-scm) >= 3.4.3
BuildRequires:	python3dist(wheel)
BuildRequires:	python3dist(pip)
BuildRequires:	rust-packaging >= 1.45
Requires:	rust-packaging >= 1.45

%description
Setuptools helpers for Rust Python extensions. Compile and distribute Python
extensions written in Rust as easily as if they were written in C.

%prep
%autosetup -n setuptools-rust-%{version}
# Remove bundled egg-info
rm -rf setuptools-rust.egg-info

%build
%py_build

%install
%py_install

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
%{python_sitelib}/setuptools_rust-%{version}-py*.egg-info
