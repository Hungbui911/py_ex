# Nhập vào từ bàn phím xâu kí tự s1, tạo xâu s2 gồm tất cả các chữ số có trong s1 (giữ nguyên thứ tự xuất hiện của chúng). 
# Cho biết mỗi chữ số xuất hiện bao nhiêu lần”.
s1 = input()

s2 = ""
for ch in s1:
    if ch.isdigit():
        s2 += ch

print(s2)

dem = {}
for ch in s2:
    if ch not in dem:
        dem[ch] = 1
    else:
        dem[ch] += 1

for ch in sorted(dem.keys()):  
    print(f"Số {ch} xuất hiện {dem[ch]} lần")
