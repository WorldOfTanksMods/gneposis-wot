import sys
import os
import urllib.request
from clanlists.uc_status import get_cw_clans
from clanlists.check_server import check_server_availability
from modules.filetools import ensure_dir, settings

SETTINGS_FILE_NAME = 'clanlist_settings.ini'
mypath = os.path.abspath(os.path.split(sys.argv[0])[0]) + '/clanlists'

def get_clanlist(server, clanref):
    def get_all_clans():
        with open(mypath + '/' + server.upper() + '_clans.lst', encoding='utf_8') as all_clans:
            content = all_clans.readlines()
        return [ x[:-1].split('\t') for x in content ]
    
    if isinstance(clanref,list) or isinstance(clanref,tuple) or isinstance(clanref,set):
        content = clanref
    elif clanref.lower() == 'all':
        check_server_availability(server, 'clanlist')
        return get_all_clans()
    elif clanref.lower() == 'uc' or clanref.lower() == 'cw':
        check_server_availability(server, 'uc')
        return get_cw_clans(server)
    else:
        check_server_availability(server, 'clanlist')
        try:
            with open(clanref, encoding='utf_8') as f_clanref:
                content = f_clanref.readlines()
                content = [ x[:-1] for x in content ]
        except:
            pass
    l = []
    all_clans = get_all_clans()
    for c in content:
        i = 0
        searching = True
        while searching:
            try:
                if c.upper() == all_clans[i][1]:
                    l.append((all_clans[i][0], c.upper()))
                    searching = False
                else:
                    i += 1
            except:
                searching = False
    return tuple(l)

def get_emblem(server, clan, size):
    url = settings(mypath + '/' + SETTINGS_FILE_NAME)[server.upper() + '_emblem_link'] + str(clan[0]) + '/' +  settings(mypath + '/' + SETTINGS_FILE_NAME)['emblem_' + size.lower()]
    with urllib.request.urlopen(url) as u:
        raw_data = u.read()
    return raw_data

def download_emblems(server, clanref, size, path):
    clanlist = get_clanlist(server, clanref)
    if clanlist:
        for i in range(len(clanlist)):
            print('\rDownloading '+ size +' clan emblem: {0}/{1} ({2}%) [{3}]'.format(i+1,len(clanlist),round((i+1)/len(clanlist)*100,1),clanlist[i][1]).ljust(40),end='')
            with open(ensure_dir(path + 'clanicons/' + server.upper()) + '/' + clanlist[i][1] + '_' + settings(mypath + '/' + SETTINGS_FILE_NAME)['emblem_' + size.lower()], mode='w+b') as emblem:
                emblem.write(get_emblem(server, clanlist[i], size))
        print('')

if __name__ == "__main__":
	pass
