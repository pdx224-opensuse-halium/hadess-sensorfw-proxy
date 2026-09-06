%global debug_package %{nil}
%define _build_id_links none
%undefine _missing_build_ids_terminate_build

# VERSION MUST MATCH THE SOURCE. Derive it, do not carry it forward:
#
#     git describe --tags   ->   droidian/next/0.2.1
#
# The base commit is that tag with no offset, so 0.2.1 is exact.
#
# The previous spec said 0.0.1, which corresponds to nothing upstream, so the
# version on the device could not be matched back to a source tree.
Name:           hadess-sensorfw-proxy
Version:        0.2.1
Release:        0.droid
Summary:        sensorfw to net.hadess.SensorProxy bridge
License:        GPL-3.0-or-later
URL:            https://github.com/pdx224-opensuse-halium/hadess-sensorfw-proxy
BuildArch:      aarch64
AutoReqProv:    no

%description
Exposes sensorfw's sensors on the net.hadess.SensorProxy D-Bus interface, the
one iio-sensor-proxy provides, so desktop consumers such as KWin can drive
screen auto-rotation from an Android sensor HAL.

%install
install -D -m0755 %{_sourcedir}/hadess-sensorfw-proxy \
                  %{buildroot}/usr/bin/hadess-sensorfw-proxy

%files
/usr/bin/hadess-sensorfw-proxy

%changelog
* Sun Sep 06 2026 Krzysztof Kolendowicz <koloses@gmail.com> - 0.2.1-0.droid
- Ship the spec with the source instead of generating it inside a build script
- Version 0.0.1 -> 0.2.1 to match the source (droidian/next/0.2.1)
