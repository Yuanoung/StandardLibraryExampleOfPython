#!/usr/bin/env python
# -*- coding: utf-8 -*-
import string

values = {'var': 'foo'}

t = string.Template("$var is here but $misssing is not provided")

try:
    print('substitute()     :', t.substitute(values))
except KeyError as err:
    print('ERROR:', str(err))

print('safe_substitute():', t.safe_substitute(values))
