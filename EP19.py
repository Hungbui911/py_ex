#Nhập vào từ bàn phím một xâu kí tự S. Kiểm tra xâu đó có phải xâu đối xứng không và thông báo kết quả ra màn hình.
s = input().replace(" ", "")
if s == s[::-1]:
    print("YES")
else:
    print("NO")