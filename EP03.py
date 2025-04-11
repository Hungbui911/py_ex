#Nhập vào từ bàn phím một số nguyên dương N (4  N  100) và dãy A gồm N số nguyên.
#Tìm ước chung lớn nhất của dãy A.
def ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return a

n = int(input())
if n < 4 or n > 100:
    print("N không hợp lệ")
else:
    a = list(map(int, input().split()))
    if len(a) != n:
        print("Số lượng phần tử không đúng")
    else:
        kq = a[0]
        for i in range(1, n):
            kq = ucln(kq, a[i])
        print( kq)
