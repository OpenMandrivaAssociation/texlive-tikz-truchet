Name:		texlive-tikz-truchet
Version:	50020
Release:	2
Summary:	Draw Truchet tiles
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/tikz-truchet
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-truchet.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-truchet.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-truchet.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a package for LaTeX that draws Truchet tiles, as used
in Colin Beveridge's article Too good to be Truchet in issue 08
of Chalkdust.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/tikz-truchet
%{_texmfdistdir}/tex/latex/tikz-truchet
%doc %{_texmfdistdir}/doc/latex/tikz-truchet

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
