# These and other macros are documented in dhd/droid-hal-device.inc
# Feel free to cleanup this file by removing comments, once you have memorised them ;)

%define device cedric
%define vendor motorola
%define droid_target_aarch64 1
%define straggler_files\
/bugreports\
/d\
/sdcard\
%{nil}
%define vendor_pretty Motorola
%define device_pretty Moto g5

%define installable_zip 1

%include rpm/dhd/droid-hal-device.inc

# IMPORTANT if you want to comment out any macros in your .spec, delete the %
# sign, otherwise they will remain defined! E.g.:
#define some_macro "I'll not be defined because I don't have % in front"

