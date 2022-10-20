# Generated from parser-3.1.2.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name parser

Name: rubygem-%{gem_name}
Version: 3.1.2.1
Release: 1%{?dist}
Summary: A Ruby parser written in pure Ruby
License: MIT
URL: https://github.com/whitequark/parser
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 2.0.0
# BuildRequires: rubygem(racc) = 1.4.15
# BuildRequires: rubygem(cliver) >= 0.3.2
# BuildRequires: rubygem(cliver) < 0.4
# BuildRequires: rubygem(yard)
# BuildRequires: rubygem(kramdown)
BuildRequires: rubygem(minitest) >= 5.10
# BuildRequires: rubygem(gauntlet)
BuildArch: noarch

%description
A Ruby parser written in pure Ruby.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version}

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

%check
pushd .%{gem_instdir}
ruby -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
popd

%files
%dir %{gem_instdir}
%{_bindir}/ruby-parse
%{_bindir}/ruby-rewrite
%license %{gem_instdir}/LICENSE.txt
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/parser.gemspec

%changelog
* Thu Oct 20 2022 Pavel Valena <pvalena@redhat.com> - 3.1.2.1-1
- Initial package
