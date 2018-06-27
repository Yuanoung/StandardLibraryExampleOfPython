import re

text = 'This is some text -- with punctuation.'
pattern = 'is'
print('Text :', text)
print('Pattern:', pattern)
m = re.match(pattern, text)  # 只从开头开始匹配
print('Match :', m)
s = re.search(pattern, text)
print('Search :', s)
