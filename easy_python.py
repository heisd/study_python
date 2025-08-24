# 我们使用python --version
# 本代码库是基于python3.10版本写的
# 因为本人以前是学习c/c++的所以可能会和这些东西有所关联
# 在这个文档中你不仅仅能学到python还可以了解一点c/c++
# 检测自己的python版本
# 在python3中允许unicode字符作为标识符
# 可以使用汉字作为变量名
# 在c/c++中不允许使用汉字作为变量名
import keyword
姓名 ="李泉延"
print(姓名)
# 我们可以使用下面的代码来检测一个变量名是否合法
# 在c语言使用isalpha来检测一个变量名是否合法
# 在c++中使用std::is_identifier来检测一个变量名是否合法
def is_valid_identifier(姓名):
   try:
      exec(f"{姓名} = 1")
      return True
   except :
      return False
print(is_valid_identifier(姓名))


# identifier_model
# 我们可以使用keyword库来检测关键字
# 在c语言中使用iskeyword来检测关键字
# 在c++中使用std::is_keyword来检测关键字
# 这些关键字我们不需要一次全部掌握
print(keyword.kwlist)  # 列出所有的关键字
# 我们可以使用关键字库来检测一个字符串是否是关键字
def is_keyword(词):
   return 词 in keyword.kwlist
print(is_keyword("if"))
print(is_keyword("姓名"))
# 我们可以使用help函数来查看一个函数的帮助文档
help(is_keyword)
# 我们可以使用help函数来查看一个模块的帮助文档
help(keyword)
# 在模块帮助文档中使用q进行退出
# python中的特点之一就是行和缩进
# 在python中，缩进是语法的一部分
# 我们可以使用tab键或空格键来缩进代码
# 通常建议使用4个空格来表示一个缩进级别
# 这样可以提高代码的可读性
# 而在c/c++中，通常使用大括号来表示代码块
choice = input("请输入你的选择（1-是，2-否）：")
if choice == "1":
    print("Hello, World!")
else:
    print("Goodbye, World!")
# 如果缩进不一致会导致语法错误
# python通常是一行写完一条语句,如果需要换行可以使用反斜杠\
item_one = 1
item_two = 2
item_three = 3
total = item_one + \
        item_two + \
        item_three
print(total)


# number_type_model
# python 使用 """""""来表示多行字符串--在我们平时使用时就当成多行注释来处理
# python 有一种特殊的数据类型 --复数
# 在c/c++中必须引入头文件complex.h/complex
# 在c中使用I表示虚数单位->double complex_number = 1 + 2I;
# 在c语言使用这个复数的情况下，可能需要链接数学库--本人使用的是gcc编译器
# 在c语言中使用gcc编译器编译时需要加上-lm选项
# 下面是一个简单的示例
"""
#include <complex.h>
#include <stdio.h>
int main() {
    double complex z1 = 1.0 + 2.0 * I;
    double complex z2 = 3.0 + 4.0 * I;
    double complex z3 = z1 + z2;
    printf("z1 = %.2f + %.2fi\n", creal(z1), cimag(z1));
    printf("z2 = %.2f + %.2fi\n", creal(z2), cimag(z2));
    printf("z3 = %.2f + %.2fi\n", creal(z3), cimag(z3));
    return 0;
}
"""
# gcc -o complex_program complex_program.c -lm
# 在c中使用creal和cimag来获取复数的实部和虚部
# 在c++中使用->std::complex<double> complex_number(1, 2);
# 下面是一个简单的示例
"""
#include <complex>
#include <iostream>
using namespace std;
int main(){
    complex<float> c1(2.0, 3.0);  // 2 + 3i
    complex<float> c2(1.0, 4.0);  // 1 + 4i
    complex<float> c3 = c1 + c2;  // Addition
    cout << "c1: " << c1 << endl;
    cout << "c2: " << c2 << endl;
    cout << "c3: " << c3 << endl;
    return 0;
}
"""
# 在python中直接使用j或J表示虚数单位
# 可以发现python的代码量是最少的
complex_number_1 = 1 + 2j  # 1 + 2i
complex_number_2 = 3 + 4j  # 3 + 4i
print(complex_number_1+complex_number_2)
# 而python中其他的数据类型也很简单--在c/c++中都有所提及
# bool/int/float/


# string_model
# 1.而且在python中的双引号和单引号完全相同
string_1 = "Hello, World!"
string_2 = 'Hello, World!'
print(string_1)
print(string_2)
# 这两种表示方式是完全等价的
# 但是在c/c++中，字符串只能用双引号表示
# 在c/c++中，单引号表示字符 

# 2.在python中，转义字符同样使用\表示
print("He said, \nHello, World!")
# 在c/c++中，转义字符也可以使用\表示
# 我们使用r可以取消转义--发现\n正常打印

# 3.r指的是raw string
print(r"He said, \nHello, World!")
# 在c/c++中没有类似的功能

# 4.字符串可以使用+链接
# 在c++中也可以使用+链接字符串
# 下面是一个简单的示例
"""
#include <iostream>
#include <string>
using namespace std;
int main() {
    string str1 = "Hello, ";
    string str2 = "World!";
    string str3 = str1 + str2;
    cout << str3 << endl;
    return 0;
}
"""
# 但是在c中不可以使用+链接字符串
# 我们可以使用strcat来链接字符串--字符串追加
"""
#include <stdio.h>
#include <string.h>
int main() {
    char str1[20] = "Hello, ";
    char str2[] = "World!";
    strcat(str1, str2);
    printf("%s\n", str1);
    return 0;
}
"""
string_3 = "Hello, " + "World!"
print(string_3)
# 5.python中可以使用*来重复字符串
# 在c/c++中没有类似的功能
string_4 = "Hello, " * 3
print(string_4)

