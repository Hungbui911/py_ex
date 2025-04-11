# Nhập vào từ bàn phím một xâu kí tự S. Đưa ra màn hình: Xâu đảo ngược của xâu S, số lượng các kí tự số trong xâu S.
s = input()
dao_s = s[::-1]
dem_so = sum(1 for char in s if char.isdigit())
print(dao_s)
print(dem_so)