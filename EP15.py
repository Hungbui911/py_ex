# Nhập vào từ bàn phím một xâu kí tự S và thông báo ra màn hình số lần xuất hiện của 
# mỗi chữ cái tiếng Anh trong S (không phân biệt chữ hoa hay chữ thường)”.
s = input().lower()
s = s.replace(" ", "")  # Xóa khoảng trắng trong xâu
dem = {}

for ch in s:
    if 'a' <= ch <= 'z':  
        if ch not in dem:
            dem[ch] = 1
        else:
            dem[ch] += 1

# In kết quả
if dem:
    for ch in sorted(dem.keys()):
        print(f"'{ch}': {dem[ch]}")
else:
    print("Không có chữ cái tiếng Anh nào trong xâu.")