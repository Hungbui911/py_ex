#. Nhập vào từ bàn phím một xâu kí tự, chuẩn hóa xâu sao cho không có dấu cách ở đầu và cuối xâu, 
# giữa hai từ trong xâu cách nhau đúng một dấu cách. 
# Thông báo kết quả ra màn hình.  
xau = input()
xau = xau.split()
xau_chuan_hoa = ''
for i in xau:
    if i != '':
        xau_chuan_hoa += i + ' '
print(xau_chuan_hoa)