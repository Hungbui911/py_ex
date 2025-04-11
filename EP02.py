# Nhập từ bàn phím số nguyên dương n (4  N  100) và đưa ra màn hình số hạng thứ n
# của dãy Phi-bo-na-xi (dãy F là dãy Phi-bo-na-xi nếu F0 = F1 = 1; Fn = Fn-1 + Fn-2 với n>=2)


n = int(input())

if n < 4 or n > 100:
    print("N không hợp lệ")
else:
    a = b = 1  
    for i in range(2, n + 1):
        c = a + b
        a, b = b, c
    print(b)
