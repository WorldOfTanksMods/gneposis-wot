import sys
import os
from distutils.dir_util import copy_tree
from modules.filetools import ensure_dir, settings
from clanlists import emblem_downloader

SETTINGS_FILE_NAME = 'settings.ini'
mypath = os.path.abspath(os.path.split(sys.argv[0])[0])
rootpath = os.path.split(mypath)[0]

class IncorrectWorldOfTanksDirectory(ValueError): pass

def wot_directory():
    wotdir = settings(mypath + '/' + SETTINGS_FILE_NAME)['World_of_Tanks_directory']
    if not os.path.exists(wotdir):
        raise IncorrectWorldOfTanksDirectory('Please set the correct World of Tanks path in {0}'.format(SETTINGS_FILE_NAME))
    return wotdir

def get_server():
    wotdir = wot_directory()
    with open(wotdir + '/res/scripts_config.xml',mode='rb') as scripts_config:
        content=scripts_config.read()
    if b'wotru' in content:
        return 'RU'
    elif b'woteu' in content:
        return 'EU'
    elif b'wotus' in content:
        return 'NA'
    else:
        return 'unknown'

def get_wot_version():
    wotdir = wot_directory()
    with open(wotdir + '/version.xml',mode='r') as f_version:
        content=f_version.read()
    loc0_temp = content.find('<version>')
    loc0 = content[loc0_temp:].find('v.') + loc0_temp + 2
    loc1 = content[loc0:].find(' ') + loc0
    return content[loc0:loc1]
        
def copy_mods():
    def modlist():
        l = []
        s = settings(mypath + '/' + SETTINGS_FILE_NAME)
        for k in s.keys():
            if k[:4] == 'mod_' and s[k] :
                l.append(k[4:])
        return l
    
    v = get_wot_version()
    
    for m in modlist():
        print('Copying mod: {0}'.format(m))
        copy_tree(rootpath + '/mods/' + m + '/res_mods/' + v, rootpath + '/your_res_mods/'+v)

def add_clanicons(clanlist):
    s = settings(mypath + '/' + SETTINGS_FILE_NAME)
    if s['mod_wot-xvm']:
        emblem_downloader.download_emblems(get_server(),clanlist,s['clanicon_size'],rootpath + '/your_res_mods/')

def make_xvmconf():
    s = settings(mypath + '/' + SETTINGS_FILE_NAME)
    s2 = settings(emblem_downloader.mypath + '/' + emblem_downloader.SETTINGS_FILE_NAME)
    
    if s['xvmconf_file']:
        xvmconffile = s['xvmconf_file']
    else:
        xvmconffile = rootpath + '/mods/wot-xvm/configs/gneposis.xvmconf'

    with open(xvmconffile,mode='r') as f_xvmconf:
        content=f_xvmconf.read()
    search_string_server = '"'+get_server()+'"'
    loc_server = content.find(search_string_server)
    loc0 = content[loc_server:].find('[\n') + loc_server + 2
    loc1_temp = content[loc0:].find(']\n') + loc0
    loc1 = content[:loc1_temp].rfind('\n')
    
    players_list = [ c.strip() for c in content[loc0:loc1].split('\n') ]
    
    nicks = []
    clans = []
    for p in players_list:
        p_splitted = p.split('"')
        try:
            if p_splitted[1] == 'nick':
                nicks.append((p_splitted[3],p_splitted[7]))
            elif p_splitted[1] == 'clan':
                clans.append(p_splitted[3][1:-1])
        except:
            pass
    
    if s['xvm_keep_clans']:
        s_clans = set(clans)
    else:
        s_clans = set()

    if s['clanicons']:
        l_clans = emblem_downloader.get_clanlist(get_server(),s['clanicons'])
    else:
        l_clans = []
    
    for i in l_clans:
        s_clans.add(i[1])
    
    new_xvmconf = content[:loc0]
    
    row_added = False
    
    if s['xvm_keep_nicks']:
        for i in nicks:
            print('\rAdding nick to XVM.xvmconf: {0}'.format(i[0]).ljust(40),end='')
            new_xvmconf = new_xvmconf + '        { "nick": "'+i[0]+'", "icon": "'+i[1]+'" },\n'
            row_added = True
    
    for i in sorted(s_clans):
        print('\rAdding clan to XVM.xvmconf: [{0}]'.format(i).ljust(40),end='')
        new_xvmconf = new_xvmconf + '        { "clan": "['+i+']", "icon": "'+i+'_'+s2['emblem_'+s['clanicon_size']]+'" },\n'
        row_added = True
    
    print('')
    
    # remove last comma, but only if no row added:
    if not row_added:
        new_xvmconf = new_xvmconf[:-1] + content[loc1:]
    else:
        new_xvmconf = new_xvmconf[:-2] + content[loc1:]
    
    v = get_wot_version()
    
    with open(rootpath + '/your_res_mods/'+v+'/gui/flash/XVM.xvmconf',mode='w') as n_xvmconf:
        n_xvmconf.write(new_xvmconf)
    
    return nicks, sorted(s_clans)

if __name__ == "__main__":
    print('\ngneposis-wot 0.1.2a by Adam Szieberth, 2012')
    print('='*67)
    print('World of Tanks server: {0}'.format(get_server()))
    print('World of Tanks version: {0}'.format(get_wot_version()))
    copy_mods()
    add_clanicons(make_xvmconf()[1])
