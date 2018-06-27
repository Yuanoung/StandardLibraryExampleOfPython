#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os.path

paths = ['/one/two/three/four',
         '/one/two/threefold',
         '/one/two/thre/',
         ]
for path in paths:
    print('PATH:', path)

print()
print('PREFIX:', os.path.commonprefix(paths))  # commonprefix列表中相同的字符串
