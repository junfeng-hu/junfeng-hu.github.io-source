Title: the variable scope of list comprehensions
Date: 2013-10-14 23:34
Author: algu
Category: 程序猿
Tags: Python, variable scope
Slug: the-variable-scope-of-list-comprehensions

When using list comprehensions,the scope of temp variable doesn't
express as you expect.

For example

> Python 2.7.5 (default, May 15 2013, 22:43:36) [MSC v.1500 32 bit
> (Intel)] on win32  
>  Type "copyright", "credits" or "license()" for more information.  
>  \>\>\> L=[i for i in range(10)]  
>  \>\>\> print i  
>  9  
>  \>\>\>

and the output is 9,But maybe you shouldn't want this.

If you have variable i in the toper scope.

> \>\>\> i=2  
>  \>\>\> L=[i for i in range(10)]  
>  \>\>\> print i  
>  9  
>  \>\>\>

the  value of i was overwritten。

Happily,at Python 3 . the temp i in list comprehensions is local
variable.When the list comprehensions finished,the variables
were disappear.

> Python 3.3.2 (v3.3.2:d047928ae3f6, May 16 2013, 00:03:43) [MSC v.1600
> 32 bit (Intel)] on win32  
>  Type "copyright", "credits" or "license()" for more information.  
>  \>\>\> L=[i for i in range(10)]  
>  \>\>\> print (i)  
>  Traceback (most recent call last):  
>  File "\<pyshell\#1\>", line 1, in \<module\>  
>  print (i)  
>  NameError: name 'i' is not defined  
>  \>\>\> i=2  
>  \>\>\> L=[i for i in range(10)]  
>  \>\>\> print (i)  
>  2
>
>  
>
>  

 

 

 
