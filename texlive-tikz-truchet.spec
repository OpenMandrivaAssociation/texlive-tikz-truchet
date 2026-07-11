%global tl_name tikz-truchet
%global tl_revision 50020

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Draw Truchet tiles
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/tikz-truchet
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-truchet.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-truchet.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-truchet.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is a package for LaTeX that draws Truchet tiles, as used in Colin
Beveridge's article Too good to be Truchet in issue 08 of Chalkdust.

