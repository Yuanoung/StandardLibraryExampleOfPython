#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os.path

PATHS = [
    '/one/two/three',
    '/one/two/three/',
    '/',
    '.',
    '',
]

for path in PATHS:
    print('{!r:>17} : {}'.format(path, os.path.dirname(path)))
