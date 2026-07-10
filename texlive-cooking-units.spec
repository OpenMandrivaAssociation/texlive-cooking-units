%global tl_name cooking-units
%global tl_revision 76924

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.00
Release:	%{tl_revision}.1
Summary:	Typeset and convert units for cookery books and recipes
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/cooking-units
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cooking-units.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cooking-units.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cooking-units.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides commands to typeset amounts and units consistently
and offers an easy-to-use key-value syntax to convert one unit into
another (for example 'dag' to 'g'; see the documentation for more
examples). This packages requires expl3 and xparse, translations, xfrac,
l3keys2e, and, optionally, fmtcount.

