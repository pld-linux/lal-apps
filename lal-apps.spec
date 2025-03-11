# TODO: CUDA (on bcond)
Summary:	LAL Applications
Summary(pl.UTF-8):	Aplikacje LAL
Name:		lal-apps
Version:	10.0.0
Release:	3
License:	GPL v2+
Group:		Libraries
Source0:	http://software.igwn.org/lscsoft/source/lalsuite/lalapps-%{version}.tar.xz
# Source0-md5:	0bfc74f188a40dd0a5e633478dc18b77
Patch0:		%{name}-env.patch
URL:		https://wiki.ligo.org/Computing/LALSuite
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.11
BuildRequires:	cfitsio-devel
BuildRequires:	fftw3-devel >= 3
BuildRequires:	fftw3-single-devel >= 3
BuildRequires:	gsl-devel >= 1.13
BuildRequires:	help2man >= 1.37
BuildRequires:	lal-devel >= 7.5.0
BuildRequires:	lal-burst-devel >= 2.0.0
BuildRequires:	lal-frame-devel >= 3.0.0
BuildRequires:	lal-inference-devel >= 4.1.0
BuildRequires:	lal-inspiral-devel >= 5.0.0
BuildRequires:	lal-metaio-devel >= 4.0.0
BuildRequires:	lal-pulsar-devel >= 6.0.0
BuildRequires:	lal-simulation-devel >= 5.4.0
BuildRequires:	libframe-devel >= 8.39.2
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:2
BuildRequires:	metaio-devel >= 8.4.0
BuildRequires:	octave-devel >= 1:3.2.0
BuildRequires:	pkgconfig
BuildRequires:	python3-devel >= 1:3.5
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	zlib-devel
Requires:	gsl >= 1.13
Requires:	lal >= 7.5.0
Requires:	lal-burst >= 2.0.0
Requires:	lal-frame >= 3.0.0
Requires:	lal-inference >= 4.1.0
Requires:	lal-inspiral >= 5.0.0
Requires:	lal-metaio >= 4.0.0
Requires:	lal-pulsar >= 6.0.0
Requires:	lal-simulation >= 5.4.0
Requires:	libframe >= 8.39.2
Requires:	metaio >= 8.4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Collection of gravitational wave data analysis codes and pipelines
utilising the LAL libraries.

%description -l pl.UTF-8
Zbiór programów i potoków do analizy fal grawitacyjnych przy użyciu
bibliotek LAL.

%package -n python3-lalapps
Summary:	Python LAL Apps library
Summary(pl.UTF-8):	Biblioteka LAL Apps dla Pythona
Group:		Libraries/Python
Requires:	python3-lal >= 7.5.0
Requires:	python3-lalburst >= 2.0.0
Requires:	python3-lalpulsar >= 6.0.0
Requires:	python3-ligo-lw >= 1.7.0
Requires:	python3-ligo-segments
Requires:	python3-lscsoft-glue
Requires:	python3-modules >= 1:3.5

%description -n python3-lalapps
Python LAL Apps library.

%description -n python3-lalapps -l pl.UTF-8
Biblioteka LAL Apps dla Pythona

%prep
%setup -q -n lalapps-%{version}
%patch -P 0 -p1

