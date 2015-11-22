Title: mount and grep
Date: 2014-06-08 21:45
Author: junfeng
Category: memo
Tags: mount, grep


mount options
-------------
`mount`display current partions mount options.
Output like this:

```
/dev/sda2 on /home type ext4 (rw,relatime,data=ordered)
/dev/sda5 on /media/sda5 type ext4 (rw,nosuid,nodev,noexec,relatime,data=ordered,user)
/dev/sda7 on /media/sda7 type ext4 (rw,nosuid,nodev,noexec,relatime,data=ordered,user)
/dev/sda6 on /media/sda6 type ext4 (rw,nosuid,nodev,noexec,relatime,data=ordered,user)
```

if you run a executable program on a partion with settiong noexec mount options, this program will not execute.

And you got error message like `bash: ./a.out: Permission denied`.

When you have a program that opens exec bit flag, but it can't run, even you have corret permission.

then `mount` check mount options of the partion the program run on. Maybe just because you didn't open exec mount option.

*Caution:*

if you set partions auto mount on /et/fstab, check whether you set user mount option.

according the mount man page says:

> Allow an ordinary user to mount the filesystem.
  The name of the mounting user is written to mtab so that he can unmount the filesystem again.
  This option implies the options noexec, nosuid, and nodev (unless overridden by subsequent options,
  as in the option line user,exec,dev,suid).

So if you want programs can run on these auto mount partions, add exec option if you setted user option.

grep options
-----------
If you want to search some words like `X-Forwarded-For` recursively, you type
`grep -i "X-Forwarded-For" -r *`. It works, but search every type files.

Maybe you want to recursively search just some type files like "*.py".

Type `grep -i "X-Forwarded-For" -r *.py` is a naturaly derivation. But It doesn't work.
It equals to `grep -i "X-Forwarded-For" *.py`, just search current directory "*.py" files.

The right solution is:
`grep -i "X-Forwarded-For" --include=*.py -r`

recursively search *.py files for `X-Forwarded-For`
