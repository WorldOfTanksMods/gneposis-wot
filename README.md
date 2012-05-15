gneposis-wot v0.001alpha  
========================

Word of Tanks HUD mod

Contents
--------

    gneposis-wot / res_mods               
    :   README.md                              : this readme
    :...0.7.3                                  
    :   :   scripts_config.xml                 : green / white silhouettes for EU server
    :   :...gui                                
    :   :   :   avatar_input_handler.xml       : for maximum zoom out
    :   :   :...flash                         
    :   :   :      DamageIndicator.swf         : for damage indicator pins
    :   :   :      XVM.xvmconf                 : green / white config
    :   :   :      XVM.xvmconf.default         : green / red config                 
    :   :   :...maps
    :   :       :...ingame
    :   :           :...aim
    :   :                  gun_marker_blue.dds : server side crosshair (german,, green)
    :   :...scripts
    :       :...client
    :              Avatar.pyc                  : auto enable server side crosshair
    :
    gneposis-wot / src :  description will be added soon...
                   
TODO
----

1. green / white vehicleicons for overtarget marker and minimap
2. dot to align damage indocator
3. smaller icons on minimap
4. minimap pin
5. new main hud
    a) big range counter to top
    b) new reload and health bars
    c) reload timer to bottom
6. damagepanel takn contour to the botoom centre
7. crew, modules, fire to the hud

Tools Used
----------
libiconv-2.dll : <http://www.sawmill.net/prerelease/libiconv-2.dll>
sharpdiff (diff.exe): <http://code.google.com/p/sharpdiff/downloads/detail?name=diff.exe&can=2&q=>
Swifty Compress & Decompress (swfcomp.exe, swfdecomp.exe): <http://www.buraks.com/swifty/swfc11.zip>
swfmill.exe : <http://swfmill.org/>
TortoiseSVN (for patch and XVM repo): <http://tortoisesvn.net/downloads.html>
Copy the above files to C:\Windows or into your $PATH if you want to manipulate content

XVM Full 2.3.rc1 (WoT client 0.7.3) : <http://code.google.com/p/wot-xvm/downloads/detail?name=xvm-full-2.3.rc1.zip&can=2&q=>