# Nhập vào từ bàn phím một số nguyên dương N (4  N  100) và dãy A gồm N số nguyên. 
# Kiểm tra xem dãy A đã sắp xếp theo trật tự không giảm chưa? Nếu chưa hãy sắp  xếp dãy A theo trật tự không giảm.
n = int(input())

if n < 4 or n > 100:
    print("N không hợp lệ")
else:
    a = list(map(int, input().split()))
    
    if len(a) != n:
        print("Số lượng phần tử không đúng.")
    else: 
        is_sorted = True
        for i in range(1, n):
            if a[i] < a[i - 1]:
                is_sorted = False
                break

        if is_sorted:
            print("Dãy A đã được sắp xếp theo thứ tự không giảm.")
        else: 
            a.sort()
            print(*a)