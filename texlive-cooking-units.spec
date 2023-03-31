Name:		texlive-cooking-units
Version:	65241
Release:	2
Summary:	Typeset and convert units for cookery books and recipes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/cooking-units
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cooking-units.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cooking-units.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cooking-units.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides commands to typeset amounts and units
consistently and offers an easy-to-use key-value syntax to
convert one unit into another (for example 'dag' to 'g'; see
the documentation for more examples). This packages requires
expl3 and xparse, translations, xfrac, l3keys2e, and,
optionally, fmtcount.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/cooking-units
%{_texmfdistdir}/tex/latex/cooking-units
%doc %{_texmfdistdir}/doc/latex/cooking-units

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
