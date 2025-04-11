# Nhập vào từ bàn phím số nguyên dương N (4 < N < 100) và dãy A gồm N số nguyên.
# Hãy cho biết dãy A có phải là một cấp số cộng không và thông báo kết quả ra màn hình
n = int(input())
a = list(map(int, input().split()))
if n < 4 or n > 100:
    print("N không hợp lệ")
else:  
    d = a[1] - a[0]
    csc = True
    for i in range(2, n):
        if a[i] - a[i-1] != d:
            csc = False
            break
    if csc:
        print("YES")
    else:
        print("NO")