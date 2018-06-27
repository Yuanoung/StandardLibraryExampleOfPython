from re_test_patterns_groups import test_patterns

"""
    (a)+ 与 (a+) 对于 aaaa 来说是不一样的：
    (a)+, groups() -> a,
    (a+), groups() -> aaaa
"""
test_patterns(
    'abbaabbba',
    [(r'a((a+)|(b+))', 'a then seq. of a or seq. of b'),  # 没有匹配则为None,而不是为空字符串
     (r'a((a|b)+)', 'a then seq. of [ab]')],
)
