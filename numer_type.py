# python中的数据类型
# python中的数据类型不需要声明
# 而且可以动态改变
# 但是在c/c++中需要声明数据类型
"""
# 例如：
int a = 10;
float b = 3.14;
char c = 'A';
"""
# 在python中
a=10
b=3.14
c='A'
print(a)
print(b)
print(c)

# 在python中允许向多个变量赋值
x1=x2=x3=6
# 在c/c++中不允许这样做
# 在c/c++中需要这样写
"""
int x1, x2, x3=6;
"""
# 在python中还允许多个不同类型的变量赋值
# 在c/c++中不允许这样做
y1, y2, y3 = 6, 6, "abc"
# 在c/c++中需要这样写
"""
int y1 = 6;
int y2 = 6;
char* y3 = "abc";
"""
# 使用type来查看变量的类型
print(type(x1))
print(type(y1))
# 在c/c++中没有类似的功能--因为我们都需要提前声明变量的类型




# python中的数据类型主要有以下几种
# 不变的数据类型：number,string,tuple
# 可变的数据类型：list,dict,set

# 1. 数字类型
# 只有int, float, complex,bool四种类型
num = 10
pi = 3.14
flag = True
complex_number_1 = 2 + 3j
# 可以使用isinstance()来判断变量类型
print(isinstance(num, int))
print(isinstance(pi, float))
print(isinstance(flag, bool))
print(isinstance(complex_number_1, complex))
# 当你指定一个值时，Number对象就会被创建
var1 = 1
var2 = 10.0
# 可以使用del语句删除对象
del var1, var2
# 这是不是很像我们c/c++中的free()函数
# 难道python的变量都是建立在堆上的吗？
# 这里我问了一下deepseek
"""
Python的变量确实建在堆上,Python运行时通过引用计数和垃圾回收机制自动为我们释放内存,
其自动化程度和安全性远高于手动delete,其原理类似于C++的std::shared_ptr,但对程序员是完全透明的。
在绝大多数情况下,你都不需要手动使用del。
它通常只在需要主动打破循环引用或从大型数据结构（如列表、字典）中移除元素，或者清理某个命名空间（例如在函数中删除一个大型临时变量）时才会被用到。
"""
# 下面是python有趣的几种计算和c/c++不一样的
# 乘方运算
num1=2**3
# 整数除法
num2=5//2
print(num1)
print(num2)
# 这里是python中整数除法和浮点数除法的区别
# 在python中，/表示浮点数除法，//表示整数除法


# 2. 字符串类型
str = "Hello, World!"
print(str)
# 我们可以使用反斜杠来转义字符
# \也可以作为续行符
# 但是python中的字符是不可以改变的
# 在c/c++中字符串是可以改变的
# 同样体现了c/c++的灵活性
str2 = "Hello, \"World!\""
print(str2)
# str2[0]='h'
# 报错--'str' object does not support item assignment
# 使用r可以取消转义
# 在c/c++中没有类似的功能
str3 = r"Hello, \"World!\""
print(str3)



# 3. 列表类型
# 类似于c/c++中的数组
# 刚刚看见这个给我的反应是数据结构里面的链表
# 其实在python中，list是一个动态数组
# 类似于STL中的vector
# 索引值以0开始值，到-1结束
# 在c/c++中，数组的索引也是从0开始的
# 但是不允许使用负数索引
# 我们找末索引时可以使用vector.size();
# 这个返回值就是末索引
# 列表写在方括号之间，元素使用逗号分隔
list = [1, 2, 3]
print(list[1])
print(list[-1])
# 列表和字符串一样允许索引和切片操作
print(list[0:2])
print(list[-2:])
# 特殊的遍历整个列表
print(list[:])
# 这里是python中列表的添加元素
list.append(4)
print(list) #等价于C/C++中的push_back()
# 列表可以使用+号进行拼接
# 在STL中也可以使用+号进行拼接
# python列表中也允许不同的数据类型
# 在STL中可以使用std::any来实现
# 但是比python的这个也有一定缺陷
# 因为我们需要知道具体类型而且使用std::any_cast<具体类型>来进行类型转换
list2 = [5, 6, 7, 'd']
list3 = list + list2
print(list3)
# 列表中的元素是可变的
list[0] = 10
print(list)


