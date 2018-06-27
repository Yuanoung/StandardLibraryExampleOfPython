#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pathlib

usr_local = pathlib.Path('/usr/local')
share = usr_local / '..' / 'share'
print(share.resolve())
