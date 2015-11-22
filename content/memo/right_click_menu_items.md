Title: right click menu items
Date: 2015-05-16 18:42:50
Author: junfeng
Category: memo
Tags: mime, desktop
The list of program that is displayed when right-clicking on a file in PCManFM is the combination of:
mimeinfo.cache
mimeapps.list
The default program that is launched when you double-click on a file in PCManFM is (first match wins):
The one from ~/.local/share/applications/mimeapps.list
The one from ~/.local/share/applications/defaults.list
The one from /usr/local/share/applications/defaults.list
The one from /usr/share/applications/defaults.list
The first one from /usr/share/applications/mimeinfo.cache

From https://lkubaski.wordpress.com/2012/10/29/understanding-file-associations-in-lxde-and-pcmanfm/
