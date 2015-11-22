Title: html页面编码
Date: 2013-03-12 17:50
Author: algu
Category: 照片墙
Tags: encode, html
Slug: htmle9a1b5e99da2e7bc96e7a081

html貌似比较简单，但今天程序却栽在设置html字符集上了．遇到这样一个页面．head头中这样写的：  

[![](http://jcodef.com/wp-content/uploads/2013/03/2013-03-12-175823_433x21_scrot-300x14.png "2013-03-12-175823_433x21_scrot")](http://jcodef.com/wp-content/uploads/2013/03/2013-03-12-175823_433x21_scrot.png)  

本来是想把页面设置成utf-8编码的，但貌似这句meta没起作用，好像页面变成了gbk编码．我提交中文数据时，程序就因编码问题死掉了．等我注意到这上面的时候，整个程序的代码也快被我看完了．然后改成这样  

[![](http://jcodef.com/wp-content/uploads/2013/03/2013-03-12-180342_670x42_scrot-300x18.png "2013-03-12-180342_670x42_scrot")](http://jcodef.com/wp-content/uploads/2013/03/2013-03-12-180342_670x42_scrot.png)  
果然顺利通过．这时间浪费的真冤枉．  
谁能想到错误竟然是由html页面造成的，看来细微之处别有洞天啊！
