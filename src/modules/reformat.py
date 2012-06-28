def trim(s):
    '''Trims leading and trailing whitespaces'''
    if s == '' : return ''
    while s[0] == ' ' and len(s) > 1:
        s = s[1:]
    while s[-1] == ' ' and len(s) > 1:
        s = s[:-1]
    if s == ' ' : return ''
    return s
        