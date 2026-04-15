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

# 4. Một số thao tác với dictionary
def dict_part_4():
    pass
    # 4.1. Lấy số lượng phần tử (số cặp key-value)
    name_part_4 = {"name": "Nhi", "age": 21, "grade": 9}
    print(len(name_part_4), "\n")

    # 4.2. Lấy value theo key
    # Cách 1: dùng dấu ngoặc vuông []
    print(name_part_4["name"], "\n")

    # Nếu key không tồn tại sẽ gây lỗi
    # print(name_part_4["hobby"], "\n")

    # Cách 2: dùng hàm get()
    print(name_part_4.get("grade"), "\n")

    # Nếu key không tồn tại (không gây ra lỗi) sẽ trả về None hoặc giá trị mặc định
    print(name_part_4.get("this_song"), "\n") # Trả về None
    print(name_part_4.get("this_song", "Nhi"), "\n") # Trả về Nhi

    # 4.3. Kiểm tra key có trong dict không?
    if "happy" in name_part_4:
        print("Có happy")
    elif "sad" not in name_part_4:
        print("Không hề sad")
    else:
        print("Không có rì hết")

    # 4.4. Thêm/thay đổi phần tử
    print(name_part_4, "\n")
    name_part_4["song"] = "run"
    print(name_part_4, "\n")

    # 4.5. Xóa phần tử
    del name_part_4["song"]
    print(name_part_4, "\n")

    # 4.6. Xóa và lấy giá trị bị xóa
    name_deleted = name_part_4.pop("age")
    print(name_deleted, "\n")
    print(name_part_4, "\n")

    # 4.7. Xóa toàn bộ dictionary
    clear_all = name_part_4.clear()
    print(clear_all, "\n")
    print(name_part_4, "\n")

    # 4.8. Lấy tất cả key
    get_all_colors_key = colors.keys()
    print(get_all_colors_key, "\n")

    # 4.9. Lấy tất cả values
    get_all_colors_values = colors.values()
    print(get_all_colors_values, "\n")

    # 4.10. Lấy tất cả các items (các cặp key-value)
    get_all_keys_values = colors.items()
    print(get_all_keys_values, "\n")

    # 4.11. Copy dictionary
    print(colors, "\n")
    copy_colors = colors.copy()
    print(copy_colors, "\n")

dict_part_4()

# ---------------------------------------------------------------------------
# 5. Duyệt dictionary
def dict_part_5():
    pass
    yen_nhi = {"name": "Nguyễn Thị Yến Nhi", "age": 21, "grade": 9}
    # 5.1. Duyệt qua các key
    for key in yen_nhi.keys():
        print(key, "\n")

    # 5.2. Duyệt qua các value
    for value in yen_nhi.values():
        print(value, "\n")

    # 5.3. Duyệt qua các item (cả key và value)
    for key, value in yen_nhi.items():
        print(f"{key} -> {value}", "\n")

dict_part_5()

# Nguyễn Thị Yến Nhi - 2026