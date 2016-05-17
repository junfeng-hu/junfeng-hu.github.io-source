Title: Install PostgreSQL on Arch Linux
Date: 2016-05-17 19:13:53
Author: junfeng
Category: memo
Tags: postgresql

[TOC]


### Introduction

For myself to remember.

### Content
First do
```
$ sudo -i -u postgres
```
or
```bash
$ su
$ su - postgres
```

Then initializes database cluster:
```
[postgres]$ initdb --locale $LANG -E UTF8 -D '/var/lib/postgres/data'
```
Where:

* the --locale is the one defined in the file /etc/locale.conf;
* the -E is the default encoding of the database that will be created in the future;
* and -D is the default location where the database cluster must be stored.

Changes `listen_address` setting at `/var/lib/postgres/data/postgresql.conf`, if you want to
postgres server listens on different addresses, default is localhost, need restarts

Maybe you also want to add a line to `/var/lib/postgres/data/pg_hba.conf`:
```
host       all all  network_address/23  md5
```

Creates new user using:
```
[postgres]$ createuser --interactive
```
For convenience, create a user named your login name.

Then create a database:
```
$ createdb myDatabaseName
```

### Reference
1. https://wiki.archlinux.org/index.php/PostgreSQL
