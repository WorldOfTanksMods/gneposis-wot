WOT-XVM FULL Pack v2.4.1 for gneposis-wot
=========================================

ABOUT
-----

This mod allows you to customize your view in World of Tanks. Plus it allows you to get ingame statistics.

Check: <https://github.com/gneposis/gneposis-wot/raw/master/mods/wot-xvm/xvm-doc/screenshot.jpg>
                         
INSTALLATION               
------------
1. Follow original install instructions:

    1. Game must be installed to disk with NTFS file system.
    
    2. Microsoft .NET Framework 2.0 is required.
       You can check your installed .NET versions using this utility:
         http://www.tmgdevelopment.co.uk/versioncheck.htm
    
    3. Install DokanLibrary: http://dokan-dev.net/en/download/#dokan
    
    4. Unzip archive to game folder:
       Right click to archive -> "Exctract all..." -> select game folder -> "Extract"
    
    5. You do not need to setup anything by default.
    
       If you want special settings, you need to create config file:
         \res_mods\<game version>\gui\flash\XVM.xvmconf
    
       You can select ready config file from \xvm-doc\samples\ directory(*), or use
       online editor: https://sites.google.com/site/sirmaxwiki/xvm-editor
    
       Old OTMData.xml configs are also supported in legacy mode, you can use if if
       you do not need new features.
    
       All possible config options you can see in this file:
         \xvm-doc\samples\Full config EN\XVM.xvmconf
    
       Note: If you changing config manually, use Notepad, DO NOT use MS Word,
       WordPad and such editors.
    
    6. If you do not want statistics, run game as usual.
    
       If you want statistics, run wot-xvm-proxy.exe (game will be started
       automatically). Also make a note that statistics is turned off by default,
       so you need to enable it in config file.
    
       If you want statistics and game launcher, start with /launcher argument:
         Create shortcut wot-xvm-proxy.exe
         Open Properties
         Write 'wot-xvm-proxy.exe /launcher' (without quotas) in Object field
         Press OK
    
    7. If you use Skype, in Tools -> Options -> Advanced -> Connection ->
       REMOVE CHECK "Use port 80 and 443 as alternatives for incoming connections".
    
    8. If you want to send bug report, run wot-xvm-proxy.exe with /debug argument
       and add console output to report.

2. Copy all the the content of the current folder to the 'res_mods' folder of your World of Tanks install. Don't forget to make backups of your 'res_mods' folder regularly.

(*) : I moved the content of that directory to '\res_mods\<game version>\gui\flash\configs'

Contents
--------
    wot-xvm-proxy.exe : the little softwer which manages game data flow
    wot-xvm-proxy.exe.config : it's config file; it needs to be updated regularly
    xvm-doc\* :  documentations
    res_mods\<game version>\gui\flash\* : the xvm-modified game files
    res_mods\<game version>\gui\flash\config\* : sample configs
                                                            
Tools Used
----------                     
3b37ff884ee2a786d22360f1d6b9edec9d39bc5e *xvm-full-2.4.1.zip

License
-------
The following license applies to wot-xvm: GNU GPL v3, <http://www.gnu.org/licenses/gpl.html>