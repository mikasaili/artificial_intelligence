import operator
import sys
import numpy as np

class staObject:
    def __init__(self):
        # 当前状态序列
        self.array = []
        # f(n)
        self.fn = 0
        # 上一步操作
        self.lastOperation = 0
        # d(n)
        self.dn = 0
        self.father = staObject


def get_operation(i1, lastOperation):
    select = []
    # 向上操作,上一步操作不能为向下，否则会陷入死循环
    if 3 <= i1 <= 8 and lastOperation != 2:
        select.append(1)
    # 向下
    if 0 <= i1 <= 5 and lastOperation != 1:
        select.append(2)
    # 向左
    if i1 != 0 and i1 != 3 and i1 != 6 and lastOperation != 4:
        select.append(3)
    # 向右
    if i1 != 2 and i1 != 5 and i1 != 8 and lastOperation != 3:
        select.append(4)
    return select


def ArrByOperation(old, arr1, op):
    a = 0
    if op == 1:
        a = old - 3
    if op == 2:
        a = old + 3
    if op == 3:
        a = old - 1
    if op == 4:
        a = old + 1

    tem = arr1[a]
    arr1[a] = arr1[old]
    arr1[old] = tem
    return arr1


def wn(current, end0):
    count = 0
    current = np.array(current)
    endList0 = np.array(end0)

    for ii in range(len(current)):
        if current[ii] != 0 and current[ii] != endList0[ii]:
            count += 1
    return count


def dist(value, current, end0):
    def x1(index):
        if 0 <= index <= 2:
            return 0
        if 3 <= index <= 5:
            return 1
        if 6 <= index <= 8:
            return 2

    def y1(index):
        if index % 3 == 0:
            return 0
        if index % 3 == 1:
            return 1
        if index % 3 == 2:
            return 2

    currentIndex = current.index(value)
    currentX = x1(currentIndex)
    currentY = y1(currentIndex)
    endIndex = end0.index(value)
    endX = x1(endIndex)
    endY = y1(endIndex)

    dis = abs(currentX - endX) + abs(currentY - endY)

    return dis


def totalDist(current, end0):
    length = 0
    for item1 in current:
        if item1 != 0:
            length += dist(item1, current, end0)
    return length


def revNum(arr0):
    count = 0
    for i in range(len(arr0)):
        for j in range(len(arr0)):
            if arr0[i] > arr0[j]:
                count += 1
    return count


if __name__ == '__main__':
    start = int(input("是否要进行八解码问题求解（0为否，1为是）："))
    while start:
        # 执行
        countDn = 0
        openList = []
        closed = []
        print("请依次输入八解码的起始状态：")
        initObject = staObject()
        arr = initObject.array
        for i in range(9):
            x = input("第" + str(i) + "位" + "为：")
            arr.append(int(x))

        print("请依次输入八解码的终止状态：")
        end = []
        for i in range(9):
            x = input("第" + str(i) + "位" + "为：")
            end.append(int(x))

        initObject.fn = countDn + wn(arr, end)
        openList.append(initObject)
        zeroIndex = openList[0].array.index(0)

        initRev = revNum(arr) - zeroIndex
        print("起始序列逆序数", initRev)
        endRev = revNum(end) - zeroIndex
        print("终止序列逆序数", endRev)

        # 距离之和
        res = totalDist(initObject.array, end)

        if (initRev % 2 == 0 and endRev % 2 == 0) or (initRev % 2 != 0 and endRev % 2 != 0):
            finalFlag = 0
            while 1:
                # 判断是否为end状态
                if operator.eq(openList[0].array, end):
                    # 更新表，并退出
                    deep = openList[0].dn
                    finalFlag = finalFlag + 1
                    closed.append(openList[0])
                    endList = []
                    del openList[0]
                    if finalFlag == 1:
                        father = closed[-1].father
                        endList.append(end)
                        print("最终状态为:")
                        print(end)
                        while father.dn >= 1:
                            endList.append(father.array)
                            father = father.father
                        endList.append(initObject.array)
                        print("【变换成功,共需要" + str(deep) + "次变换】")
                        for item in reversed(endList):
                            print(item)
                        sys.exit()
                else:
                    countDn = countDn + 1
                    # 找到选中的状态0下标
                    zeroIndex = openList[0].array.index(0)
                    # 获得该位置可select的operation
                    operation = get_operation(zeroIndex, openList[0].lastOperation)
                    tempStatusList = []
                    for opeNum in operation:
                        # 根据操作码返回改变后的数组
                        copyArray = openList[0].array.copy()
                        newArray = ArrByOperation(zeroIndex, copyArray, opeNum)
                        newStatusObj = staObject()  # 构造新对象插入open表
                        newStatusObj.array = newArray
                        newStatusObj.dn = openList[0].dn + 1  # 更新dn 再计算fn
                        newFn = newStatusObj.dn + wn(newArray, end)
                        # newFn = newStatusObj.Dn + countTotalLength(newArray, endArray)
                        newStatusObj.fn = newFn
                        newStatusObj.lastOperation = opeNum
                        newStatusObj.father = openList[0]
                        tempStatusList.append(newStatusObj)
                    # 将操作后的tempStatusList按Fn的大小排序
                    tempStatusList.sort(key=lambda t: t.fn)
                    # 更新closed表
                    closed.append(openList[0])
                    # 更新open表
                    del openList[0]
                    for item in tempStatusList:
                        openList.append(item)
                    # 根据Fn将open表进行排序
                    openList.sort(key=lambda t: t.fn)

        else:
            print("无法搜到有效解")

        start = int(input("是否要进行八解码问题求解（0为否，1为是）："))
