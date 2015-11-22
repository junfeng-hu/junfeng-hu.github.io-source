Title: JavaScript closure
Date: 2013-10-23 16:35
Author: algu
Category: 程序猿
Tags: closure, JavaScript
Slug: closure-of-programming-languages

>  a closure (also lexical closure or function closure) is a function or
> reference to a function together with a referencing environment—a
> table storing a reference to each of the non-local variables (also
> called free variables or upvalues) of that function.
>
> <http://en.wikipedia.org/wiki/Closure_(computer_science)>

Notes:

1.  The initial values of the non-local variables depends on not where
    the closure define,but where the closure call.
2.  Referencing environment ,not copy.Meaning when you call a variable
    references to a closure twice,the environment maybe change.
3.  Every time you hold a returened closure using a varible
    will initialize it's referencing enviroment.

 

Example:

<div>

var name="Window";

</div>

<div>

var Top={

</div>

<div>

    name:"top",

</div>

<div>

    Inner:{

</div>

<div>

        name:"inner",

</div>

<div>

        getName:function(){

</div>

<div>

            var that=this;

</div>

<div>

            var i=0;//note1

</div>

<div>

            function increase(){

</div>

<div>

                var rt="this binding:"+this.name+"\\n\\n"+"number
i:"+i;//this binding

</div>

<div>

                i++;

</div>

<div>

                return rt;

</div>

<div>

            };

</div>

<div>

            i++;//note1

</div>

<div>

            return increase;

</div>

<div>

        }

</div>

<div>

    }

</div>

<div>

};

</div>

<div>

var closure1=Top.Inner.getName();

</div>

<div>

alert("first call closure1"+"\\n"+closure1());//note1

</div>

<div>

var closure2=Top.Inner.getName();

</div>

<div>

alert("first call closure2"+"\\n"+closure2()); //note1,note3

</div>

<div>

alert("againe call closure1"+"\\n"+closure1());//note2

</div>

<div>

alert("againe call closure2"+"\\n"+closure2());//note2

</div>

<div>

var closure21=closure2;

</div>

<div>

alert("first call closure21"+"\\n"+closure3());//assign another varible
has referencing enviroment

</div>

<div>

</div>

<div>

</div>

<div>

References
----------

<http://www.ruanyifeng.com/blog/2009/08/learning_javascript_closures.html>

<http://coolshell.cn/articles/6731.html>

<http://en.wikipedia.org/wiki/Closure_(computer_science)>

</div>
