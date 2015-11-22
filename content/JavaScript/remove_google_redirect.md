Title: 从remove google redirect 失效说起
Date: 2014-05-11 0:37
Author: junfeng
Category: JavaScript
Tags: extensions, js event

前段时间发现remove google redirect突然不能用了，在chrome web store的页面也没了。难道被google和谐了？对于我这个重度google使用者来说可不是一件好事情，搜索的结果都要先被google重定向，增加了不必要的加载时间。

只想寻找解决办法：[点击这里][1]

于是想着能不能改改那个插件的代码，修复这个bug，找到那个插件的源代码，发现一下子1200多行代码，这么复杂。感觉移除一个重定向链接不需要这么麻烦吧，决定自己实现一个。

用的时候发现google在你点击一个链接时，会被替换成google的重定向链接。

    http://en.wikipedia.org/wiki/Continuous_integration
会被替换成

    https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&sqi=2&ved=0CDUQFjAA&url=%68%74%74%70%3a%2f%2f%65%6e%2e%77%69%6b%69%70%65%64%69%61%2e%6f%72%67%2f%77%69%6b%69%2f%43%6f%6e%74%69%6e%75%6f%75%73%5f%69%6e%74%65%67%72%61%74%69%6f%6e&ei=W0NuU-OSBImQrQe0lYBw&usg=AFQjCNHxUWTtSC_MArGdeBXVTWRAUUkL5Q&sig2=dTBasnGxLNpeCYshC_LnbA

查询的url的值是原网址经过url encode转换的。本来想着用这
个值得到原网址的。但google还算厚道，把原网址存到了属性data-url中了。原网址是得到了，关键是怎么恢复原网址。

通过反复测试发现，刚开始搜索出来的链接是没有被处理的，但当你点击链接的时候却变成了google重定向的链接。因为google的某段js代码监听了mousedown事件，当你点击链接的时候，在鼠标按下时，google把链接修改了。这就好办了，我们可以监听mouseup事件，把网址再改回来，这样当点击后，浏览器看到的就是原网址了。(你要知道点击一次鼠标会先后触发mousedown, mouseup, click事件) 。如此就去掉了搜索结果的重定向。

于是做了个小插件，只有24行代码

下载地址：[here][1]
项目地址：[here][2]

  [1]: https://github.com/juffy/RecoverUrl/raw/master/recover%20url.0.0.1.crx
  [2]: https://github.com/juffy/RecoverUrl
> Written with [StackEdit](https://stackedit.io/).
