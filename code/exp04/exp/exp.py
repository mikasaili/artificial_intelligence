import random

# 工件数
work_num = 5
# 机器数
machine_num = 4
# 种群数
max_zhongqun = 20
# 交叉概率
pc = 0.6
# 变异概率
pm = 0.1
# 迭代次数
interation = 10
# 工件每个机器加工时间
time_all = [[31, 41, 25, 30], [19, 55, 3, 34],
            [23, 42, 27, 6], [13, 22, 14, 13],
            [33, 5, 57, 19]]
# 顺序
sequence = [0 for _ in range(work_num)]


class population:
    def __init__(self):
        self.job = [0 for _ in range(work_num)]
        # 加工时间
        self.time_ = 0
        # 适应度
        self.fit = 0.0
        # 选择概率
        self.p = 0.0
        # 累计概率
        self.q = 0.0


def search(a, b):
    for k in range(work_num):
        if a == b[k]:
            return k
    return -1


# 初始化
def init_population(p):
    for i in range(max_zhongqun):
        v = list(range(work_num))
        for j in range(work_num):
            a = random.randint(0, len(v) - 1)
            p[i].job[j] = v[a]
            v.pop(a)


# 适应度
def fitness(p):
    for i in range(max_zhongqun):
        c = [[0 * machine_num] for _ in range(work_num)]
        c[p[i].job[0]][0] = time_all[p[i].job[0]][0]
        for j in range(1, machine_num):
            c[p[i].job[0]][j] = c[p[i].job[0]][j - 1] + time_all[p[i].job[0]][j]
        for j in range(1, work_num):
            c[p[i].job[j]][0] = c[p[i].job[j - 1]][0] + time_all[p[i].job[j]][0]
        for j in range(1, work_num):
            for k in range(1, machine_num):
                c[p[i].job[j]][k] = max(c[p[i].job[j - 1]][k], c[p[i].job[j]][k - 1]) + time_all[p[i].job[j]][k]
        p[i].time = c[p[i].job[work_num - 1]][machine_num - 1]
        p[i].fit = 1.0 / p[i].time


# 选择
def select(p):
    sum_fit = 0.0
    sum_q = 0.0
    for i in range(max_zhongqun):
        sum_fit += p[i].fit
    for i in range(max_zhongqun):
        p[i].p = p[i].fit / sum_fit
        sum_q += p[i].p
        p[i].q = sum_q

    temp = [population() for _ in range(max_zhongqun)]
    for i in range(max_zhongqun):
        j = 0
        a = random.uniform(0, 1)
        if a <= p[0].q:
            # 浅拷贝
            temp[i].__dict__ = p[0].__dict__.copy()
            continue
        else:
            while p[j - 1].q < a <= p[j].q:
                j += 1
        temp[i].__dict__ = p[j].__dict__.copy()
    for i in range(max_zhongqun):
        p[i].__dict__ = temp[i].__dict__.copy()

    # for i in range(max_zhongqun):
    #     j = 0
    #     a = random.uniform(0, 1)
    #     if a <= p[0].q:
    #         temp[i] = p[0]
    #         continue
    #     else:
    #         for j in range(1, max_zhongqun):
    #             if p[j - 1].q < a <= p[j].q:
    #                 break
    #     temp[i] = p[j]
    #
    # for i in range(max_zhongqun):
    #     p[i] = temp[i]


# 交叉
def crossover(p):
    n = int(pc * 10)
    while n > 0:
        ia = 0
        ib = 0
        while ia == ib:
            ia = random.randint(0, max_zhongqun - 1)
            ib = random.randint(0, max_zhongqun - 1)
        a, b = 0, 0
        while a == b or a >= b:
            a = random.randint(0, work_num - 1)
            b = random.randint(0, work_num - 1)
        arr = [-1] * work_num
        brr = [-1] * work_num
        for j in range(a, b):
            arr[p[ia].job[j]] = p[ib].job[j]
            brr[p[ib].job[j]] = p[ia].job[j]
            t = p[ia].job[j]
            p[ia].job[j] = p[ib].job[j]
            p[ib].job[j] = t
        for j in range(a):
            while search(p[ia].job[j], arr) != 1:
                p[ia].job[j] = search(p[ia].job[j], arr)
        for j in range(b, work_num):
            while search(p[ia].job[j], arr) != 1:
                p[ia].job[j] = search(p[ia].job[j], arr)
        for j in range(a):
            while search(p[ib].job[j], brr) != 1:
                p[ib].job[j] = search(p[ib].job[j], brr)
        for j in range(b,work_num):
            while search(p[ib].job[j], brr) != 1:
                p[ib].job[j] = search(p[ib].job[j], brr)

        n -= 1


# 变异
def mutation(p):
    n = int(pm * 10)
    while n > 0:
        index = random.randint(0, max_zhongqun - 1)
        a, b = 0, 0
        while a == b:
            a = random.randint(0, work_num - 1)
            b = random.randint(0, work_num - 1)
        temp = p[index].job[a]
        p[index].job[a] = p[index].job[b]
        p[index].job[b] = temp
        n -= 1


if __name__ == "__main__":
    p = [population() for _ in range(max_zhongqun)]
    random.seed()
    init_population(p)
    cnt = 0
    best_time = float('inf')
    while cnt < interation:
        fitness(p)
        jubu_best = min([i.time_ for i in p])
        print(f"第{cnt + 1}代, 最短加工时间为: {jubu_best}")

        select(p)
        crossover(p)
        mutation(p)

        for i in p:
            if i.time_ <= best_time:
                best_time = i.time_
                sequence = i.job.copy()

        cnt += 1
        print(f"最短加工时间为：{best_time}")
        print("最优加工序列为：", end=" ")
        for i in range(work_num):
            if i == 0:
                print(sequence[i] + 1, end="")
            else:
                print(f"-{sequence[i] + 1}", end="")
        print()

