# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/spverbatim
# catalog-date 2009-11-10 00:30:52 +0100
# catalog-license lppl
# catalog-version v1.0
Name:		texlive-spverbatim
Version:	v1.0
Release:	1
Summary:	Allow line breaks within \verb and verbatim output
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/spverbatim
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/spverbatim.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/spverbatim.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/spverbatim.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
LaTeX's \verb macro treats its argument as an unbreakable unit
of text. This can lead to poor typesetting, especially when the
argument is long. The spverbatim package provides an \spverb
macro that is analogous to \verb and an spverbatim environment
that is analogous to verbatim with the difference being that
\spverb and spverbatim allow LaTeX to break lines at space
characters.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/spverbatim/spverbatim.sty
%doc %{_texmfdistdir}/doc/latex/spverbatim/README
%doc %{_texmfdistdir}/doc/latex/spverbatim/spverbatim.pdf
#- source
%doc %{_texmfdistdir}/source/latex/spverbatim/spverbatim.dtx
%doc %{_texmfdistdir}/source/latex/spverbatim/spverbatim.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
