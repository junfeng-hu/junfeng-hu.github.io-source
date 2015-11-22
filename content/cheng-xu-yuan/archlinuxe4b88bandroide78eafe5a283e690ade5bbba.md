Title: archlinux下android环境搭建
Date: 2012-12-10 22:56
Author: algu
Category: 程序猿
Tags: android-sdk
Slug: archlinuxe4b88bandroide78eafe5a283e690ade5bbba

由于系统中已有openjdk，就开始安装eclipse

sudo pacman -S eclipse

在选择java版本时纠结了，是选择sun-java呢，还是openjava？

刚开始选择sun-java，但网速过于慢了，就又换回了openjava

安装android-sdk，android-sdk-platform-tools无法解决依赖：

在/etc/pacman.conf中启用multilib源

sudo vim /etc/pacman.conf

安装android-sdk，android-sdk-platform-tools

sudo pacman -S android-sdk android-sdk-platform-tools

感觉文件好大啊！但到后面装eclipse-android时真的是小巫见大巫了。

android-sdk默认安装到/opt文件夹下。

使用yaourt安装eclipse-android 使用pacman无法解决依赖。

sudo yaourt  -S eclipse-android （非root用户也可以）

会下载这三个东东eclipse-emf   eclipse-gef    eclipse-wtp-wst。

平均每个都一百多M。

cd /opt/android-sdk/tools

运行android脚本启动android-sdk-manager：

./android

若遇到权限问题把/opt/android-sdk/文件夹及其所有内容的所有者改成你自己

sudo chown -R user：users /opt/android-sdk

sudo也可以。

选择android API版本下载安装。

启动eclipse，设置android-sdk路径。

android开发环境已配置完成。

###### 新建android虚拟机，测试环境：

在android-sdk-manager中找到tools-\>Manage AVDs，启动Android Virtual
Device Manager。

new新建android虚拟机。

设置参数

Start启动虚拟机

若出现问题无法启动，按照提示提供的执行命令。

若出现“fork(): Cannot allocate memory”错误，把内存调小一点试试。

启动过程较慢，以为死掉，造成关了重新启动多次。

最后出现android虚拟机：

成功

时间主要花在下载android-sdk和android-sdk-platform-tools上，学校源中无此软件包，只能在官网上下载，但官网已限速，而且多次出现下载完后，返回莫名错误。

用yaourt下载eclipse-android依赖包时也是花费较多时间。

参考：[Android(简体中文)](https://wiki.archlinux.org/index.php/Android_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87))
