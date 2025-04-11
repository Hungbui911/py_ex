# Nhập vào từ bàn phím số nguyên dương N (4 <= N <= 100) và dãy A gồm N số nguyên.
# Tìm số lớn thứ nhì của dãy A.
n = int(input())
a = list(map(int, input().split()))
if n < 4 or n > 100:
    print("N không hợp lệ")
else:
    a = list(set(a))
    a.sort(reverse=True) 
    print(a[1])