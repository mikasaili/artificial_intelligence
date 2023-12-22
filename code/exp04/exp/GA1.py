import random

gongjian_num = 5  # 工件数量
machine_num = 4  # 机器数量
maxn = 20  # 种群数量
pc = 0.6  # 交叉概率
pm = 0.1  # 变异概率
iteration = 30

time_all = [
    [31, 41, 25, 30],
    [19, 55, 3, 34],
    [23, 42, 27, 6],
    [13, 22, 14, 13],
    [33, 5, 57, 19]
]

best = [0] * gongjian_num


class Population:
    def __init__(self):
        self.job = [0] * gongjian_num
        self.time = 0
        self.fit = 0.0
        self.p = 0.0
        self.q = 0.0


def MAX(a, b):
    return a if a >= b else b


def search(a, b):
    for k in range(gongjian_num):
        if a == b[k]:
            return k
    return -1


def init_population(p):
    for i in range(maxn):
        v = list(range(gongjian_num))
        for j in range(gongjian_num):
            a = random.randint(0, len(v) - 1)
            p[i].job[j] = v[a]
            v.pop(a)


def fitness(p):
    for i in range(maxn):
        c = [[0] * machine_num for _ in range(gongjian_num)]
        c[p[i].job[0]][0] = time_all[p[i].job[0]][0]
        for j in range(1, machine_num):
            c[p[i].job[0]][j] = c[p[i].job[0]][j - 1] + time_all[p[i].job[0]][j]
        for j in range(1, gongjian_num):
            c[p[i].job[j]][0] = c[p[i].job[j - 1]][0] + time_all[p[i].job[j]][0]
        for j in range(1, gongjian_num):
            for k in range(1, machine_num):
                c[p[i].job[j]][k] = MAX(c[p[i].job[j - 1]][k], c[p[i].job[j]][k - 1]) + time_all[p[i].job[j]][k]
        p[i].time = c[p[i].job[gongjian_num - 1]][machine_num - 1]
        p[i].fit = 1.0 / p[i].time


def select_population(p):
    sum_fit = sum(x.fit for x in p)
    sum_q = 0.0
    for i in range(maxn):
        p[i].p = p[i].fit / sum_fit
        sum_q += p[i].p
        p[i].q = sum_q
    temp = [Population() for _ in range(maxn)]
    for i in range(maxn):
        j = 0
        a = random.uniform(0, 1)
        if a <= p[0].q:
            temp[i].__dict__ = p[0].__dict__.copy()
            continue
        else:
            for j in range(1,maxn):
                if p[j-1].q<a<=p[j].q:
                    break
        temp[i].__dict__ = p[j].__dict__.copy()
    for i in range(maxn):
        p[i].__dict__ = temp[i].__dict__.copy()


def crossover_population(p):
    n = int(pc * 10)
    while n > 0:
        ia, ib = 0, 0
        while ia == ib:
            ia = random.randint(0, maxn - 1)
            ib = random.randint(0, maxn - 1)
        a, b = 0, 0
        while a == b or a > b :
            a = random.randint(0, gongjian_num - 1)
            b = random.randint(0, gongjian_num - 1)
        arr, brr = [-1] * gongjian_num, [-1] * gongjian_num
        for j in range(a, b):
            arr[p[ia].job[j]] = p[ib].job[j]
            brr[p[ib].job[j]] = p[ia].job[j]
            p[ia].job[j], p[ib].job[j] = p[ib].job[j], p[ia].job[j]
        for j in range(a):
            while search(p[ia].job[j], arr) != -1:
                p[ia].job[j] = search(p[ia].job[j], arr)
        for j in range(b, gongjian_num):
            while search(p[ia].job[j], arr) != -1:
                p[ia].job[j] = search(p[ia].job[j], arr)
        for j in range(a):
            while search(p[ib].job[j], brr) != -1:
                p[ib].job[j] = search(p[ib].job[j], brr)
        for j in range(b,gongjian_num):
            while search(p[ib].job[j], brr) != -1:
                p[ib].job[j] = search(p[ib].job[j], brr)
        # for j in range(a):
        #     while arr[p[ia].job[j]] != -1:
        #         p[ia].job[j] = search(p[ia].job[j], arr)
        # for j in range(b, gongjian_num):
        #     while arr[p[ia].job[j]] != -1:
        #         p[ia].job[j] = search(p[ia].job[j], arr)
        # for j in range(a):
        #     while brr[p[ib].job[j]] != -1:
        #         p[ib].job[j] = search(p[ib].job[j], brr)
        # for j in range(b, gongjian_num):
        #     while brr[p[ib].job[j]] != -1:
        #         p[ib].job[j] = search(p[ib].job[j], brr)
        n -= 1


def mutation_population(p):
    n = int(pm * 10)
    while n > 0:
        index = random.randint(0, maxn - 1)
        a, b = 0, 0
        while a == b:
            a = random.randint(0, gongjian_num - 1)
            b = random.randint(0, gongjian_num - 1)
        p[index].job[a], p[index].job[b] = p[index].job[b], p[index].job[a]
        n -= 1


def main():
    result = []
    lun_num = []
    for j in range(20):
        lun = []
        jubu = []
        p = [Population() for _ in range(maxn)]
        random.seed()
        init_population(p)
        cnt = 0
        best_time = float('inf')  # Initialize best_time
        while cnt < iteration:
            fitness(p)
            jubu_best = min(x.time for x in p)
            jubu.append(jubu_best)
            print(f"第{cnt + 1}代,最短加工时间为:{jubu_best}")
            select_population(p)
            crossover_population(p)
            mutation_population(p)
            for i in range(maxn):
                if p[i].time <= best_time:
                    best_time = p[i].time
                    best = p[i].job.copy()
            cnt += 1
        print(f"最短加工时间为：{best_time}")
        result.append(best_time)
        for i in range(iteration):
            if jubu[i] == best_time:
                lun.append(i+1)
        print("最优加工序列为：", end=" ")
        for i in range(gongjian_num):
            if i == 0:
                print(best[i] + 1, end="")
            else:
                print(f"-{best[i] + 1}", end="")
        print()
        lun_num.append(lun)

    mintime = min(result)
    maxtime = max(result)
    print(result)
    count = 0
    c = 0
    x = 0
    ave = 0
    for i in range(len(result)):
        ave += result[i]
        if result[i] == mintime:
            c += len(lun_num[i])
            x += 1
            for j in range(len(lun_num[i])):
                count += lun_num[i][j]
    ave = ave/20
    print("最短时间：", mintime)
    print("最长时间：", maxtime)
    print("最好解的频率", x)
    print("平均时间：", ave)
    print("最好解的平均迭代次数:", count/c)


if __name__ == "__main__":
    main()
