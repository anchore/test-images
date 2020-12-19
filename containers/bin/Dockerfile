FROM alpine:3.12.3

# install go 1.13, python 3.8, and busybox 1.31
# 
# note: locations derived from package installations should NOT be labeled as binary packages
#
# $ anchore-cli image content anchore/test_images:bin os
# Package                       Version                 Licenses
# busybox                       1.31.1-r19              GPL-2.0-only
# go                            1.13.15-r0              BSD-3-Clause
# python2                       2.7.18-r0               custom
# python3                       3.8.5-r0                PSF-2.0
# ...
RUN apk add --no-cache go=1.13.15-r0 python3=3.8.5-r0 python2=2.7.18-r0 busybox=1.31.1-r19

# place the test fixtures (including positive and negative examples)
#
# note: you should only see "positive" locations (not "negative")
#
# $ anchore-cli image content anchore/test_images:bin binary
# Package        Version           Location
# busybox        3.33.3            /staged/positive/busybox
# go             1.14              /staged/positive/go
# go             1.15              /staged/positive/VERSION
# python         3.6.3a-vZ9        /staged/positive/python3.6
# python         3.7.4a-vZ9        /staged/positive/libpython3.7.so
# python         3.9-aZ5           /staged/positive/patchlevel.h
# ...
COPY staged/ staged/

# lets have actual copies of the installed binaries around such that we can positively test
# the binary analyzer module against a real instance of the binary.
#
# note: we copy in python3.8, however, the binary cataloger as-is cannot detect this alone 
# but instead needs the contents of libpython*.so. For this reason we have a different version 
# of the python lib (libpython2.7.so.1.0) copied in to demonstrate this.
#
# $ anchore-cli image content anchore/test_images:bin binary
# Package        Version           Location
# busybox        1.31.1            /staged/copy/busybox
# python         2.7.18            /staged/copy/libpython2.7.so.1.0
# go             1.13.15           /staged/copy/go
# ...
RUN mkdir /staged/copy && \
    cp "$(which go)" /staged/copy && \
    cp "$(which python3.8)" /staged/copy && \
    cp /usr/lib/libpython2.7.so.1.0 /staged/copy && \
    cp "$(which busybox)" /staged/copy
