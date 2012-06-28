import sys
import os
import urllib.request
from clanlists.check_server import check_server_availability
from modules.filetools import settings

SETTINGS_FILE_NAME = 'clanlist_settings.ini'
mypath = os.path.abspath(os.path.split(sys.argv[0])[0]) + '/clanlists'

def get_dic(url):
	with urllib.request.urlopen(url) as u:
	    s = u.read().decode('utf-8')
	    s = s.replace('null', 'None')
	    s = s.replace('true', 'True')
	    s = s.replace('false', 'False')
	return eval(s)

def get_cw_clans(server):
    check_server_availability(server, 'uc')
    d = get_dic(settings(mypath + '/' + SETTINGS_FILE_NAME)['region_data_url'] + str(settings(mypath + '/' + SETTINGS_FILE_NAME)[server.upper() + '_regions'][0]))
    l = []
    d_clans = d['clans']
    for i in d_clans:
        l.append((d_clans[i]['id'],d_clans[i]['tag']))
    return tuple(l)
