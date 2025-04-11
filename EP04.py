# Nhập vào từ bàn phím số nguyên dương (4 <= N <= 100) và dãy A gồm N số nguyên. 
# Cho biết dãy được tạo thành bởi những số nào?
n = int(input())
if n < 4 or n > 100:
    print("N không hợp lệ")
else:
    a = list(map(int, input().split()))
    so = list(dict.fromkeys(a))
    print("Dãy được tạo thành bởi những số:", *so)
