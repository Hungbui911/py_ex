#Nhập từ bàn phím xâu kí tự S chỉ gồm các chữ cái. Hãy cho biết số lượng các chữ cái khác nhau xuất hiện trong xâu S
s = input()
dem = 0
for i in range(len(s)):
    if s[i] not in s[:i]:
        dem += 1
print(dem)