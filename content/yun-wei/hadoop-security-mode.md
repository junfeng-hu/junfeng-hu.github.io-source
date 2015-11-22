Title: Hadoop secure Mode配置
Date: 2015-07-25 18:55:33
Author: pfw, junfeng
Category: 运维
Tags: Hadoop, Kerberos

###介绍
老板让配Hadoop的安全模式,网上搜了些资料,
具体过程略有出入,下面记录详细配置过程,


###环境
Hadoop Version: Apache Hadoop 2.7.1

`/etc/hosts`:
```bash
192.168.1.100   hadoop1
192.168.1.101   hadoop2
192.168.1.102   hadoop3
```
hadoop1是master, 另外两台是slaves
note:**确保域名解析和反向域名解析在集群中正常工作**

`/etc/profile`:
```bash
#Hadoop
HADOOP_VERSION=2.7.1
export HADOOP_PREFIX=/opt/hadoop-${HADOOP_VERSION}
export HADOOP_HOME=${HADOOP_PREFIX}
export YARN_HOME=${HADOOP_PREFIX}
export YARN_CONF_DIR=${HADOOP_PREFIX}/etc/hadoop
export HADOOP_COMMON_LIB_NATIVE_DIR=$HADOOP_PREFIX/lib/native
export HADOOP_OPTS="-Djava.library.path=$HADOOP_PREFIX/lib"
export PATH=${HADOOP_PREFIX}/bin:${HADOOP_PREFIX}/sbin:$PATH
```
三台机器同步`/etc/hosts`和`/etc/profile`

OS: Ubuntu 14.04.2 LTS

kdc和kadmind运行在hadoop1上
###Process
首先确保非安全模式下Hadoop集群能够正常运行,
确保集群各个节点时间同步

在hadoop1上安装Kerberos:
`sudo apt-get install krb5-admin-server krb5-kdc`

运行`sudo dpkg-reconfigure krb5-kdc`重新配置Kerberos

在hadoop2, hadoop3上只需安装kerberos client:
`sudo apt-get install krb5-user krb5-config`

