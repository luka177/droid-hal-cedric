# These and other macros are documented in dhd/droid-hal-device.inc
# Feel free to cleanup this file by removing comments, once you have memorised them ;)

%define device cedric
%define vendor motorola

%define vendor_pretty Motorola
%define device_pretty Moto G5

%define installable_zip 1

%define straggler_files \
/bugreports \
/d \
/sdcard \
/file_contexts.bin \
/property_contexts \
/selinux_version \
/service_contexts \
/vendor \


 %define android_config \
  #define WANT_ADRENO_QUIRKS 1\
 %{nil}

%include rpm/dhd/droid-hal-device.inc

# IMPORTANT if you want to comment out any macros in your .spec, delete the %
# sign, otherwise they will remain defined! E.g.:
#define some_macro "I'll not be defined because I don't have % in front"

