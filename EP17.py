# Tìm ước chung lớn nhất của hai số nguyên dương M, N
def ucln(m, n):
    if n == 0:
        return m
    return ucln(n, m % n)
m, n = map(int, input().split())
print(ucln(m, n))