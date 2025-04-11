# Nhập vào từ bàn phím số nguyên dương N (4  N  100) và dãy A gồm N số nguyên. 
# Tìm giá trị lớn nhất của dãy A.
n = int(input())
a = list(map(int, input().split()))
gtln = a[0]
for i in range(1, n):
    if a[i] > gtln:
        gtln = a[i]
print(gtln)