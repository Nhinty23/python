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

# 3. Cách tạo dictionary
def my_dictionary():
    # Tạo dictionary bằng cặp ngoặc nhọn {}
    print("My dictionary------------------------------------------", "\n")
    student = {"name": "Nguyễn Thị Yến Nhi", "age": 21, "grade": 9}
    print(student, "\n")
    print(type(student), "\n")

    # Tạo dictionary bằng hàm dict()
    # key phải là các biến hợp lệ (bắt đầu chữ cái hoặc gạch dưới,
    # không được bắt đầu bằng số, không phải là keyword - class, for,...
    # không chứa khoảng trắng ...
    print("My scores----------------------------------------------", "\n")
    scores = dict(math=10, enlish=9, history=8)
    print(scores, "\n")
    print(type(scores), "\n")

    # Dictionary có thể lồng nhau
    my_students = {
        "nhi": {"name": "Nhi", "age": 21, "grade": 9},
        "huệ": {"name": "Huệ", "age": 13, "grade": 9.5},
        "dương": {"name": "Dương", "age": 21, "grade": 8}
    }
    print(my_students, "\n")
    print(type(my_students), "\n")

    # In ra mỗi Nhi thôi
    print(my_students["nhi"], "\n")

my_dictionary()

# Nguyễn Thị Yến Nhi - 2026