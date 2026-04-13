# 1. Set là gì?
# Set là một cấu trúc dữ liệu cho phép lưu trữ các phần tử:
# - Không trùng lặp
from lesson_8.list import students

numbers = {1, 2, 3, 4, 5, 1, 2, 3, 4, 5}
print(numbers, "\n")

# - Không có thứ tự
fruits = {"apple", "banana", "cherry"}
print(fruits, "\n")
# Không lấy phần tử theo index được vì vị trí nó không cố định

# 2. Cách tạo set
# 2.1. Tạo set bằng { }
colors = {"red", "green", "blue"}
print(type(colors), "\n")

# 2.2. Tạo set rỗng bằng hàm set()
# Không dùng { } vì đó là dictionary rỗng
empty_set = set()
print(empty_set, "\n")
print(type(empty_set), "\n")

# 2.3. Tạo set từ list
numbers_list = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
numbers_set = set(numbers_list)
print(numbers_set, "\n")
print(type(numbers_set), "\n")

# 2.4. Tạo set từ chuỗi
text = "Nguyễn Thị Yến Nhi"
text_set = set(text)
print(text_set, "\n")
print(type(text_set), "\n")

# 2.5. Tạo set từ tuple
numbers_tuple = (1, 2, 3, 4, 5, 1, 2, 3, 4, 5)
numbers_set = set(numbers_tuple)
print(numbers_set, "\n")
print(type(numbers_set), "\n")

# 3. Các thao tác / phương thức cơ bản
# 3.1. Lấy chiều dài, số lượng phần tử
numbers = {1, 2, 3, 4, 5, 1, 2, 3, 4, 5}
print(len(numbers), "\n")

# 3.2. Kiểm tra 1 phần tử có nằm trong set không
students = {"Nhi", "Huệ", "Mai", "Dương"}
if "Nhi" in students:
    print("Yes", "\n")
else:
    print("No", "\n")

# 3.3. Thêm một phần tử vào set
students.add("Hoa")
print(students, "\n")
students.add("Nhi")
print(students, "\n")

# 3.4. Thêm nhiều phần tử vào set
students.update(["Huế", "Tiên"])
print(students, "\n")

# 3.5. Xóa 1 phần tử
students.discard("Tiên")
print(students, "\n")

students.remove("Hoa")
print(students, "\n")

# 3.6. Xóa một phần tử ngẫu nhiên
print(colors, "\n")
deleted_color = colors.pop()
print(deleted_color, "\n")
print(colors, "\n")

# 3.7. Xóa toàn bộ set
colors.clear()
print(colors, "\n")

# 3.8. Copy (shallow)
print(students, "\n")
students_copy = students.copy()
print(students_copy, "\n")
students_copy.remove("Huế")
print(students_copy, "\n")

# Bản gốc không bị đổi
print(students, "\n")

# 4. Duyệt các phần tử trong set dùng vòng lặp
# Do set không có thứ tự nên mỗi lần chạy có thể in ra khác nhau
for student in students:
    print(student, "\n")