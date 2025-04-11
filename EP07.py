# Nhập vào từ bàn phím số nguyên dương N (4 <= N <= 100) và dãy A gồm N số nguyên.
# Cho biết trong dãy A có bao nhiêu số chính phương.
n = int(input())
if n < 4 or n > 100:
    print("N không hợp lệ")
else:
    a = list(map(int, input().split()))
    if len(a) != n:
        print("Số lượng phần tử không đúng")
    else:
        count = 0
        for i in a:
            if i >= 0:
                x = int(i ** 0.5)
                if x * x == i:
                    count += 1
        print("Số lượng số chính phương trong dãy A là:", count)

