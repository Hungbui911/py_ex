# Một khách hàng gửi vào ngân hàng số tiền là A đồng với lãi suất mỗi tháng là r. 
# Biết rằng nếu không rút tiền ra khỏi ngân hàng thì cứ sau mỗi tháng số tiền lãi sẽ được nhập vào gốc 
# để tính lãi cho tháng tiếp theo. 
# Hỏi sau bao nhiêu tháng, người đó rút hết tiền thì sẽ nhận được số tiền ít nhất là B đồng?.
A = float(input())
r = float(input()) 
B = float(input())

if A <= 0 or r <= 0 or B <= A:
    print("Dữ liệu không hợp lệ (A > 0, r > 0, B > A)")
else:
    thang = 0
    goc = A
    while goc < B:
        goc += goc * r  
        thang += 1

    print(f"Sau {thang} tháng, số tiền đạt ít nhất {B} đồng.")
