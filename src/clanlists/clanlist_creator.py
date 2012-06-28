import sys
import os.path
import lxml.html
from optparse import OptionParser
from clanlists.check_server import check_server_availability
from modules.filetools import ensure_dir, settings

SETTINGS_FILE_NAME = 'clanlist_settings.ini'
mypath = os.path.abspath(os.path.split(sys.argv[0])[0]) + '/clanlists'

def make_clanlist(server, start=None):
    
    check_server_availability(server, 'clanlist')
    
    if not start:
        try:
            with open(mypath + '/' + server.upper() + '_clans.lst', mode='r', encoding='utf_8') as clanlist:
                l = clanlist.readlines()
            start = int(l[-1].split('\t')[0]) + 1
        except:
            start = 1 + settings(mypath + '/' + SETTINGS_FILE_NAME)[server.upper() + '_clan_index_shift']
    
    url = settings(mypath + '/' + SETTINGS_FILE_NAME)[server.upper() + '_clan_page_link']

    i = start
    c = True
    while c:
        try:
            c = lxml.html.parse(url+str(i)+'/')
            known_404 = None
        except:
            known_404s = settings(mypath + '/' + SETTINGS_FILE_NAME)[server.upper() + '_known_404']
            if isinstance(known_404s, int):
                if i == settings(mypath + '/' + SETTINGS_FILE_NAME)[server.upper() + '_known_404']:
                    known_404 = True
            elif isinstance(known_404s, list) or isinstance(known_404s, tuple):
                if i in settings(mypath + '/' + SETTINGS_FILE_NAME)[server.upper() + '_known_404']:
                    known_404 = True
            c = False
        if c and not known_404:
            t = c.find(".//title").text
            if settings(mypath + '/' + SETTINGS_FILE_NAME)[server.upper() + '_disbanded'] not in t :
                tag_name = t[:-settings(mypath + '/' + SETTINGS_FILE_NAME)[server.upper() + '_clan_page_trim']]
                tag_end = tag_name.find(']')
                clan_tag = tag_name[1:tag_end]
                clan_name = tag_name[tag_end+2:]
                print('\rProcessing clan: # {0} [{1}]'.format(i,clan_tag).ljust(67),end='')
                with open(mypath + '/' + server.upper() + '_clans.lst', mode='a', encoding='utf_8') as clanlist:
                    clanlist.write('{0}\t{1}\t{2}\n'.format(i,clan_tag,clan_name))
        if known_404:
            c = True
        i += 1

    print('\nDONE.')

if __name__ == "__main__":
    pass
