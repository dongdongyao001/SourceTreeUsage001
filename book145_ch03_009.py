# prg0400.py
'''
生成一定范围内的所有质数
'''
import sys
import keyword

range_number = int(input("请输入一个数字上限:"))
for item in range(2, range_number + 1):
    item_sqrt = item ** 0.5
    i = 2
    while i <= item_sqrt:
        if item % i == 0:
            break
        i = i + 1
    else:
        print(item, end=' ')
