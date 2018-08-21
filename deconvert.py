#!/usr/bin/env python

import base64
import sys
import textwrap
import zlib

file_name = sys.argv[1]

utf = open(file_name, 'r').read().encode('utf-8')
zlib_compressed = zlib.compress(utf)
b64_encoded = base64.b64encode(zlib_compressed)
deconverted = b64_encoded.decode('ascii')

for line in textwrap.wrap(deconverted, 76):
    print(line)

