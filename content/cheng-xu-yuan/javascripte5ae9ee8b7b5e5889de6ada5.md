Title: JavaScript实践初步
Date: 2013-09-18 00:19
Author: algu
Category: 程序猿
Tags: JavaScript
Slug: javascripte5ae9ee8b7b5e5889de6ada5

\<\<JavaScript高级程序设计\>\>也看了大半本了,但却发现不会写JS程序,对界面设计什么的总是有一种畏惧的心理,最近这几天迷上了Chrome\_Extensions开发了,想做一个插件来着．顺便练习了下JS编程,补充一下苍白的实践经验．

虽然一个晚上,options.html页面都没做完,但还是学到了些知识．本来这些关于代码的没有必要写出来的，但今天晚上和JS作战,领悟了些许编程思想,觉得还是值得分享的.

关于模块化编程有了些许理解,它不在是教科书中的古板,毫无印象的概念.

1.  一个函数,一个类,一个文件都可以说是模块,晚上某一特定功能.
2.  模块与模块之间界限要清楚,一个模块不能做另一个模块的事情.不然的话,有的受的,逻辑混乱,思维不顺,无休止的调试.
3.  关于JavaScript编程,页面显示代码尽量只根据页面的结构来动态显示页面,数据保存代码做它自己的事．符合上一条规则.

 

一个tab空格健无意间在parent的childNodes插入了一个Text
Node.造成至少有半个小时的调试.

突然发现学DOM的一个好工具:

Chromium自带的开发者工具看某个element的属性比www.w3schools.com的JavaScript在线教程舒服多了.
