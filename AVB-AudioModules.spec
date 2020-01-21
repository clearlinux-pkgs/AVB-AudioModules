#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : AVB-AudioModules
Version  : 4.2.0
Release  : 4
URL      : https://github.com/intel/AVB-AudioModules/archive/v4.2.0/AVB-AudioModules-4.2.0.tar.gz
Source0  : https://github.com/intel/AVB-AudioModules/archive/v4.2.0/AVB-AudioModules-4.2.0.tar.gz
Summary  : Common audio modules
Group    : Development/Tools
License  : BSD-3-Clause
Requires: AVB-AudioModules-data = %{version}-%{release}
Requires: AVB-AudioModules-lib = %{version}-%{release}
Requires: AVB-AudioModules-license = %{version}-%{release}
BuildRequires : boost-dev
BuildRequires : buildreq-cmake
BuildRequires : pkgconfig(alsa)
BuildRequires : pkgconfig(automotive-dlt)
BuildRequires : pkgconfig(sndfile)
BuildRequires : tbb-dev

%description
# AVB-AudioModules
Instruction for installation in Clearlinux
1. mkdir build & cd build
2. cmake -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_INSTALL_LIBDIR=/usr/lib64 ../
3. make
4. sudo make install

%package data
Summary: data components for the AVB-AudioModules package.
Group: Data

%description data
data components for the AVB-AudioModules package.


%package dev
Summary: dev components for the AVB-AudioModules package.
Group: Development
Requires: AVB-AudioModules-lib = %{version}-%{release}
Requires: AVB-AudioModules-data = %{version}-%{release}
Provides: AVB-AudioModules-devel = %{version}-%{release}
Requires: AVB-AudioModules = %{version}-%{release}

%description dev
dev components for the AVB-AudioModules package.


%package lib
Summary: lib components for the AVB-AudioModules package.
Group: Libraries
Requires: AVB-AudioModules-data = %{version}-%{release}
Requires: AVB-AudioModules-license = %{version}-%{release}

%description lib
lib components for the AVB-AudioModules package.


%package license
Summary: license components for the AVB-AudioModules package.
Group: Default

%description license
license components for the AVB-AudioModules package.


%prep
%setup -q -n AVB-AudioModules-4.2.0
cd %{_builddir}/AVB-AudioModules-4.2.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1579637346
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake .. -DCMAKE_INSTALL_LIBDIR=%{_lib}
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1579637346
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/AVB-AudioModules
cp %{_builddir}/AVB-AudioModules-4.2.0/LICENSE.txt %{buildroot}/usr/share/package-licenses/AVB-AudioModules/bec8feed5d6152624b747f316dcbcae24a3b9a94
pushd clr-build
%make_install
popd
## install_append content
mkdir -p %{buildroot}/usr/share/cmake/
mv %{buildroot}/usr/lib64/ias-audio-common/ %{buildroot}/usr/share/cmake/
## install_append end

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/alsa/alsa.conf.d/50-smartx.conf
/usr/share/cmake/*

%files dev
%defattr(-,root,root,-)
/usr/include/avbaudiomodules/audio/common/IasAudioCommonTypes.hpp
/usr/include/avbaudiomodules/audio/common/audiobuffer/IasMemoryAllocator.hpp
/usr/include/avbaudiomodules/audio/common/audiobuffer/IasMetaData.hpp
/usr/include/avbaudiomodules/audio/common/audiobuffer/IasMetaDataFactory.hpp
/usr/include/avbaudiomodules/audio/common/audiobuffer/IasUserMetaDataFactory.hpp
/usr/include/avbaudiomodules/internal/audio/common/IasAlsaTypeConversion.hpp
/usr/include/avbaudiomodules/internal/audio/common/IasAudioLogging.hpp
/usr/include/avbaudiomodules/internal/audio/common/IasCommonVersion.hpp
/usr/include/avbaudiomodules/internal/audio/common/IasDataProbe.hpp
/usr/include/avbaudiomodules/internal/audio/common/IasDataProbeHelper.hpp
/usr/include/avbaudiomodules/internal/audio/common/IasFdSignal.hpp
/usr/include/avbaudiomodules/internal/audio/common/IasIntProcCondVar.hpp
/usr/include/avbaudiomodules/internal/audio/common/IasIntProcMutex.hpp
/usr/include/avbaudiomodules/internal/audio/common/alsa_smartx_plugin/IasAlsaHwConstraintsDynamic.hpp
/usr/include/avbaudiomodules/internal/audio/common/alsa_smartx_plugin/IasAlsaHwConstraintsStatic.hpp
/usr/include/avbaudiomodules/internal/audio/common/alsa_smartx_plugin/IasAlsaPluginIpc.hpp
/usr/include/avbaudiomodules/internal/audio/common/alsa_smartx_plugin/IasAlsaPluginShmConnection.hpp
/usr/include/avbaudiomodules/internal/audio/common/alsa_smartx_plugin/IasSmartXPluginIpcStructures.hpp
/usr/include/avbaudiomodules/internal/audio/common/audiobuffer/IasAudioIpc.hpp
/usr/include/avbaudiomodules/internal/audio/common/audiobuffer/IasAudioIpcMessageContainer.hpp
/usr/include/avbaudiomodules/internal/audio/common/audiobuffer/IasAudioIpcProtocolHead.hpp
/usr/include/avbaudiomodules/internal/audio/common/audiobuffer/IasAudioIpcProtocolMacro.hpp
/usr/include/avbaudiomodules/internal/audio/common/audiobuffer/IasAudioIpcProtocolTail.hpp
/usr/include/avbaudiomodules/internal/audio/common/audiobuffer/IasAudioRingBuffer.hpp
/usr/include/avbaudiomodules/internal/audio/common/audiobuffer/IasAudioRingBufferFactory.hpp
/usr/include/avbaudiomodules/internal/audio/common/audiobuffer/IasAudioRingBufferMirror.hpp
/usr/include/avbaudiomodules/internal/audio/common/audiobuffer/IasAudioRingBufferReal.hpp
/usr/include/avbaudiomodules/internal/audio/common/audiobuffer/IasAudioRingBufferResult.hpp
/usr/include/avbaudiomodules/internal/audio/common/audiobuffer/IasAudioRingBufferTypes.hpp
/usr/include/avbaudiomodules/internal/audio/common/helper/IasCopyAudioAreaBuffers.hpp
/usr/include/avbaudiomodules/internal/audio/common/helper/IasIRunnable.hpp
/usr/include/avbaudiomodules/internal/audio/common/helper/IasThread.hpp
/usr/include/avbaudiomodules/internal/audio/common/samplerateconverter/IasSrcController.hpp
/usr/include/avbaudiomodules/internal/audio/common/samplerateconverter/IasSrcFarrow.hpp
/usr/include/avbaudiomodules/internal/audio/common/samplerateconverter/IasSrcWrapper.hpp
/usr/include/avbaudiomodules/internal/audio/common/samplerateconverter/IasSrcWrapperBase.hpp
/usr/lib64/libias-audio-common.so
/usr/lib64/pkgconfig/AudioCommon.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/alsa-lib/libasound_module_pcm_smartx.so
/usr/lib64/alsa-lib/libasound_module_rate_smartx.so
/usr/lib64/libias-audio-common.so.4
/usr/lib64/libias-audio-common.so.4.2.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/AVB-AudioModules/bec8feed5d6152624b747f316dcbcae24a3b9a94
