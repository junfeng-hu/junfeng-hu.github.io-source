Title: C++ link and library usage
Date: 2015-06-28 20:20:58
Author: junfeng
Category: 程序猿
Tags: C++, CMake

When use a programming language produtively,
We need use third parties libraries.

If we install libraries and header files in
/usr/lib, /usr/local/lib and /usr/include/,
/usr/local/include, compilers will find them automatically.
But when libraries and headers are not in system paths, How
do you tell compilers to find them.

The answer is using compiler flags:

- `-I` adds headers search paths
- `-L` adds lib search paths
- `-l` adds lib files, includes dynamic and static libs
- `-Wl,-rpath,shared_path` adds shared_path to rpath

These flags control compilers how to find libraries you use.
Just like Java's class path.

*note: when use dynamic link, you should set rpath(RUNTIME SEARCH PATH)*
*proporly, otherwise when executes, your program would't find shared*
*libraries not located in system link path.*

But the above way is a low level approach. More convenient way
is using Makefile with pkg-config tool. pkg-config can read config
files and provides compiler flags about a library.

The most simple way is using CMake, CMake provides many commands to
find the library you are working with, and it is so convenient that
CMake provides lots of varaibles you can add paths for CMake to search.

Some useful commands include:

- `include_directories`, adds header files search path.
- `find_library`, find library files for linking.
- some varaibles about rpath:
    - `CMAKE_INSTALL_RPATH`
    - `CMAKE_INSTALL_RPATH_USE_LINK_PATH`
    - `CMAKE_BUILD_WITH_INSTALL_RPATH`


###References:
[http://www.rapidtables.com/code/linux/gcc.htm][1]

[http://manned.org/pkg-config.1][2]

[https://en.wikipedia.org/wiki/Rpath][3]

[http://www.cmake.org/documentation/][4]

[1]: http://www.rapidtables.com/code/linux/gcc.htm
[2]: http://manned.org/pkg-config.1
[3]: https://en.wikipedia.org/wiki/Rpath
[4]: http://www.cmake.org/documentation/

