Title: backslash in C++
Date: 2015-06-21 18:24:19
Author: junfeng
Category: 程序猿
Tags: backslash, C++

Use backslash to format long long lines. Oops, I nerver use it in C++.

How to use backslash?

This is an example:
```cpp
#include <iostream>
#include <string>
int main() {
    int a = 1, \
            b = 2;
    int c = 3,
        d = 4;
    std::string s = "fffff" \
                     "fffff\\n"; // right
    std::string s2 = "fffff"
        "fffff\\n"; // right
    std::string s3 = "\u4f60\u597d";
    /* std::string s3 = "\u4f60\u" \
                      "597d"; wrong
    std::string s3 = "\u4f60\u"
        "597d"; wrong
    */
    std::string s4 = "你好";
    std::cout << a << " " << b << std::endl;
    std::cout << c << " " << d << std::endl;
    std::cout << s << std::endl;
    std::cout << s2 << std::endl;
    std::cout << s3 << std::endl;
    std::cout << s4 << std::endl;
}
```

Maybe from now I need write one variable in one line, and document every variable.

Hope I can get *clean code*
