# 下面是python中使用的一些数学函数
import math
x=13.14
# 向上取整
math.ceil(x)
print(math.ceil(x))
# 向下取整
math.floor(x)
print(math.floor(x))
# 计算平方根
math.sqrt(x)
print(math.sqrt(x))
# 计算绝对值
num=-100
print(math.fabs(num))
# 计算自然对数
print(math.log(x))
# 计算以10为底的对数
print(math.log10(x))
# 计算浮点数的整数和小数部分
print(math.modf(x))
# 计算幂
print(math.pow(2,3))
# 返回e的x次幂
print(math.exp(x))
# 计算最大值--不需要数学库
max_val=max(1,2,3,4,5)
print(max_val)
# 计算最小值--不需要数学库
min_val=min(1,2,3,4,5)
print(min_val)
# 计算绝对值--不需要数学库
abs_val=abs(-10)
print(abs_val)
# 四舍五入--后面的数字是小数点后保留的位数
rounded_val=round(3.14159,2)
print(rounded_val)