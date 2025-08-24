# 随机数函数
import random
# 随机选择---在0到9之间
print("随机选择---在0到9之间:", random.choice(range(10)))
# 生成随机数种子
# 这个是没有返回值
print("生成随机数种子:", random.seed(42))
# 随机生成一个实数--在1~10之间
print("随机生成一个实数--在1~10之间:", random.uniform(1,10))
# 洗牌
list = [1,2,3,4,5]
random.shuffle(list)
print("洗牌后的结果:", list)
# 随机生成生成下一个实数--在0~1之间
print("随机生成一个实数--在0~1之间:", random.random())
# 从指定范围内，按照基数递增的集合中获取一个随机数
# start:起始数 0
# stop:结束数 100
# step:步长 2
print("从指定范围内，按照基数递增的集合中获取一个随机数:", random.randrange(0, 101, 2))
