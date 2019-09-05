import random

n = eval(input("请输入你要抛硬币的次数:"))
result1 = []
result2 = []
for i in range(n):
    num = random.randint(1, 2)#1代表硬币正面,2代表硬币反面
    if num == 1:
        result1.append(num)
    else:
        result2.append(num)
print("出现正面的概率为:{}%,出现反面的概率为:{}%".format((len(result1)/n)*100,(len(result2)/n)*100))
