# 1. List là gì?
# List là một danh sách chứa các phần tử có thể trùng lặp
# List gom một nhóm các dữ liệu vào với nhau để quản lý cho gọn

##################################################################################
# 2. Cách nhận biết một list là cặp ngoặc vuông [] ngăn cách nhau bởi dấu phẩy (,)
fruits = ["apple", "banana", "cherry"]
mix = ["apple", "banana", "cherry", 1, 5, True, "Yến Nhi"]

# Vị trí các phần tử trong list bắt đầu từ 0, 1, 2,...,n
# Vị trí các phần tử có thể thay đổi được

##################################################################################
# 3. Các thao tác cơ bản
#  Lấy trái cây ở ngăn đầu
print(fruits[0], "\n")

# Thêm trái cây mới vào khay
fruits.append("mango")

# Thay thế vị trí của ngăn trái cây bất kỳ
fruits[1] = "orange"

# Lấy trái cây ở ngăn cuối
print(fruits[-1], "\n")

# In ra toàn bộ trái cây
print(fruits, "\n")

# Tạo ra danh sách rỗng
empty_list = list()
print(empty_list, "\n")

# Tạo list từ hàm range()
range(2, 10, 2) # 2, 4, 6, 8
range_number = list(range(2, 10, 2))
print(range_number, "\n")

# Lấy ra độ dài của list
print(len(fruits), "\n") # len = length

# Kiểm tra phần tử có tồn tại trong list không
if "banana" in fruits:
    print("Yes", "\n")
else:
    print("No", "\n") # Chạy vào đây vì banana bị thay thế bởi orange rồi

# Nối 2 chuỗi
combo = fruits + mix
print(combo, "\n")

# lặp lại các phần tử trong list
my_name = ["Nguyễn Thị Yến Nhi"] * 3
print(my_name, "\n")

list_nhi = my_name * 10
print(list_nhi, "\n")

# Lấy một phần của list (slicing), cắt 1 phần list
print(fruits[::], "\n") # fruits[start:stop:step] >> [0, 5, 1]
print(fruits[::2], "\n") # [0, 5, 2]
print(fruits[:3:], "\n") # [0, 3, 1]
print(fruits[1:], "\n") # [1, 5, 1]
print(fruits[1::2], "\n") # [1, 5, 2]

print(fruits[2:4], "\n") # Lấy từ vị trí 2 đến vị trí 3

# 4. Các hàm phổ biến trong list
# Chèn môt phần tử vào cuối chuỗi
students = ["Nhi", "Huệ", "Mai"]
students.append("Trang")
print(students, "\n")

# Chèn một phần tử x vào vị trí i
students.insert(2, "Dương")
print(students, "\n")

# Nối list
new_students = ["Huế", "Ánh"]
students.extend(new_students)
print(students, "\n")

# Xóa phần tử x
students.remove("Ánh")
print(students, "\n")

# Xóa và in ra giá trị bị xóa
removed_student = students.pop(4)
print(students, "\n")
print(removed_student, "\n")

# Xóa toàn bộ list
check_clear_all = [1, 2, 3, 4, 5]
check_clear_all.clear()
print(check_clear_all, "\n")

# Sắp xếp (sort)
print(students, "\n")
students.sort()
print(students, "\n")

students.sort(reverse=True)
print(students, "\n")

# Đảo ngược list
list_reverse = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_reverse.reverse()
print(list_reverse, "\n")

# Đếm số lần xuất hiện của một phần tử
students.append("Nhi")
cout_nhi = students.count("Nhi")
print(f"Nhi xuất hiện {cout_nhi} lần trong danh sách", "\n")

# 5. Duyệt list
# Duyệt list bằng for
for student in students:
    print(student, "\n")

# Duyệt bằng index (chỉ số)
for index in range(len(students)):
    print(students[index], "\n")

# Nguyễn Thị Yến Nhi - 2026