%build
%{__libtoolize}
%{__aclocal} -I gnuscripts
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	PYTHON=%{__python3} \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/etc/shrc.d
%{__mv} $RPM_BUILD_ROOT%{_sysconfdir}/*sh $RPM_BUILD_ROOT/etc/shrc.d

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README.md
%attr(755,root,root) %{_bindir}/lalapps_DistanceVsMass
%attr(755,root,root) %{_bindir}/lalapps_StringAddFrame
%attr(755,root,root) %{_bindir}/lalapps_StringSearch
%attr(755,root,root) %{_bindir}/lalapps_animate
%attr(755,root,root) %{_bindir}/lalapps_binj
%attr(755,root,root) %{_bindir}/lalapps_blindinj
%attr(755,root,root) %{_bindir}/lalapps_calcexpsnr
%attr(755,root,root) %{_bindir}/lalapps_calfacs
%attr(755,root,root) %{_bindir}/lalapps_cbc_stochasticbank
%attr(755,root,root) %{_bindir}/lalapps_chirplen
%attr(755,root,root) %{_bindir}/lalapps_coh_PTF_inspiral
%attr(755,root,root) %{_bindir}/lalapps_coinj
%attr(755,root,root) %{_bindir}/lalapps_effdist
%attr(755,root,root) %{_bindir}/lalapps_exc_resp
%attr(755,root,root) %{_bindir}/lalapps_fr_ninja
%attr(755,root,root) %{_bindir}/lalapps_frextr
%attr(755,root,root) %{_bindir}/lalapps_frinfo
%attr(755,root,root) %{_bindir}/lalapps_frjoin
%attr(755,root,root) %{_bindir}/lalapps_frread
%attr(755,root,root) %{_bindir}/lalapps_frview
%attr(755,root,root) %{_bindir}/lalapps_gwf2xml
%attr(755,root,root) %{_bindir}/lalapps_inspawgfile
%attr(755,root,root) %{_bindir}/lalapps_inspfrinj
%attr(755,root,root) %{_bindir}/lalapps_inspinj
%attr(755,root,root) %{_bindir}/lalapps_inspiralDistance
%attr(755,root,root) %{_bindir}/lalapps_makeblindinj
%attr(755,root,root) %{_bindir}/lalapps_makeblindinj_himass
%attr(755,root,root) %{_bindir}/lalapps_ninja
%attr(755,root,root) %{_bindir}/lalapps_power
%attr(755,root,root) %{_bindir}/lalapps_random_bank
%attr(755,root,root) %{_bindir}/lalapps_randombank
%attr(755,root,root) %{_bindir}/lalapps_spininj
%attr(755,root,root) %{_bindir}/lalapps_splitbank
%attr(755,root,root) %{_bindir}/lalapps_tmpltbank
%attr(755,root,root) %{_bindir}/lalapps_version
%attr(755,root,root) %{_bindir}/lalapps_xtefitstoframe
# wrappers for lal tools
%attr(755,root,root) %{_bindir}/lalapps_cache
%attr(755,root,root) %{_bindir}/lalapps_fftw_wisdom
%attr(755,root,root) %{_bindir}/lalapps_fftwf_wisdom
%attr(755,root,root) %{_bindir}/lalapps_tconvert
# wrappers for lalpulsar tools
%attr(755,root,root) %{_bindir}/lalapps_ComputeAntennaPattern
%attr(755,root,root) %{_bindir}/lalapps_ComputeFstatBenchmark
%attr(755,root,root) %{_bindir}/lalapps_ComputeFstatLatticeCount
%attr(755,root,root) %{_bindir}/lalapps_ComputeFstatMCUpperLimit
%attr(755,root,root) %{_bindir}/lalapps_ComputeFstatistic_v2
%attr(755,root,root) %{_bindir}/lalapps_ComputePSD
%attr(755,root,root) %{_bindir}/lalapps_CopySFTs
%attr(755,root,root) %{_bindir}/lalapps_DriveHoughMulti
%attr(755,root,root) %{_bindir}/lalapps_FstatMetric_v2
%attr(755,root,root) %{_bindir}/lalapps_HierarchSearchGCT
%attr(755,root,root) %{_bindir}/lalapps_HierarchicalSearch
%attr(755,root,root) %{_bindir}/lalapps_MakeSFTs
%attr(755,root,root) %{_bindir}/lalapps_Makefakedata_v4
%attr(755,root,root) %{_bindir}/lalapps_Makefakedata_v5
%attr(755,root,root) %{_bindir}/lalapps_PredictFstat
%attr(755,root,root) %{_bindir}/lalapps_PrintDetectorState
%attr(755,root,root) %{_bindir}/lalapps_SFTclean
%attr(755,root,root) %{_bindir}/lalapps_SFTvalidate
%attr(755,root,root) %{_bindir}/lalapps_Weave
%attr(755,root,root) %{_bindir}/lalapps_WeaveCompare
%attr(755,root,root) %{_bindir}/lalapps_WeaveConcat
%attr(755,root,root) %{_bindir}/lalapps_WeaveSetup
%attr(755,root,root) %{_bindir}/lalapps_WriteSFTsfromSFDBs
%attr(755,root,root) %{_bindir}/lalapps_compareFstats
%attr(755,root,root) %{_bindir}/lalapps_compareSFTs
%attr(755,root,root) %{_bindir}/lalapps_create_solar_system_ephemeris
%attr(755,root,root) %{_bindir}/lalapps_create_time_correction_ephemeris
%attr(755,root,root) %{_bindir}/lalapps_dumpSFT
%attr(755,root,root) %{_bindir}/lalapps_fits_header_getval
%attr(755,root,root) %{_bindir}/lalapps_fits_header_list
%attr(755,root,root) %{_bindir}/lalapps_fits_overview
%attr(755,root,root) %{_bindir}/lalapps_fits_table_list
%attr(755,root,root) %{_bindir}/lalapps_heterodyne_pulsar
%attr(755,root,root) %{_bindir}/lalapps_pulsar_crosscorr_v2
%attr(755,root,root) %{_bindir}/lalapps_pulsar_frequency_evolution
%attr(755,root,root) %{_bindir}/lalapps_pulsar_parameter_estimation_nested
%attr(755,root,root) %{_bindir}/lalapps_spec_avg
%attr(755,root,root) %{_bindir}/lalapps_spec_avg_long
%attr(755,root,root) %{_bindir}/lalapps_spec_coherence
%attr(755,root,root) %{_bindir}/lalapps_splitSFTs
%attr(755,root,root) %{_bindir}/lalapps_ssbtodetector
%attr(755,root,root) %{_bindir}/lalapps_synthesizeBstatMC
%attr(755,root,root) %{_bindir}/lalapps_synthesizeLVStats
%attr(755,root,root) %{_bindir}/lalapps_synthesizeTransientStats
%{_datadir}/lalapps
/etc/shrc.d/lalapps-user-env.csh
/etc/shrc.d/lalapps-user-env.fish
/etc/shrc.d/lalapps-user-env.sh
%{_mandir}/man1/lalapps_frextr.1*
%{_mandir}/man1/lalapps_frinfo.1*
%{_mandir}/man1/lalapps_frjoin.1*
%{_mandir}/man1/lalapps_frread.1*
%{_mandir}/man1/lalapps_mkcalfac.1*
%{_mandir}/man1/lalapps_mkcalref.1*
%{_mandir}/man1/lalapps_power.1*
%{_mandir}/man1/lalapps_ring.1*

%files -n python3-lalapps
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/lalapps_cafe
%attr(755,root,root) %{_bindir}/lalapps_cosmicstring_pipe
%attr(755,root,root) %{_bindir}/lalapps_power_likelihood_pipe
%attr(755,root,root) %{_bindir}/lalapps_power_pipe
%attr(755,root,root) %{_bindir}/lalapps_string_apply_vetoes
%attr(755,root,root) %{_bindir}/lalapps_string_calc_likelihood
%attr(755,root,root) %{_bindir}/lalapps_string_contour_plotter
%attr(755,root,root) %{_bindir}/lalapps_string_contour_plotter_largeloops
%attr(755,root,root) %{_bindir}/lalapps_string_cs_gamma
%attr(755,root,root) %{_bindir}/lalapps_string_cs_gamma_largeloops
%attr(755,root,root) %{_bindir}/lalapps_string_final
%attr(755,root,root) %{_bindir}/lalapps_string_meas_likelihood
%attr(755,root,root) %{_bindir}/lalapps_string_plot_binj
%attr(755,root,root) %{_bindir}/lalapps_string_plot_likelihood
# wrappers for lal python tools
%attr(755,root,root) %{_bindir}/lalapps_path2cache
%attr(755,root,root) %{_bindir}/lalapps_searchsum2cache
# wrappers for lalpulsar python tools
%attr(755,root,root) %{_bindir}/lalapps_MakeSFTDAG
%attr(755,root,root) %{_bindir}/lalapps_combine_crosscorr_toplists
%attr(755,root,root) %{_bindir}/lalapps_create_solar_system_ephemeris_python
%attr(755,root,root) %{_bindir}/lalapps_knope
%attr(755,root,root) %{_bindir}/lalapps_knope_automation_script
%attr(755,root,root) %{_bindir}/lalapps_knope_collate_results
%attr(755,root,root) %{_bindir}/lalapps_knope_result_page
%attr(755,root,root) %{_bindir}/lalapps_run_pulsar_crosscorr_v2
%dir %{py3_sitedir}/lalapps
%{py3_sitedir}/lalapps/*.py
%{py3_sitedir}/lalapps/__pycache__
