Title: Debian 环境下的 beaglebone black NFS client 配置
Date: 2014-06-07 11:36
Author: junfeng 
Category: configs
Tags: Debian,NFS

不知什么时候手贱把beaglebone black刷成了Debian(Archlinux 没刷成功), 然后就放那了.

今天要做实验, 就搭了下NFS.

NFS Server 使用 Archlinux, 配置参见[这里](https://wiki.archlinux.org/index.php/Nfs)

client 使用 Debian. 需要安装 nfs-common package

配置 BB-black 联网:

在板子下输入命令:

```shell
/sbin/route add default gw 192.168.7.1
echo "nameserver 114.114.114.114" >> /etc/resolv.conf
```

在宿主机上输入:

```shell
sudo iptables -A POSTROUTING -t nat -j MASQUERADE
echo 1 | sudo tee /proc/sys/net/ipv4/ip_forward > /dev/null
```

ping 你喜爱的网站查看是否能成功．


联网后:
`vim /etc/apt/sources.list` 添加以下几行软件源:

> deb http://mirrors.ustc.edu.cn/debian stable main contrib non-free
  deb-src http://mirrors.ustc.edu.cn/debian stable main contrib non-free
  deb http://mirrors.ustc.edu.cn/debian stable-proposed-updates main contrib non-free
  deb-src http://mirrors.ustc.edu.cn/debian stable-proposed-updates main contrib non-free

`aptitude update` 更新 packages list
执行 `aptitude -y install nfs-common` 安装 所需软件包.
然后 `mount -t nfs 192.168.7.1:/srv/nfs4/BBB nfs4` 挂载即可


参考:

* http://www.server-world.info/en/note?os=Debian_7.0&p=nfs&f=2
* https://lug.ustc.edu.cn/wiki/mirrors/help/debian



