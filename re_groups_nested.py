from re_test_patterns_groups import test_patterns

# a((a*)(b*))
# match.groups(),   首先显示
# ((a*)(b*))        接着显示
# (a*) 可为空字符串   然后显示
# (b*)
test_patterns(
    'abbaabbba',
    [(r'a((a*)(b*))', 'a followed by 0-n a and 0-n b')],
)
