import os
from modules.reformat import trim

def ensure_dir(f):
    # Code is from: http://stackoverflow.com/questions/273192/python-best-way-to-create-directory-if-it-doesnt-exist-for-file-write
    '''Creates directory for output file if not exits.'''
    if not os.path.exists(f):
        os.makedirs(f)
    return f    

def settings(settingsfile):
    def convert_setting(s, splitter=','):
        if len(s.split(splitter)) == 1:
            try:
                return int(trim(s))
            except:
                if trim(s).lower() == 'true':
                    return True
                elif trim(s).lower() == 'false':
                    return False
                elif trim(s) == '':
                    return None
                else:
                    return trim(s)
        else:
            try:
                return [ int(trim(x)) for x in s.split(splitter)]
            except:
                return [ trim(x) for x in s.split(splitter)]
    d = {}
    with open(settingsfile, encoding='utf_8') as settings:
        content = settings.readlines()
    for l in content:
        # we skip empty lines and lines which are starting with '#':
        if l.lstrip() != '': 
            if l.lstrip()[0] != '#':
                # to trim newline character at the end:
                l = l[:-1]                   
                d[trim(l.split('=')[0])] = convert_setting(trim(l.split('=')[1]))
    return d