def generate_magic_square(n):
    magic_square = [[0] * n for _ in range(n)]

    i, j = 0, n // 2

    for num in range(1, n**2 + 1):
        magic_square[i][j] = num
        i -= 1
        j += 1

        if num % n == 0:
            i += 2
            j -= 1
        elif i < 0:
            i = n - 1
        elif j == n:
            j = 0

    return magic_square

def print_magic_square(square):
    for row in square:
        for num in row:
            print(f"{num:3}", end=" ")
        print()

# def main():
#     n = int(input("请输入奇数n（n为奇数）："))
#
#     if n % 2 == 0:
#         print("请输入奇数n！")
#         return
#
#     magic_square = generate_magic_square(n)
#     print("生成的魔方阵为：")
#     print_magic_square(magic_square)

# if __name__ == "__main__":

a = input()
print(type(a))