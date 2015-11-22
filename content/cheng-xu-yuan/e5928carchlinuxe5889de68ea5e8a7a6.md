Title: 和archlinux初接触
Date: 2012-11-22 22:49
Author: algu
Category: 程序猿
Tags: arch安装
Slug: e5928carchlinuxe5889de68ea5e8a7a6

我发现每隔一段时间都想装一下系统。今天在虚拟机里装了archlinux。用的是官方的livecd，确实是livecd，只是没有桌面环境而已。比较一下还是gentoo的livecd做的比较好，那叫一个漂亮，虽然它是最难装的。而arch的livecd就略显粗糙了，只有字符界面。由于是在virtualbox中装的，也就省了配置网络的步骤。直接分区，使用cgdisk把sda分成了两个区，一个做根，一个做home，格式化文件系统，挂载分区。然后设置好源，更新源。

\# pacstrap /mnt base base-devel ／mnt是你挂载的根分区目录。  
\# genfstab -p /mnt \>\> /mnt/etc/fstab
如果忘记这部，重启后文件系统会变成只读，不知道为什么。

    # arch-chroot /mnt 若出现“chroot failed to run command /bin/sh' no such file or directory”

     则再依次键入上面三个命令，就不知道什么时候成功了。

    一系列配置后，卸载livecd，重启，登录系统，默认只有字符界面，

    #ping www.google.com 若出现unknow host，请继续使用livecd根据archlinux-wiki设置网络。

    好像在由chroot进入新系统可能ping的通，但若不配置网络，直接重装好的系统启动，会无法联网（虚拟机选择的是NAT方式联网）。

    设置好网络后，开始安装桌面环境。

    首先安装X11

    # pacman -S xorg-server xorg-xinit xorg-utils xorg-server-utils

    我们学校的源总是差几M造成无法安装，

    无奈在/etc/pacman.d/mirrorlist加上网易的源才算把X装上。

    虚拟机不用装显卡驱动，又省了不少事。

    安装输入设备驱动

    # pacman -S xf86-input-synaptics （笔记本所需）

    安装测试环境

    # pacman -S xorg-twm xorg-xclock xterm

    启动X 之前删除～／.xinitrc文件

    startx

    可以看到启动了一些窗口

    exit关闭X。

    然后苦难的日子就开始了。

    #pacman -S gnome gnome-extra 安装gnome，全部都装了下来，占用900多M空间，

    键入 vi ~/.xinitrc 创建.xinitrc文件 写入exec gnome-session

    startx 如图

    无法启动

    #pacman -Rsn gnome 删除gnome环境

    #pacman -S kde 安装kde，全装，占用1000多M

    同样在.xinitc文件中写入 exec startkde 但X提示无法找到startkde

    无奈安装openbox窗口管理器试试。

    成功启动。

    再装e17，没成功，源里没有。

    然后装lxde ，xfce4都成功启动，但水平太低，不会配置，深感难看。

    在这几个桌面环境，图形窗口都有同样的问题：

    在浏览器中，鼠标无法滚动网页，两边都有黑框。

    然后从中午一直折腾到现在，选修课也没去上。

    再看gentoo livecd 真心叫一个漂亮。

    各种桌面环境，软件都装的不少。

    觉得自己水平太渣。

    然后想把livecd直接复制到硬盘上，直接用。以为自己想到了一个好办法。

    一搜索，发现还真行，有教程，是2007年的。

    又要一段时间不折腾了。

    参考：arch新手指南


