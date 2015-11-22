Title: vps下lnmp配置 
Date: 2014-01-10 00:37
Author: algu
Category: 程序猿
Tags: mysqld, vps(128MB)
Slug: vpse4b88blnmpe9858de7bdae

换了hostigation的vps(128MB)之后，试了Debian，Ubuntu较新的版本都不行，总是提示说MySQL安装失败,最后不得已换上ubuntu
10.04勉强把mysql装上,但网站连接十次要有9次连不上。知道是肯定是那装的那些软件版本太低，bug太多。但还是没管它。

最近得有空闲时间，决定把问题给解决。  
备份整个数据库：


    mysqldump -p -u --all-databases > all.sql

备份归档wordpress目录,nginx配置文件目录  
然后安装fedora 18

安装mysqld


    yum update #升级现有包
    yum install mysql-server #mysqld

安装mysql-server  
当启动mysqld时出现错误，无法启动。(折腾半天)  
列出包里面的文件:


    rpm -ql mysql-server

日志文件在/var/log/mysqld.log  
查看mysqld.log发现错误信息：


    vim /var/log/mysqld.log
    InnoDB: Error: pthread_create returned 11

**11 (EAGAIN)表示系统缺乏资源创建另一个线程。**  
好像是明白了，  
128MB的小内存VPS运行InnoDB直接运行不了。

用my-small.cnf替换/etc/my.cnf


    cp /usr/share/mysql/my-small.cnf /etc/my.cnf

同时修改my.cnf,在[mysqld]项下添加以下两行:


    default-storage-engine=MYISAM
    innodb=OFF

用MYISAM替换InnoDB。


    systemctl start mysqld  #没有错误
    systemctl enable mysqld #开机自启动
    /usr/bin/mysql_secure_installation #安全安装
    echo "flush privileges;" | mysql -p -u root #登陆到mysql,刷新权限,不然将出现数据库连接错误.

安装nginx


    yum install nginx
    systemctl stop httpd
    #and
    yum erase httpd
    systemctl start nginx
    systemctl enable nginx
    #恢复nginx配置文件,然后
    systemctl reload nginx #配置信息生效

安装php(注意依赖)


    yum install php-pecl-apc php-cli php-pear php-pdo php-mysqlnd php-pgsql php-pecl-mongo php-sqlite php-pecl-memcache php-pecl-memcached php-gd php-mbstring php-mcrypt php-xml php-fpm

    systemctl start php-fpm
    systemctl enable php-fpm

恢复备份的wordpress到/var/www/目录

打开网站,一切正常。  
迁移成功。  
吐槽hostigation为什么没有archlinux的虚拟系统。
