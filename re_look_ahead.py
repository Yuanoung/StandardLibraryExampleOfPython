import re

# 注释掉， 17～20行，输出的结果还是有很大的区别的
address = re.compile(
    '''
    # A name is made up of letters, and may include "."
    # for title abbreviations and middle initials.
    ((?P<name>
        ([\w.,]+\s+)*[\w.,]+
     )
     \s+
    ) # The name is no longer optional.
    
    # LOOKAHEAD
    # Email addresses are wrapped in angle brackets, but only
    # if both are present or neither is.
    (?= (<.*>$)         # Remainder wrapped in angle brackets
        |
        ([^<].*[^>]$)       # Remainder *not* wrapped in angle brackets
    )
    <? # Optional opening angle bracket
    
    # The address itself: username@domain.tld
    (?P<email>
        [\w\d.+-]+      # Username  []中， . 号不需要转义
        @
        ([\w\d.]+\.)+   # Domain name prefix  ()中， . 号需要转义
        (com|org|edu)   # Limit the allowed top-level domains.
    )
    >? # Optional closing angle bracket
    ''',
    re.VERBOSE)

candidates = [
    u'First Last <first.last@example.com>',
    u'No Brackets first.last@example.com',
    u'Open Bracket <first.last@example.com',
    u'Close Bracket first.last@example.com>',
]

for candidate in candidates:
    print('Candidate:', candidate)
    match = address.search(candidate)
    if match:
        print(' Name :', match.groupdict()['name'])
        print(' Email:', match.groupdict()['email'])
    else:
        print(' No match')
