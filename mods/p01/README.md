p01 visualization profile v1.0 for gneposis-wot
===============================================

ABOUT
-----

Word of Tanks HUD mod I develop for myself, but I guess it has some nice features other players may like:

1. 24x24 size clan icons over vehicles. Among the previous ones all the EU clans included which are on global map at 8. June 2012.
2. HD minimap if you prefer high resolution
3. Smaller icons on minimap making easier to determine the location of a vehicle
4. Permanent server side crosshair makes you shoot better since it removes the lag part of the aiming
5. DamageIndicator Pins are to make easier to determine the direction of the incoming shoots plus it has a timer which you can use to count the moment of the next shoot (If you know the enemy tank very well). Some remarks:
   * The pin has a hole which will fit to pixel in the top center of the HUD. It is on my TODO list
   * The timer resets if you swich between arcade and strategic view
6. I replaced the default green/red colors to (black/)green/white. It is also good for colorblind people and allows me to make a consistent colored HUD.
   * black color stays for a small danger or not relevant informations
   * green color is for friends and it shows you that something is average
   * white stays for enemies or danger or extraordinary high values
7. I invented a marker which provides easy and fast informations for the player:
   1. the core of the marker is the vehicle type with huge characters
   2. below left is current HP colored black/green/white at <= 20%/50%/100%
   3. to the right is the HP value at 100%
   4. below is the HP bar
   5. below the HP bar to the left is the efficiency rating of the player colored by <= 1000/1500/infinity
   6. to the right is the amount of battles whit that particular vehicle colored by <= 100/500/infinity
   7. below everything is the vehicle icon (white for enemies)
8. If you want to know how many battles a player has you can check it using TAB or during the battle loading, since those contain the data of efficiency/total battles (colored by <= 5000/25000/infinity)
9. XVM provides a winning chance calculator (TAB), which is enabled by default

Well, I hope I make you interested! :)

You can find some screenshots in the mod folder. Just click on 'Raw' to get to 100% zoom.

INSTALLATION
------------
1. Follow installation instructions of <https://github.com/gneposis/gneposis-wot/tree/master>
2. Follow installation instructions of <https://github.com/gneposis/gneposis-wot/tree/master/mods/_all>
3. Copy the '_all/res_mods' folder to the World of Tanks folder. Overwrite all files, but don't forget to make a backup.
4. Copy the '(region)/res_mods' folder to the World of Tanks folder. Overwrite all files, but don't forget to make a backup.
5. 

Contents
--------
_all/res_mods/(version)/gui/flash/DamageIndicator.swf : Damage Indicator Pins with timer v0.1
_all/res_mods/(version)/gui/flash/Minimap.swf : Green/White Colored Minimap v1.0
_all/res_mods/(version)/gui/flash/VehicleMarkersManager.swf : Green/White Colored Vehicle Marker Icon v1.0
_all/res_mods/(version)/gui/flash/XVM.xvmconf : wot-xvm configuration file
_all/res_mods/(version)/gui/maps/ingame/aim/gun_marker_blue.dds : Server side crosshair graphic
_all/res_mods/(version)/scripts/client/Avatar.pyc : Permanent Server Side Crosshair Enabler for 0.7.3
(region)/res_mods/(version)/scripts_config.xml : Green/White Colored Tank Silhouette v1.0
 
To Do
-----

1. dot to align damage indocator
2. optional smaller icons on minimap
3. minimap pin
4. new main hud
   * big range counter to top
   * new reload and health bars
   * reload timer to bottom
6. damagepanel to the bottom centre
7. crew, modules, fire icons to the hud

Tools Used
----------

libiconv-2.dll : <http://www.sawmill.net/prerelease/libiconv-2.dll>

sharpdiff (diff.exe): <http://code.google.com/p/sharpdiff/downloads/detail?name=diff.exe&can=2&q=>

Swifty Compress & Decompress (swfcomp.exe, swfdecomp.exe): <http://www.buraks.com/swifty/swfc11.zip>

swfmill.exe : <http://swfmill.org/>

TortoiseDiff (for patch and XVM repo): <http://sourceforge.net/projects/tortoisesvn/files/Tools/1.6.7/>

Copy the above files to C:\Windows or into your $PATH if you want to manipulate swf content.

Besides of those I was using the following softwares:

jEdit 4.5 : <http://www.jedit.org/>

License
-------
The following license applies for my stuff:

               DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
                       Version 2, December 2004
   
    Copyright (C) 2004 Sam Hocevar <sam@hocevar.net>
   
    Everyone is permitted to copy and distribute verbatim or modified
    copies of this license document, and changing it is allowed as long
    as the name is changed.
   
               DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
      TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION
   
     0. You just DO WHAT THE FUCK YOU WANT TO. 