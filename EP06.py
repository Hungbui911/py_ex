#Nhập vào từ bàn phím số nguyên dương N (4  N  100) và dãy A gồm N số nguyên.
# Cho biết trong dãy A có bao nhiêu số nguyên tố.
n = int(input())
a = list(map(int, input().split()))
if n < 4 or n > 100:
    print("N không hợp lệ")
else:
    sl_snt = 0
    ds_snt = []

    for x in a:
        if x < 2:
            continue
        so_nguyen_to = True
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                so_nguyen_to = False
                break
        if so_nguyen_to:
            sl_snt += 1
            ds_snt.append(x)

    print(sl_snt)