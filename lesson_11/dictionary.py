# 1. Dictionary là gì
# Dictionary cho phép lưu nhiều phần tử, mỗi phần tử có dạng một cặp key-value
from lesson_10.set import students

my_infor = {"Name": "Nguyễn Thị Yến Nhi",
            "Age": 21,
            "Gender": "Female",
            "Đúng":["Đúng", "Sai"]}
print(my_infor, "\n")
print(type(my_infor), "\n")

# 2. Tính chất:
# 2.1. Có thể thay đổi (mutable): có thể thêm, xóa, sửa các phần tử
print(my_infor, "\n")

# Thêm phần tử
my_infor["Grade"] = 9
print(my_infor, "\n")

# Sửa phần tử
my_infor["Age"] = 22
print(my_infor, "\n")

# Xóa phần tử
del my_infor["Đúng"]
print(my_infor, "\n")

# 2.2. Không có thứ tự cố định ở các bản Python cũ
# Nhưng từ Python 3.7+ thì giữ thứ tự thêm vào
colors = {}
colors["red"] = "đỏ"
colors["yellow"] = "vàng"
colors["orange"] = "cam"
print(colors, "\n")

# 2.3. Key phải duy nhất
# Trùng key => lấy cặp key-value được thêm sau
students = {
    "name": "Yến Nhi",
    "age": 21,
    "grade": 9,
    "name": "Nhi" # name này được thêm sau nên không bị xóa
}
print(students, "\n")

# Ghi đè
students["name"] = "Nguyễn Thị Yến Nhi"
print(students, "\n")

# Nguyễn Thị Yến Nhi - 2026