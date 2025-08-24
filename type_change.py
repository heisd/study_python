# 数据类型转换
# 1.隐式转换
# 自动进行的类型转换
a = 10
b = 3.14
c = a + b
print(c)
# c自动转换成了float类型
# 这是因为在表达式中，int类型会被自动提升为float类型
# 2.显式转换
# 需要手动进行的类型转换
d = int(b)
print(d)
# d被转换成了整数类型
# int(x)  将x转换为整数
# float(x)  将x转换为浮点数
# complex(real,[imag])  创建复数
# str(x)  将x转换为字符串
# repr(x)  将x转换为字符串（可以用eval()还原）
# eval(str)  计算字符串中的表达式并返回结果
# list(x)  将x转换为列表
# tuple(x)  将x转换为元组
# dict(x)  将x转换为字典
# frozenset(x)  将x转换为不可变集合
# chr(x)  将整数x转换为对应的字符
# ord(x)  将字符x转换为对应的整数
# hex(x)  将整数x转换为十六进制字符串
# ord(x)  将整数x转换为八进制字符串
