# n, k = map(int, input().split())
# keys = [0] * n
# for i in range(n):
#     keys[i] = i + 1
#
# lis = [[0, 0, 0] for _ in range(k)]
#
# for i in range(k):
#     lis[i] = list(map(int, input().split()))
#     lis[i][2] = lis[i][1] + lis[i][2]
#
# lis_start = sorted(lis, key=lambda x: x[1])
# lis_end = sorted(lis, key=lambda x: (x[2], x[0]))
#
# c = 0
# for i in range(k):
#     while lis_end[c][2] <= lis_start[i][1]:
#         key_return = lis_end[c][0]
#         for j in range(n):
#             if keys[j] == 0:
#                 keys[j] = lis_end[c][0]
#                 break
#         c += 1
#
#     # 借钥匙
#     key_use = lis_start[i][0]
#     for j in range(n):
#         if keys[j] == key_use:
#             keys[j] = 0
#             break
#
# if lis_end[0][2] >= lis_start[k - 1][1]:
#     for i in range(k):
#         key_return = lis_end[i][0]
#         for j in range(n):
#             if keys[j] == 0:
#                 keys[j] = lis_end[i][0]
#                 break
#
# else:
#     for i in range(c, k):
#         key_return = lis_end[i][0]
#         for j in range(n):
#             if keys[j] == 0:
#                 keys[j] = lis_end[i][0]
#                 break
#
# print(*keys, sep=' ')


#
# def exChange(lis, b):
#     # 交换图形
#     # 最顶层图形
#     c = [lis]
#     for x in b:
#         if x not in c:
#             c.append(x)
#     b = c
#     return b
#
#
# # 获取n与k
# n, k = map(int, input().split())
#
# lis_border = [[0, 0, 0, 0] for _ in range(n)]
#
# for i in range(n):
#     lis_border[i] = list(map(int, input().split()))
#     lis_border[i].append(i + 1)
#
# lis_border = lis_border[::-1]
#
# lis_dot = [[0, 0] for _ in range(k)]
# for i in range(k):
#     lis_dot[i] = list(map(int, input().split()))
#
# a = 0
# xx = []
# for i in range(k):
#     for j in range(n):
#         # 如果在矩形内
#         if lis_border[j][0] <= lis_dot[i][0] <= lis_border[j][2] and lis_border[j][1] <= lis_dot[i][1] <= lis_border[j][3]:
#             a = lis_border[j][-1]
#             xx = lis_border[j]
#             break
#
#     if a == 0:
#         print('IGNORED')
#     else:
#         print(a)
#         lis_border = exChange(xx, lis_border)
#
#     a = 0

# def fit(a, b):
#     for m in range(4):
#         for n in range(4):
#             if b[m][n] == 0:
#                 continue
#             elif b[m][n] == 1 and a[m][n] == 1:
#                 return 0
#             else:
#                 return 1
#
#
# def change(a, b):
#     count = 0
#     # 判断最后是否为全0行
#     for m in range(3, -1, -1):
#         if b[m][0] == 0 and b[m][1] == 0 and b[m][2] == 0 and b[m][3] == 0:
#             count += 1
#         else:
#             break
#
#     for m in range(count, 4):
#         for n in range(4):
#             if b[m - count][n] == 1 and a[m][n] == 0:
#                 a[m][n] = 1
#     return a
#
#
# def turn(kk, stat, a, c):
#     for m in range(kk, kk + 4):
#         for n in range(stat - 1, stat + 3):
#             x = c[m][n]
#             y = a[m - kk][n - stat + 1]
#             c[m][n] = y
#     return c
#
#
# lit_lis = [[0 for _ in range(10)] for _ in range(15)]
# for i in range(15):
#     lit_lis[i] = list(map(int, input().split()))
#
# new_lis = [[0 for _ in range(4)] for _ in range(4)]
# for i in range(4):
#     new_lis[i] = list(map(int, input().split()))
#
# left = int(input())
#
# lis_choice = [[[0 for _ in range(4)] for _ in range(4)] for _ in range(12)]
#
# for i in range(12):
#     for j in range(4):
#         for k in range(4):
#             lis_choice[i][j][k] = lit_lis[i + j][left - 1 + k]
#
# lis = [0 for _ in range(12)]
# for i in range(12):
#     lis[i] = fit(lis_choice[i], new_lis)
#
# # 查找最后一个值为1的索引
# last_index = None
# for i in range(len(lis) - 1, -1, -1):
#     if lis[i] == 1:
#         last_index = i
#         break
#
# lis_choice[last_index] = change(lis_choice[last_index], new_lis)
#
# lit_lis = turn(last_index, left, lis_choice[last_index], lit_lis)
#
# for i in range(15):
#     print(*lit_lis[i], sep=' ')

