# 带a的是反三角函数
import math
print("反正弦函数:", math.asin(0.5))
print("反余弦函数:", math.acos(0.5))
print("反正切函数:", math.atan(0.5))
# 不带a的是三角函数
print("正弦函数:", math.sin(math.radians(30)))
print("余弦函数:", math.cos(math.radians(60)))
print("正切函数:", math.tan(math.radians(45)))
# hypot()函数--返回两点之间的距离--从这个点到原点的距离
print("两点之间的距离:", math.hypot(3, 4))
# atan2（y, x）--返回点（x，y）与x轴之间的夹角
print("点(3, 4)与x轴之间的夹角:", math.degrees(math.atan2(4, 3)))
# degrees()函数--将弧度转换为角度
print("将弧度转换为角度:", math.degrees(math.pi))
# radians()函数--将角度转换为弧度
print("将角度转换为弧度:", math.radians(180))