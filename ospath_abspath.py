#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

os.chdir('/usr')
PATHS = [
    '.',
    '..',
    './one/two/three',
    '../one/two/three',
]

for path in PATHS:
    print('{!r:>21} : {!r}'.format(path, os.path.abspath(path)))