# 4. 元组类型
# 元组是不可变的序列
# 和列表相似
# 我在想元组是不是const list
# 使用const关键字来声明，不是就是不可变的数组吗
# 在c/c++中我们如果不希望一个数组的值发生变化的话我们是使用const关键字来声明的
# 注意元组中是可以存放不同类型的数据的
# 在c/c++中数组只能存放同一种类型的数据
tuple = (1, 2, 3, "abc", 4.5)
print(tuple)
# python的数据类型大都是引用
# 这意味着当你将一个变量赋值给另一个变量时，它们实际上引用的是同一个对象
x=10
y=10
z=10
# 实际上在内存中只创建了一个对象
# 这意味着x、y和z实际上引用的是同一个对象
print(id(x))
print(id(y))
print(id(z))
# 减少了内存的使用
# 我们的元组也是支持切片的
# 这个切片我们可以类比成范围
print(tuple[1:4])
print(tuple[-3:])
# 也支持+号操作
# 这个操作我们可以类比成连接
print(tuple + (5, 6, 7))


# 5. 字典类型
# 我们可以想到C/C++中的map
# map<string, int>
# 但是python的字典比C/C++中的map更加灵活
# 因为支持不同类型的键和值
# 当然我们在c/c++中也可以使用不同类型的键和值
# 但是需要使用std::variant来实现
# 下面写个python字典的实现吧
# 发现实现十分困难，C++的类型系统太复杂了
"""
#include <variant>
#include <map>
#include <string>
#include <iostream>
#include <vector>

// 定义可以存储的类型
using Value = std::variant<int, double, std::string, bool, std::vector<Value>>;

// 模拟Python字典
using PyDict = std::map<std::string, Value>;

int main() {
    // 创建一个类似Python的字典
    PyDict person;
    
    // 添加各种类型的值 - 就像Python一样
    person["name"] = "Alice";
    person["age"] = 25;
    person["height"] = 1.75;
    person["is_student"] = false;

    // 甚至嵌套字典(通过vector of variant模拟)
    std::vector<Value> hobbies = {"reading", "swimming", "coding"};
    person["hobbies"] = hobbies;
    
    // 访问值（需要类型检查）
    std::cout << "Name: ";
    if (std::holds_alternative<std::string>(person["name"])) {
        std::cout << std::get<std::string>(person["name"]) << std::endl;
    }
    
    std::cout << "Age: ";
    if (std::holds_alternative<int>(person["age"])) {
        std::cout << std::get<int>(person["age"]) << std::endl;
    }
    
    return 0;
}
"""
# 但是使用起来就比较麻烦
# 不如直接使用Python的字典
dict = {"name": "Alice", "age": 30, "height": 1.75, "is_student": False}
# 访问字典中的值--通过字典中的键来访问
print(dict["name"])
print(dict["age"])
print(dict["height"])
print(dict["is_student"])
# 字典中的值是一对键值对
# 和pair一样
# 创建空字典使用
dict2 = {}
dict2["city"] = "New York"
dict2["country"] = "USA"

# 6. 集合类型
# 数据不会重复，支持集合运算
# 和我们在STL中的set类似
# 但是STL中的set是有序的，而Python中的set是无序的
# 在Python中set是可以包含不同类型的元素
# 但是c++中的set只能包含同一种类型的元素
# 但是Python中的set运算更加人性化
# 在c++中我们需要使用set_intersection, set_union, set_difference等函数来进行集合运算
# 而在Python中我们可以直接使用&、|、-等运算符
# 以前过的都是啥苦日子呀这些函数真的超级难记
set1 = {"apple", "banana", "cherry"}
set2 = {1, 2, 3}
print(set1 & set2)
print(set1 | set2)
print(set1 - set2)

set = {"apple", "banana", "cherry", 1, 2, 3}

# bytes类型
# 字节串是不可变的
# 和字符串一样
# 但是字节串是以字节为单位进行操作的
# 适合处理二进制数据
# 创建 bytes 对象的方式有多种，最常见的方式是使用 b 前缀
bytes_set = {b"apple", b"banana", b"cherry"}
print(bytes_set)


