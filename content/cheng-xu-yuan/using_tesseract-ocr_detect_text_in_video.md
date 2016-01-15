Title: 使用tesseract-ocr和opencv识别视频中文字
Date: 2016-01-15 16:10
Author: junfeng
Category: 程序猿
Tags: C++, tesseract-ocr, opencv

[TOC]

### Abstract
本文使用tesseract-ocr和opencv提取B站2015年舞蹈总排行榜视频中的Id号，
然后使用you-get工具下载提取到的视频。视频包下载地址见[Result](#result)。

### Introduction
在B站看到有人出了2015年舞蹈区总排行榜TOP100视频([链接][1])，看完视频感觉都还不错，
有些还没看过，想着既然能在这个排行榜上，那就应该不错，值得下载下来收藏。

那怎么把里面的视频下载下来呢？

我的思路是这样的：
1. 排行榜视频中提到的所有舞蹈区视频都贴上了Id号，就是av后面跟的六位数字。
2. 获取到Id号，通过you-get([官网][2])工具将相应视频下载下来。

那怎么获取视频的Id呢？

简单的做法是对着排行榜视频，一个一个的手动记录下来。
这种方法精确率应该能达到100%，但是伤害眼睛。

*程序猿可是要好好保护眼睛的。*

也学了4, 5年coding了，想着通过程序能不能提取出排行榜视频里的所有Id号。

### Implementation
有了想法，当然也要有方法。

想到之前在cloudera blog上看到的一篇文章([链接][3])中提到使用ocr工具
提取PDF文件中的文字，那么自然考虑能不能使用ocr工具提取视频中的文字呢。

文章中提到他们使用Ghostscript先把PDF文件分割成图片，
再交给tesseract-ocr([GitHub][4])处理，获取到文字。
那样的话，我只需要把视频分割成一帧一帧的图片，
tesseract-ocr也应该能处理。

Google搜索出通过使用ffmpeg就可以将视频分割成图片了，如下命令
```bash
ffmpeg -i 【年刊】2015年哔哩哔哩舞蹈区总排行榜TOP100.flv image_%d.png
```
但是该方法将产生5万多张图片，而且每张图片平均有2、3MB，
显然该方法并不现实，首先转换速度慢，非常占用CPU，同时视频转换到一半，
磁盘已经写了60多GB的图片了。担心实验室的配置不怎么样的机子被自己给写坏了，
就没继续转换下去。

听说OpenCV([官网][5])比较擅长处理图片和视频，于是想到能不能通过OpenCV将
视频一帧一帧的交给tesseract-ocr处理，获取每个帧图片中的Id号，最后再做个
去重。

Google一下，在stackoverflow搜到了类似的问题([链接][6])，该问题是询问用OpenCV
和tesseract-ocr从摄像头的视频中提取文字的，类比到已经存在的视频，那么OpenCV加上
tesseract-ocr应该也是可以处理的。

#### 环境准备
OS: Arch Linux

安装OpenCV和tesseract-ocr：
```bash
sudo pacman -S tesseract
# tesseract-data
sudo pacman -S tesseract-data-eng
sudo pacman -S tesseract-data-chi_sim
sudo pacman -S opencv
```
g++编译flag脚本：
```bash
#!/bin/bash
# lept是tesseract-ocr的依赖leptonica
g++ -std=c++11  `pkg-config --libs tesseract opencv lept` $1 -o ${1}.out
```

#### Coding
代码基于stackoverflow上贴出的[代码][6]，结合OpenCV官方给出的使用VideoCapture的
[示例代码][7]，加上stackoverflow上另外一个[问题][8]的回答贴出的代码，
对视频帧进行预处理，如下：
```c++
cv::Mat new_img = cv::imread(argv[1]);
cv::bitwise_not(new_img, new_img);

double thres = 100;
double color = 255;
cv::threshold(new_img, new_img, thres, color, CV_THRESH_BINARY);

cv::imwrite("inv_thres.png", new_img);
```
由于tesseract-ocr对白纸黑字的图片处理效果才比较好，所以需要对视频帧预处理，
可以说图片预处理的好坏直接影响识别文字的精确程序，而我并不懂图形学，仅仅是
看着处理效果调的。

代码还使用了stackoverflow中另外一个[问题][9]中的回答的代码，适配OpenCV数据结构`Mat`到tesseract-ocr
中的API函数SetImage的代码：
```c++
tesseract::TessBaseAPI tess;
cv::Mat sub = image(cv::Rect(50, 200, 300, 100));
tess.SetImage((uchar*)sub.data, sub.size().width, sub.size().height, sub.channels(), sub.step1());
tess.Recognize(0);
const char* out = tess.GetUTF8Text();
```

最终获取排行榜视频中ID号的代码见[Gist][10]。

至于包含Id号和Score的矩形区域是使用GIMP([官网][11])找出来的。
缩小检测区域，有利于防止tesseract-ocr返回很多垃圾文字。

开始使用chi_sim language data，发现效果并不是很好，总是把1识别成l，
由于Id号和Score都是由数字和字母组成，因此换成eng language data精确度
反而能提高一些。

获取到Id号后，构造url和去重就很简单了。

最后使用you-get下载视频：
```bash
# using uniq removes duplicates
for u in `uniq ../dance_url.out `; do echo $u; you-get $u; done
```

### Result
最后下载到的视频见[分享][12]，密码: 5gv3

Id号并没有全部识别出来。

### Related works
主要的相关工作就是cloudera blog上发表的那篇[文章][3]。他们在那篇文章中
使用tesseract-ocr识别扫描PDF文件，并将结果存在HBase中。受那篇文章启发，
才有了本篇文章的想法。

### Limitation
OpenCV和tesseract-ocr识别视频中文字，预处理很重要，而且对字体变化很敏感。
一般识别正确率达不到100%，本文例子中，由于排行榜视频前期和后期Id号字体发生
改变，导致视频中后半部分的Id号基本上识别不出来。100个Id号，仅仅正确识别40个
左右，精确率为40%。

想法可行，但要提高精确率的话，需要花很大功夫。

### Future works
使用该方法，对于字体没有什么变化的排行视频，识别率能达到90%，以鬼畜区某个
排行榜视频为例，40多个视频能精确识别出30多个，识别性能还是不错的。

同样该方法可以应用到B站类似排行视频，例如舞蹈区每周排行视频，只要字体不发生
改变，预处理做好，基本上还是能识别出大部分Id号的。

### Conclusion
OpenCV和tesseract-ocr结合，对于视频文件、实时视频流中的文本识别问题，
是一个不错的可行方案。

### References
```markdown
[1]: http://www.bilibili.com/video/av3484492/
[2]: https://you-get.org/
[3]: http://blog.cloudera.com/blog/2015/10/how-to-index-scanned-pdfs-at-scale-using-fewer-than-50-lines-of-code/
[4]: https://github.com/tesseract-ocr/tesseract
[5]: http://opencv.org/
[6]: http://stackoverflow.com/questions/14041025/how-can-i-use-tesseract-and-opencv-to-extract-the-text-from-the-camera
[7]: http://docs.opencv.org/3.0-last-rst/modules/videoio/doc/reading_and_writing_video.html#videocapture
[8]: http://stackoverflow.com/questions/11464397/image-preprocessing-for-text-recognition
[9]: http://stackoverflow.com/questions/8115368/converting-cvmat-for-tesseract
[10]: https://gist.github.com/junfenglx/ed966fb7ea41ed2a13a9
[11]: https://www.gimp.org/
```


[1]: http://www.bilibili.com/video/av3484492/
[2]: https://you-get.org/
[3]: http://blog.cloudera.com/blog/2015/10/how-to-index-scanned-pdfs-at-scale-using-fewer-than-50-lines-of-code/
[4]: https://github.com/tesseract-ocr/tesseract
[5]: http://opencv.org/
[6]: http://stackoverflow.com/questions/14041025/how-can-i-use-tesseract-and-opencv-to-extract-the-text-from-the-camera
[7]: http://docs.opencv.org/3.0-last-rst/modules/videoio/doc/reading_and_writing_video.html#videocapture
[8]: http://stackoverflow.com/questions/11464397/image-preprocessing-for-text-recognition
[9]: http://stackoverflow.com/questions/8115368/converting-cvmat-for-tesseract
[10]: https://gist.github.com/junfenglx/ed966fb7ea41ed2a13a9
[11]: https://www.gimp.org/
[12]: http://pan.baidu.com/s/1jHiXFeA
