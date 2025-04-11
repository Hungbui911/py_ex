# Nhập vào từ bàn phím số nguyên dương N (4  N  100) và dãy A gồm N số nguyên. 
# Tính trung bình cộng của các số chia hết cho 3 trong dãy A.
n = int(input())
if n < 4 or n > 100:
    print("N phai nam trong khoang [4, 100]")
else:
    a = list(map(int, input().split()))
    if len(a) != n:
        print("Khong hop le")
    else:
        s = 0
        count = 0
        for i in a:
            if i % 3 == 0:
                s += i
                count += 1
        if count == 0:
            print("Khong co so chia het cho 3")
        else:
            print(s / count)