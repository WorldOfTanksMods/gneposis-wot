import sys
import os
from modules.filetools import settings

class NotValidServer(ValueError): pass

SETTINGS_FILE_NAME = 'clanlist_settings.ini'
mypath = os.path.abspath(os.path.split(sys.argv[0])[0]) + '/clanlists'

def check_server_availability(server, criteria):
    if server.upper() not in settings(mypath + '/' + SETTINGS_FILE_NAME)[criteria + '_available_servers']:
        raise NotValidServer('This server is not valid: {0}'.format(server))
