# Nhập vào từ bàn phím số nguyên dương N (4  N  100), số nguyên tố k và dãy A gồm N số nguyên. 
# Cho biết trong dãy A có bao nhiêu số chia hết cho k.
def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input())
if n < 4 or n > 100:
    print("N không hợp lệ")
else:
    k = int(input())
    if not la_so_nguyen_to(k):
        print("k không phải là số nguyên tố")
    else:
        a = list(map(int, input().split()))
        if len(a) != n:
            print("Số lượng phần tử không đúng")
        else:
            count = 0
            for x in a:
                if x % k == 0:
                    count += 1
            print( count)