配置Kerberos参考[https://help.ubuntu.com/community/Kerberos][1]

关于hadoop daemons是否使用单个用户还是按照官方文档分成
hdfs,yarn,mapred取决于个人. 此处遵照官方文档.
三个用户主组是hadoop, 确保ssh无密码登录正确配置.

在Kerberos中创建服务所需principals:
按照官方文档的划分,不同服务器上的不同进程使用
不同的principal. 创建了如下这些principals:
```bash
# principals about http service, need starts with HTTP
HTTP/hadoop1@EXAMPLE.COM
HTTP/hadoop2@EXAMPLE.COM
HTTP/hadoop3@EXAMPLE.COM
# maybe used by ssh, just creates host/*
# to conform office document
host/hadoop1@EXAMPLE.COM
host/hadoop2@EXAMPLE.COM
host/hadoop3@EXAMPLE.COM
# principals about hdfs
nn/hadoop1@EXAMPLE.COM
sn/hadoop1@EXAMPLE.COM
dn/hadoop2@EXAMPLE.COM
dn/hadoop3@EXAMPLE.COM
# principals about yarn
rm/hadoop1@EXAMPLE.COM
nm/hadoop2@EXAMPLE.COM
nm/hadoop3@EXAMPLE.COM
# principal about job historyserver
jhs/hadoop1@EXAMPLE.COM
```
有些principal应该是不需要创建的,但为了防出错,也一并创建.
*需要进一步加深对Kerberos的了解*

创建keytab, keytab的主要作用是使services自动通过Kerberos认证
```bash
hdfs@hadoop1:/opt/hadoop-2.7.1/etc/keytabs$ ls
总用量 24K
-r-------- 1 hdfs   hadoop 806  7月 21 19:05 HTTP.keytab
-r-------- 1 mapred hadoop 802  7月 21 11:07 jhs.keytab
-r-------- 1 hdfs   hadoop 798  7月 21 11:05 nn.keytab
-r-------- 1 yarn   hadoop 798  7月 21 11:07 rm.keytab
-r-------- 1 hdfs   hadoop 798  7月 21 11:06 sn.keytab
```
各个keytab中内容和官方文档所列类似,如下示例:
```bash
hdfs@hadoop1:/opt/hadoop-2.7.1/etc/keytabs$ sudo klist -e -t -k nn.keytab
Keytab name: FILE:nn.keytab
KVNO Timestamp           Principal
---- ------------------- ------------------------------------------------------
   7 2015-07-20T20:39:29 nn/hadoop1@EXAMPLE.COM (aes256-cts-hmac-sha1-96)
   7 2015-07-20T20:39:29 nn/hadoop1@EXAMPLE.COM (arcfour-hmac)
   7 2015-07-20T20:39:29 nn/hadoop1@EXAMPLE.COM (des3-cbc-sha1)
   7 2015-07-20T20:39:29 nn/hadoop1@EXAMPLE.COM (des-cbc-crc)
   4 2015-07-21T11:05:54 host/hadoop1@EXAMPLE.COM (aes256-cts-hmac-sha1-96)
   4 2015-07-21T11:05:54 host/hadoop1@EXAMPLE.COM (arcfour-hmac)
   4 2015-07-21T11:05:54 host/hadoop1@EXAMPLE.COM (des3-cbc-sha1)
   4 2015-07-21T11:05:54 host/hadoop1@EXAMPLE.COM (des-cbc-crc)
```
并没有用到host/* principals

HTTP.keytab主要用于Web相关的服务, 内容如下:
```bash
hdfs@hadoop1:/opt/hadoop-2.7.1/etc/keytabs$ sudo klist -e -t -k HTTP.keytab
Keytab name: FILE:HTTP.keytab
KVNO Timestamp           Principal
---- ------------------- ------------------------------------------------------
   2 2015-07-21T19:04:19 HTTP/hadoop1@EXAMPLE.COM (aes256-cts-hmac-sha1-96)
   2 2015-07-21T19:04:19 HTTP/hadoop1@EXAMPLE.COM (arcfour-hmac)
   2 2015-07-21T19:04:19 HTTP/hadoop1@EXAMPLE.COM (des3-cbc-sha1)
   2 2015-07-21T19:04:19 HTTP/hadoop1@EXAMPLE.COM (des-cbc-crc)
   2 2015-07-21T19:04:20 HTTP/hadoop2@EXAMPLE.COM (aes256-cts-hmac-sha1-96)
   2 2015-07-21T19:04:20 HTTP/hadoop2@EXAMPLE.COM (arcfour-hmac)
   2 2015-07-21T19:04:20 HTTP/hadoop2@EXAMPLE.COM (des3-cbc-sha1)
   2 2015-07-21T19:04:20 HTTP/hadoop2@EXAMPLE.COM (des-cbc-crc)
   2 2015-07-21T19:04:20 HTTP/hadoop3@EXAMPLE.COM (aes256-cts-hmac-sha1-96)
   2 2015-07-21T19:04:20 HTTP/hadoop3@EXAMPLE.COM (arcfour-hmac)
   2 2015-07-21T19:04:20 HTTP/hadoop3@EXAMPLE.COM (des3-cbc-sha1)
   2 2015-07-21T19:04:20 HTTP/hadoop3@EXAMPLE.COM (des-cbc-crc)
```
note:**每次将某个princiapl加入keytab文件中时,Kerberos将会为该principal**
**随机生成新的密码,这样一个pricipal只能使用ktadd添加到一个keytab中,**
**可以使用ktutil合并keytab文件**

生成keytab后,分发keytab到集群中所有节点,最终如下所示:
hadoop1见上
hadoop2:
```bash
hdfs@hadoop2:/opt/hadoop-2.7.1/etc/keytabs$ ls -lh
总用量 16K
-r-------- 1 hdfs hadoop 798  7月 21 11:17 dn.keytab
-r-------- 1 hdfs hadoop 806  7月 21 19:05 HTTP.keytab
-r-------- 1 yarn hadoop 798  7月 21 11:17 nm.keytab
```
hadoop3:
```bash
hdfs@hadoop3:/opt/hadoop-2.7.1/etc/keytabs$ ls -lh
总用量 16K
-r-------- 1 hdfs hadoop 798  7月 21 13:26 dn.keytab
-r-------- 1 hdfs hadoop 806  7月 21 19:05 HTTP.keytab
-r-------- 1 yarn hadoop 798  7月 21 13:26 nm.keytab
```
slaves节点上应该用不到HTTP.keytab(未验证)

在配置Hadoop之前还需要下载JCE Unlimited Version,不然
hadoop服务无法通过验证.
官方Java 8版本的对于Java 7来说也可以正常使用.

下面开始对Hadoop进行配置:
core-site.xml:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<configuration>
  <!-- change to avoid Deprecated -->
  <property>
    <name>fs.defaultFS</name>
    <value>hdfs://hadoop1:9000</value>
  </property>
  <property>
    <name>hadoop.security.authentication</name>
    <value>kerberos</value>
  </property>
  <property>
    <name>hadoop.security.authorization</name>
    <value>true</value>
  </property>
  <property>
    <name>hadoop.security.auth_to_local</name>
    <value>
        RULE:[2:$1](nn|dn|sn)s/^.*$/hdfs/
        RULE:[2:$1](rm|nm)s/^.*$/yarn/
        RULE:[2:$1](jhs)s/^.*$/mapred/
        DEFAULT
    </value>
  </property>
  <property>
    <name>hadoop.http.authentication.type</name>
    <value>kerberos</value>
  </property>
<property>
  <name>hadoop.http.authentication.kerberos.keytab</name>
  <value>/opt/hadoop-2.7.1/etc/keytabs/HTTP.keytab</value>
</property>
<property>
  <name>hadoop.http.authentication.kerberos.principal</name>
  <value>HTTP/_HOST@EXAMPLE.COM</value>
</property>
</configuration>
```

hdfs-site.xml:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<configuration>
  <property>
    <name>dfs.namenode.name.dir</name>
    <value>/var/data/hadoop/hdfs/nn</value>
  </property>
  <property>
    <name>dfs.datanode.data.dir</name>
    <value>/var/data/hadoop/hdfs/dn</value>
  </property>
  <property>
    <name>dfs.datanode.data.dir.perm</name>
    <value>700</value>
  </property>
<property>
  <name>dfs.block.access.token.enable</name>
  <value>true</value>
</property>
<property>
  <name>dfs.web.authentication.kerberos.keytab</name>
  <value>/opt/hadoop-2.7.1/etc/keytabs/HTTP.keytab</value>
</property>
<property>
  <name>dfs.web.authentication.kerberos.principal</name>
  <value>HTTP/_HOST@EXAMPLE.COM</value>
</property>
<property>
  <name>dfs.namenode.keytab.file</name>
  <value>/opt/hadoop-2.7.1/etc/keytabs/nn.keytab</value>
</property>
<property>
  <name>dfs.namenode.kerberos.principal</name>
  <value>nn/_HOST@EXAMPLE.COM</value>
</property>
<property>
  <name>dfs.namenode.kerberos.internal.spnego.principal</name>
  <value>HTTP/_HOST@EXAMPLE.COM</value>
</property>
<property>
  <name>dfs.secondary.namenode.keytab.file</name>
  <value>/opt/hadoop-2.7.1/etc/keytabs/sn.keytab</value>
</property>
<property>
  <name>dfs.secondary.namenode.kerberos.principal</name>
  <value>sn/_HOST@EXAMPLE.COM</value>
</property>
<property>
  <name>dfs.secondary.namenode.kerberos.internal.spnego.principal</name>
  <value>HTTP/_HOST@EXAMPLE.COM</value>
</property>
<property>
  <name>dfs.datanode.address</name>
  <value>0.0.0.0:1004</value>
</property>
<property>
  <name>dfs.datanode.http.address</name>
  <value>0.0.0.0:1006</value>
</property>

<property>
  <name>dfs.datanode.keytab.file</name>
  <value>/opt/hadoop-2.7.1/etc/keytabs/dn.keytab</value>
</property>
<property>
  <name>dfs.datanode.kerberos.principal</name>
  <value>dn/_HOST@EXAMPLE.COM</value>
</property>
<!-- ACL -->
<property>
  <name>dfs.permissions.enabled</name>
  <value>true</value>
</property>
<property>
  <name>dfs.namenode.acls.enabled</name>
  <value>true</value>
</property>
</configuration>
```

yarn-site.xml
```xml
<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<configuration>
  <property>
    <name>dfs.namenode.name.dir</name>
    <value>/var/data/hadoop/hdfs/nn</value>
  </property>
  <property>
    <name>dfs.datanode.data.dir</name>
    <value>/var/data/hadoop/hdfs/dn</value>
  </property>
  <property>
    <name>dfs.datanode.data.dir.perm</name>
    <value>700</value>
  </property>
<property>
  <name>dfs.block.access.token.enable</name>
  <value>true</value>
</property>
<property>
  <name>dfs.web.authentication.kerberos.keytab</name>
  <value>/opt/hadoop-2.7.1/etc/keytabs/HTTP.keytab</value>
</property>
<property>
  <name>dfs.web.authentication.kerberos.principal</name>
  <value>HTTP/_HOST@EXAMPLE.COM</value>
</property>
<property>
  <name>dfs.namenode.keytab.file</name>
  <value>/opt/hadoop-2.7.1/etc/keytabs/nn.keytab</value>
</property>
<property>
  <name>dfs.namenode.kerberos.principal</name>
  <value>nn/_HOST@EXAMPLE.COM</value>
</property>
<property>
  <name>dfs.namenode.kerberos.internal.spnego.principal</name>
  <value>HTTP/_HOST@EXAMPLE.COM</value>
</property>
<property>
  <name>dfs.secondary.namenode.keytab.file</name>
  <value>/opt/hadoop-2.7.1/etc/keytabs/sn.keytab</value>
</property>
<property>
  <name>dfs.secondary.namenode.kerberos.principal</name>
  <value>sn/_HOST@EXAMPLE.COM</value>
</property>
<property>
  <name>dfs.secondary.namenode.kerberos.internal.spnego.principal</name>
  <value>HTTP/_HOST@EXAMPLE.COM</value>
</property>
<property>
  <name>dfs.datanode.address</name>
  <value>0.0.0.0:1004</value>
</property>
<property>
  <name>dfs.datanode.http.address</name>
  <value>0.0.0.0:1006</value>
</property>

<property>
  <name>dfs.datanode.keytab.file</name>
  <value>/opt/hadoop-2.7.1/etc/keytabs/dn.keytab</value>
</property>
<property>
  <name>dfs.datanode.kerberos.principal</name>
  <value>dn/_HOST@EXAMPLE.COM</value>
</property>
<!-- ACL -->
<property>
  <name>dfs.permissions.enabled</name>
  <value>true</value>
</property>
<property>
  <name>dfs.namenode.acls.enabled</name>
  <value>true</value>
</property>
</configuration>
```
container-executor.cfg
```bash
hdfs@hadoop1:/opt/hadoop-2.7.1/etc/hadoop$ ls container-executor.cfg
-r-------- 1 root hadoop 217  7月 20 16:10 container-executor.cfg
```
```cfg
yarn.nodemanager.linux-container-executor.group=hadoop
banned.users=hdfs,yarn,mapred,bin
min.user.id=1000#Prevent other super-users
allowed.system.users=##comma separated list of system users who CAN run applications
```
note:**container-executor.cfg必须配置为如上权限,**
**并且其所在所有父文件夹需要设置为组和其ta不可写**

mapred-site.xml:
```xml
<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<configuration>
<property>
  <name>mapreduce.jobhistory.keytab</name>
  <value>/opt/hadoop-2.7.1/etc/keytabs/jhs.keytab</value>
</property>

<property>
  <name>mapreduce.jobhistory.principal</name>
  <value>jhs/_HOST@EXAMPLE.COM</value>
</property>
</configuration>
```

完工,启动Hadoop集群即可,有错误看log files和Google.
HBase, Hive等配置也就水到渠成了.

时间仓促,水平有限,见谅.

感谢王和我自己

参考:

1. [https://help.ubuntu.com/community/Kerberos][1]
2. [http://tech.meituan.com/hadoop-security-practice.html][2]
3. [http://blog.csdn.net/lalaguozhe/article/details/11570009][3]

[1]: https://help.ubuntu.com/community/Kerberos
[2]: http://tech.meituan.com/hadoop-security-practice.html
[3]: http://blog.csdn.net/lalaguozhe/article/details/11570009

