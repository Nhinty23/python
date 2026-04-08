# Khác với toán tử số học trả về con số, toán tử so sánh luôn trả về giá trị kiểu logic (Boolean) hoặc là true hoặc là false

# 1. Danh sách các toán tử:
# Giả sử chúng ta có 2 biến a = 10 và b = 20
# So sánh bằng ( == ). Ví dụ: a == b => false
# So sánh khác ( != ). Ví dụ: a != b => true
# So sánh lớn hơn ( > ). Ví dụ: a > b => false
# So sánh nhỏ hơn ( < ). Ví dụ: a < b => true
# So sánh lớn hơn hoặc bằng ( >= ). Ví dụ: a >= b => false
# So sánh nhỏ hơn hoặc bằng ( <= ). Ví dụ: a <= b => true

# 2. Lưu ý
# - Dấu bằng ( = ) và dấu bằng bằng ( == ) khá giống nhau nhưng đừng nhầm lẫn nhé.
# + Dấu bằng thường dùng để gán giá trị khi khai báo biến
# + Dấu bằng bằng là toán tử so sánh nhé
# - Bạn cũng có thể dùng toán tử so sánh để so sánh chữ  cái. Python so sánh dựa trên mã Unicode (Thường thì chữ cái đứng sau trong bảng chữ cái sẽ lớn hơn)
# + Ví dụ: ""Apple" < "Banana" => True

# 3. Bài tập thực hành
# Nhập 2 số a và b và tiến hành in ra kết quả so sánh
a = float(input(f"Bạn vui lòng nhập vào số a : "))
b = float(input(f"Bạn vui lòng nhập vào số b : "))

print(f"Kết quả so sánh giữa {a} và {b}:")
if a > b:
    print(f"Số {a} lớn hơn số {b}")
elif a < b:
    print(f"Số {a} nhỏ hơn số {b}")
elif a == b:
    print(f"Số {a} bằng số {b}")

print("\n")

# >> Trong java là else if thì trong python là elif

# Nhập tuổi là age để kiểm tra độ tuổi lái xe

age = int(input(f"Mời bạn nhập tuổi: "))
if age < 18:
    print(f"Bạn mới {age} tuổi chưa đủ tuổi lái xe đâu nhé !!!")
elif age >= 18:
    print(f"Bạn đã {age} tuổi đủ tuổi lái xe rồi nhé nhé !!!")
