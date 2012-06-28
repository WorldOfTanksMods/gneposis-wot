gneposis-wot v0.1.2a
====================

ABOUT
-----
This is a mod enabler and visualization tool for the free MMO game World of Tanks. You can choose of the many mod pack of collection according to your preferences.

In the pack there are and will be some of my made mods and stuff. The unique feature of this software is that it auto-downloads clan icons (current ones on global map or all of them) and puts them onto vehicle markers. 

Check: <https://github.com/gneposis/gneposis-wot/raw/master/shot1.jpg>

Gneposis-wot is a Python software which reads the settings file and make your res_mods folder based on your preferences. You can enable/disable mods in a flexible way.

Usage
-----
1. Download and install Python 3 (to its default directory) from here: <http://www.python.org/download/releases/3.2.3/>
2. Edit 'src/settings.ini' with Notepad. Check if your World of Tanks directory is set correctly
3. Start 'runme.bat'
4. Copy the contents of 'your_res_mods' to your World of Tanks' 'res_mods' folder

Check: Check: <https://github.com/gneposis/gneposis-wot/raw/master/shot2.jpg>

Extra feature: If you want cool World of Tanks related links, put a shortcut to the links folder onto your Desktop.

The package contains the following mods (all of them are 0.7.4 compatible):

* ACCURATE DAMAGEINDICATOR : The stock indicator gives you a general idea of where you were shot from. This one has a separate piece that swings to stay pointing at the shot's origin.
* BETTER MINIMAP ICONS : This mod bumpeds up the icons size by about 33% (by Pettingson)
* HD MINIMAP : This mod replaces the standard map with a high definition one (by Locastan/Shtys)
* INGAME CHAT REMOVAL : Disables in-game chat. Useful if you often get angry in random battles (by Nepumax)
* MAXIMUM ZOOM OUT : This very common mod allows you to zoom out more
* RETICLE COUNTDOWN VANILLA : The mod uses the default reticle that comes with tanks and is updated where needed. It has a reload timer and a health feature. (by Puddy70s)
* RETICLE STANDARD GREEN : Same as RETICLE COUNTDOWN VANILLA. With green text. (by STL1te)
* RETICLE STANDARD WHITE : Same as RETICLE STANDARD GREEN, but with white text. (by STL1te)
* WOT-XVM : This mod allows you to customize your view and markers in World of Tanks. By default I include the Lite version only. If you want to use the full one, you should replace the files manually. However, you can still put clan icons into full configs (even into your customized one) 

You can find link for screenshots in the README's of the the Packages in 'mods/(modpackname)' folder.

I will include more mods and more customisation in the future.

Attention!
----------
This program is in alpha state right now, so bugs may come. I tested it with RU, EU and NA clients, and it worked for all of them.

At this point it uses an eval function to parse CW region data provided by <http://wot-stats.appspot.com/>. In future release I will code a workaround for this.

It is very unlikely for someone to hack them and put a harmful code in them but if you are paranoid you can check the region data before running this program:
* RU: <http://wot-stats.appspot.com/region-data/129>
* EU: <http://wot-stats.appspot.com/region-data/257>
* NA: <http://wot-stats.appspot.com/region-data/385>

License
-------
The following license applies for my stuff only:

               DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
                       Version 2, December 2004
   
    Copyright (C) 2004 Sam Hocevar <sam@hocevar.net>
   
    Everyone is permitted to copy and distribute verbatim or modified
    copies of this license document, and changing it is allowed as long
    as the name is changed.
   
               DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
      TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION
   
     0. You just DO WHAT THE FUCK YOU WANT TO. 