Title: Fire Net
Date: 2013-05-20 20:24
Author: algu
Category: 程序猿
Tags: ZOJ1002
Slug: fire-net

ZOJ Problem Set - 1002

<style type="text/css"><!--<br />
pre { font-family: monospace; color: #000000; background-color: #ffffff; } body { font-family: monospace; color: #000000; background-color: #ffffff; } .PreProc { color: #a020f0; } .Special { color: #6a5acd; } .Constant { color: #ff00ff; } .Identifier { color: #008080; } .Statement { color: #804040; font-weight: bold; } --><br></br>
--></style>
    def Input(L,n):
            if type(L)==list:
                    for i in range(0,n):
                            L.append([t for t in sys.stdin.readline().rstrip('\n')])
    def place_bh(L,row,col,n):
            if L[row][col]=='X':
                    return False
            j=n-1
            while(j>=0):
                    if j==col:
                            j-=1
                            continue
                    if L[row][j]=='X':
                            break
                    if L[row][j]=='O':
                            return False
                    j-=1

            k=n-1
            while(k>=0):
                    if k==row:
                            k-=1
                            continue
                    if L[k][col]=='X':
                            break
                    if L[k][col]=='O':
                            return False
                    k-=1

            return True

    def FindMax(L,k,n):
            curnum=0
            j=k
            while j<k+n*n:
                    if j>=n*n:
                            z=j-n*n
                    else:
                            z=j

                    row=z/n
                    col=z%n
                    if place_bh(L,row,col,n):
                            L[row][col]='O'
                            curnum+=1

                    j+=1

            return curnum

    def main():
            while True:
                    n=int(sys.stdin.readline().rstrip('\n'))
                    if n==0:
                            break

                    L=[]
                    maxn=0
                    Input(L,n)
                    for k in range(0,n*n):
                            t=copy.deepcopy(L)
                            curn=FindMax(t,k,n)
                            if maxn<curn:
                                    maxn=curn

                    print maxn

    if __name__=='__main__':
            import copy
            import sys
            main()

突然发现我没有用回溯法哎。

Python做算法可以偷懒。呵呵

参考：[链接](http://www.cnblogs.com/phinecos/archive/2008/09/18/1293017.html)
