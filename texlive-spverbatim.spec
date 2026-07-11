%global tl_name spverbatim
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Allow line breaks within \verb and verbatim output
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/spverbatim
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/spverbatim.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/spverbatim.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/spverbatim.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
LaTeX's \verb macro treats its argument as an unbreakable unit of text.
This can lead to poor typesetting, especially when the argument is long.
The spverbatim package provides an \spverb macro that is analogous to
\verb and an spverbatim environment that is analogous to verbatim with
the difference being that \spverb and spverbatim allow LaTeX to break
lines at space characters.