# import math
# num = int(input())
# shuiQian = 0
# if num <= 3500:
#     shuiQian = num
# elif num <= 4955:
#     shuiQian = (num - 105) / 0.97
# elif num <= 7655:
#     shuiQian = (num - 455) / 0.9
# elif num <= 11255:
#     shuiQian = (num - 1255) / 0.8
# elif num <= 30755:
#     shuiQian = (num - 1880) / 0.75
# elif num <= 44755:
#     shuiQian = (num - 3805) / 0.7
# elif num <= 61005:
#     shuiQian = (num - 6730) / 0.65
# else:
#     shuiQian = (num - 15080)/0.55
# print(math.ceil(shuiQian))


# n = int(input())
# tim = int(input())
# opp = []
# for i in range(tim):
#     opp.append(list(map(int, input().split())))
#
# lis = []
# for i in range(n):
#     lis.append(i+1)
#
# for i in range(tim):
#     peo = opp[i][0]
#     opera = opp[i][1]
#     for j in range(n):
#         if lis[j] == peo:
#             opera += j
#             break
#     lis.remove(peo)
#     lis.insert(opera, peo)
# print(*lis,sep=" ")

# 10
# 9+3+4x3
# 5+4x5x5
# 7-9-9+8
# 5x6/5x4
# 3+5+7+9
# 1x1+9-9
# 1x9-5/9
# 8/5+6x9
# 6x7-3x6
# 6x4+4/5

# def cou(s):
#     lisA = []
#     for i in range(7):
#         lisA.append(s[i])
#     while "x" in lisA or "/" in lisA:
#         length = (len(lisA)-1)/2
#         for i in range(int(length)):
#             if lisA[i*2 + 1] == "x":
#                 c = str(int(lisA[2*i]) * int(lisA[2*i + 2]))
#                 lisA.pop(i*2)
#                 lisA.pop(i * 2)
#                 lisA.pop(i * 2)
#                 lisA.insert(i*2, c)
#                 break
#             elif lisA[i*2 + 1] == "/":
#                 c = str(int(int(lisA[2*i]) / int(lisA[2*i + 2])))
#                 lisA.pop(i*2)
#                 lisA.pop(i * 2)
#                 lisA.pop(i * 2)
#                 lisA.insert(i*2, c)
#                 break
#     length = (len(lisA) - 1) / 2
#     while "+" in lisA or "-" in lisA:
#         for i in range(int(length)):
#             if lisA[i * 2 + 1] == "+":
#                 c = str(int(lisA[2 * i]) + int(lisA[2 * i + 2]))
#                 lisA.pop(i * 2)
#                 lisA.pop(i * 2)
#                 lisA.pop(i * 2)
#                 lisA.insert(i * 2, c)
#                 break
#             elif lisA[i * 2 + 1] == "-":
#                 c = str(int(int(lisA[2 * i]) - int(lisA[2 * i + 2])))
#                 lisA.pop(i * 2)
#                 lisA.pop(i * 2)
#                 lisA.pop(i * 2)
#                 lisA.insert(i * 2, c)
#                 break
#     return lisA
#
#
# n = int(input())
# lis = [0 for _ in range(n)]
# result = []
# for i in range(n):
#     lis[i] = input()
#     x = cou(lis[i])[0]
#     if x == "24":
#         result.append("Yes")
#     else:
#         result.append("No")
# for i in range(n):
#     print(result[i])

# r,y,g = map(int,input().split())
# n = int(input())
# lis = []
# for i in range(n):
#     lis.append(list(map(int,input().split())))
#
# tim = 0
#
# for i in range(n):
#     if lis[i][0] == 0:
#         tim += lis[i][1]
#     elif lis[i][0] == 1:
#         tim += lis[i][1]
#     elif lis[i][0] == 2:
#         tim += lis[i][1] + r
# print(tim)

liss = [["0",0]]
n, k = map(int, input().split())
for i in range(n):
    s = str(i + 1)
    liss.append([s, i + 1])
while len(liss) > 2:
    lis_del = []
    for i in range(1,len(liss)):
        if liss[i][1] % k == 0 or liss[i][1] % 10 == k:
            lis_del.append(liss[i])
    n = liss[-1][1]
    liss[0] = ["0", n]
    for i in range(len(lis_del)):
        liss.remove(lis_del[i])
    for i in range(1,len(liss)):
        liss[i] = [liss[i][0], 1+liss[i-1][1]]

print(int(liss[-1][0]))

