# Nhập vào từ bàn phím một xâu kí tự. Cho biết xâu có bao nhiêu từ (từ là tập hợp các kí tự phân cách nhau bởi dấu cách). 
# Viết ra màn hình từ có độ dài lớn nhất (nếu có nhiều từ có cùng độ dài lớn nhất thì đưa ra từ có độ dài lớn nhất đầu tiên tìm được)”
s = input().strip()

words = s.split()

if len(words) == 0:
    print("Xâu không chứa từ nào.")
else:
    max_word = words[0]
    for word in words[1:]:
        if len(word) > len(max_word):
            max_word = word
    print("Số từ trong xâu là:", len(words))
    print("Từ có độ dài lớn nhất là:", max_word)
