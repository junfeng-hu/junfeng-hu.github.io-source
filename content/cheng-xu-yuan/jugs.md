Title: Jugs
Date: 2013-05-30 00:05
Author: algu
Category: 程序猿
Tags: 互质数
Slug: jugs

<style type="text/css"><!--<br />
pre { font-family: monospace; color: #000000; background-color: #ffffff; } body { font-family: monospace; color: #000000; background-color: #ffffff; } .Type { color: #2e8b57; font-weight: bold; } .Statement { color: #804040; font-weight: bold; } .Constant { color: #ff00ff; } .PreProc { color: #a020f0; } --><br></br>
--></style>
ZOJ Problem Set - 1005 Jugs  

题目：[来源](http://acm.zju.edu.cn/onlinejudge/showProblem.do?problemCode=1005)

    #include <iostream>
    using namespace std;
    int Ca,Cb,N;
    void work()
    {
        int a=0,b=0;
        if(Cb==N)
            cout << "fill B" << endl;
        else
        {
            if(Ca==N)
            {
                cout << "fill A" << endl;
                cout << "pour A B" << endl;
            }
            else
            {
                while(b!=N)
                {
                    if(a==0)
                    {
                        cout << "fill A" << endl;
                        a=Ca;
                    }
                    else if(b==Cb)
                    {
                        b=a;
                        cout << "empty B" << endl;
                        a=0;
                        cout << "pour A B" << endl;
                    }
                    else if(a+b>Cb)
                    {
                        a-=Cb-b;
                        b=Cb;
                        cout << "pour A B" << endl;
                    }
                    else
                    {
                        b+=a;
                        a=0;
                        cout << "pour A B" << endl;
                    }
                }
            }
        }
        cout << "success" << endl;
    }
    int main()
    {
        while(cin >> Ca >> Cb >> N)
        {
            work();
        }
        return 0;
    }

回溯，深度优先搜索，直接死循环了。  

然后搜到了互质数的一个性质。貌似广度优先搜索也可以，没试，层次比较深的话，估计会超出内存限制。  

参考：[链接](http://www.cnblogs.com/phinecos/archive/2008/09/21/1295472.html)
