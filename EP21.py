# Tính giá trị của đa thức: P(x)=anxn + an-1xn-1+...+a1x + a0 tại x = x0, 
# với n là số nguyên dương, a0,...,an, x0 là các số thực được nhập vào từ bàn phím.
n = int(input())

if n <= 0:
    print("Số lượng hệ số không đúng.")
else:
    a = list(map(float, input().split()))
    
    if len(a) != n + 1:
        print("Số lượng hệ số không đúng.")
    else:
        x0 = float(input())
        
        P = 0
        for i in range(n + 1):
            P += a[i] * (x0 ** i)
        
        print(P)
