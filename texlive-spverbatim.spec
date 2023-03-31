Name:		texlive-spverbatim
Version:	15878
Release:	2
Summary:	Allow line breaks within \verb and verbatim output
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/spverbatim
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/spverbatim.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/spverbatim.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/spverbatim.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
LaTeX's \verb macro treats its argument as an unbreakable unit
of text. This can lead to poor typesetting, especially when the
argument is long. The spverbatim package provides an \spverb
macro that is analogous to \verb and an spverbatim environment
that is analogous to verbatim with the difference being that
\spverb and spverbatim allow LaTeX to break lines at space
characters.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/spverbatim/spverbatim.sty
%doc %{_texmfdistdir}/doc/latex/spverbatim/README
%doc %{_texmfdistdir}/doc/latex/spverbatim/spverbatim.pdf
#- source
%doc %{_texmfdistdir}/source/latex/spverbatim/spverbatim.dtx
%doc %{_texmfdistdir}/source/latex/spverbatim/spverbatim.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