# 6.Python 中的字符串有两种索引方式，从左往右以 0 开始，从右往左以 -1 开始
string_5 = "Hello, World!"
print(string_5[0])   # 输出 H
print(string_5[-1])  # 输出 !
# 7.在python中，切片可以使用:表示
# 表示从左到右的索引范围
print(string_5[0:-1])  # 输出 Hello, World
# 在c/c++中也有类似的功能
# 但是在c/c++中，负索引是无效的
# 在c语言中
# 下面是一个简单的示例
"""
#include <stdio.h>
#include <string.h>
int main() {
    char str[] = "Hello, World!";
    printf("%c\n", str[0]);   // 输出 H
    printf("%c\n", str[strlen(str) - 1]);  // 输出 !
    return 0;
}
"""
# 在c++中
# 下面是一个简单的示例
"""
#include <iostream>
#include <string>
using namespace std;
int main() {
    string str = "Hello, World!";
    cout << str[0] << endl;   // 输出 H
    cout << str[str.length() - 1] << endl;  // 输出 !
    return 0;
}
"""

# 8.python中的字符串是不可变的
# 这意味着一旦创建，就无法修改字符串的内容
# 如果需要修改字符串，可以创建一个新的字符串
# 例如：
string_6 = "Hello, World!"
string_6 = string_6.replace("World", "Python")
print(string_6)
# 但是在c/c++中，字符串是可变的--除了char*类型的不可变
# 例如：
# 在c语言中
""""
char str[] = "Hello, World!";
str[7] = 'P';
str[8] = 'y';
str[9] = 't';
str[10] = 'h';
str[11] = 'o';
str[12] = 'n';
printf("%s\n", str);
"""
# 在c++中
"""
#include <iostream>
#include <string>
using namespace std;
int main() {
    string str = "Hello, World!";
    str[7] = 'P';
    str[8] = 'y';
    str[9] = 't';
    str[10] = 'h';
    str[11] = 'o';
    str[12] = 'n';
    cout << str << endl;
    return 0;
}
"""
# 9.在python中，字符串可以使用in来判断一个字符串是否包含另一个字符串
# 在c/c++中没有类似的功能
string_7 = "Hello, World!"
if "World" in string_7:
   print("Found!")
else:
   print("Not Found!")

# 10.python没有char类型
# 在python中，字符可以被视为长度为1的字符串
char_1 = 'A'
char_2 = 'B'
print(char_1)
print(char_2)
# 在c/c++中，char类型是一个基本数据类型
# 在c/c++中，char类型占用1个字节
# 在c/c++中，char类型可以表示一个字符
# 在c/c++中，char类型可以使用单引号表示
""""
#include <stdio.h>
char char_1 = 'A';
char char_2 = 'B';
printf("%c\n", char_1);
printf("%c\n", char_2);
"""

# 11.可以加上步长的概念
string_8 = "Hello, World!"
print(string_8[0:5:1])  # 输出 Hello
print(string_8[0:5:2])  # 输出 Hlo
# 每间隔一个字符取一个
print(string_8[1:3:2])     # 输出 el
print(string_8[7:12:2])    # 输出 ol!
# 在c/c++中可以通过for循环实现相同的功能
""""
for (int i = 0; i < strlen(string_8); i += 2) {
    printf("%c", string_8[i]);
}
printf("\n");
"""


# 空行的处理
# 在c/c++中可以通过if判断空行
"""
if (string_8[0] == '\n') {
    printf("Empty line\n");
}
"""
# 下面这段代码在python中是等价的
if string_8[0] == '\n':
    print("Empty line")
    # 等待用户输入
    input("\n\nPress Enter to continue...")
    print("继续执行...")


# 在python一行中输入多条语句
# 例如：
# 中间是用分号隔开
# sys是Python的标准库
# sys.stdout.write用于输出在控制台
import sys; x = 'runoob'; sys.stdout.write(x + '\n')
# 在c/c++中
"""
#include <iostream>
using namespace std;
int main() {
    string x = "runoob";
    cout << x << endl;
    return 0;
}
"""

# 多个语句构成代码组
# 缩进相同的语句属于同一个代码块
# 类似于C/C++中的大括号
if True:
    print("Hello, World!")
    print("This is a code block.")
    print("This is also part of the code block.")
else:
    print("This is outside the code block.")
    print("This is also outside the code block.")
# 在c/c++中
"""
#include <iostream>
using namespace std;
int main() {
    if (true) {
        cout << "Hello, World!" << endl;
        cout << "This is a code block." << endl;
        cout << "This is also part of the code block." << endl;
    } else {
        cout << "This is outside the code block." << endl;
        cout << "This is also outside the code block." << endl;
    }
    return 0;
}
"""

# 在python默认的print是换行的
print("Hello, World!")
print("This is a code block.")
print("This is also part of the code block.")
# 在python中可以使用end参数来控制输出的结尾
print("Hello, World!", end=", ")
print("This is a code block.", end=", ")
print("This is also part of the code block.")
# 在c/c++中默认的cout是换行的
# 但是printf是不换行的
"""
#include <iostream>
using namespace std;
int main() {
    cout << "Hello, World!" << endl;
    cout << "This is a code block." << endl;
    cout << "This is also part of the code block." << endl;
    printf("Hello, World!");
    printf("This is a code block!");
    printf("This is also part of the code block!");
    return 0;
}
"""

# import 和 from...import
# 在python中可以使用import来引入模块
# 导入数学模块
import math
# 在c/c++中可以使用#include来引入头文件
"""
#include <iostream>
#include <cmath>
using namespace std;
"""

# 关于python的命令行参数
# 使用python -h
# 可以查看帮助信息