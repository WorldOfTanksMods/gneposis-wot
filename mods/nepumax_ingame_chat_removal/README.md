NEPUMAX INGAME CHAT REMOVAL Pack v1.0 for gneposis-wot
======================================================

ABOUT
-----

Disables in-game chat.

Check: <https://github.com/gneposis/gneposis-wot/raw/master/mods/nepumax_ingame_chat_removal/shot1.jpg>


INSTALLATION
------------
1. Copy the content of 'res_mods' folder to the 'res_mods' folder of your World of Tanks install. Don't forget to make backups of your 'res_mods' folder regularly.

If you want to enable chat again, overwrite current file with the .default one.

Contents
--------
    res_mods/(version)/gui/messenger.xml : this file disables it
    res_mods/(version)/gui/messenger.xml : and this one enables it back if renamed

Nepumax's post
--------------
You have to do it by yourself.

1. Download WoT-Tools 0.5.
2. Once downloaded, extract them wherever you want, f. ex. in your main World of Tanks directory.
3. Go to your ...World of Tanks\res\gui folder and make a backup of messenger.xml.
4. Start wottools.exe and then open messenger.xml.
5. Scroll up and look for these lines:

    41 </lobby>
    42 <battle>
    43       <lifeTime>      10      </lifeTime>
    44       <alphaSpeed>    3       </alphaSpeed>
    45       <inactiveStateAlpha>    35      </inactiveStateAlpha>
    46       <colorScheme>
    47       <player>

6. Change 10 to 0.01 and 3 to 0.01.
7. Save it and check it ingame. Done.

If anything goes wrong, delete the messenger.xml and rename your backup

EDIT: For everybody who dislikes this: I already changed my chat time to 30 seconds with this method, so that I won't miss any messages. That's possible, too! 

Check: <http://forum.worldoftanks.eu/index.php?/topic/91750-in-game-chat-removal-option/page__view__findpost__p__1532836>
    
Tools Used
----------
jEdit 4.5 : <http://www.jedit.org/>
e06d14cfa07e8c2fd08663966ef952494a151dfc *wottools0.5.zip

License
-------
The following license applies for this stuff:

               DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
                       Version 2, December 2004
   
    Copyright (C) 2004 Sam Hocevar <sam@hocevar.net>
   
    Everyone is permitted to copy and distribute verbatim or modified
    copies of this license document, and changing it is allowed as long
    as the name is changed.
   
               DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
      TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION
   
     0. You just DO WHAT THE FUCK YOU WANT TO. 