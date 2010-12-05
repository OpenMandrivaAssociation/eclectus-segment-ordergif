Summary:	Han character dictionary
Name:		eclectus-segment-ordergif
Version:	0.2
Release:	%mkrel 2
Group:		Development/Python
License:	GPLv3+
URL:		http://code.google.com/p/eclectus/
Source0:	http://eclectus.googlecode.com/files/order.gif-%{version}beta.tar.gz
BuildArch:	noarch
Requires:	eclectus
BuildRoot:      %{_tmppath}/%{name}-%{version}-buildroot

%description
Eclectus is a small Han character dictionary especially designed for
learners of Chinese character based languages like Mandarin Chinese
or Japanese.

%prep
%setup -qn order.gif-%{version}beta

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_datadir}/eclectus/order.gif/
cp -fr *.gif %{buildroot}%{_datadir}/eclectus/order.gif

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_datadir}/eclectus/order.gif
