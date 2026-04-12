# 1. Tuple là gì?
# - Tuple là một cấu trúc dữ liệu trong python dùng để lưu trữ nhiều giá trị trong
# một biến duy nhất, tương tự như list. Tuy nhiên, khác với list, một tuple sau khi
# được tạo ra thì sẽ không thể thay đổi được (immutable), tức là không thể thêm,
# xóa, sửa các giá trị bên trong của tuple
week_days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print(week_days, "\n")
print(type(week_days), "\n")

###################################################################################
# 2. Các tính chất của tuple
# - Bất biến / Không thể thay đổi được (immutable)
# List - mutable
list_mutable = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list_mutable, "\n")
list_mutable.append(10)
print(list_mutable, "\n")
list_mutable[0] = 10
print(list_mutable, "\n")

# Tuple - immutable
tuple_immutable = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(tuple_immutable, "\n")
# tuple_immutable[0] = 10
#print(tuple_immutable, "\n") # In lỗi do tuple không được phép thay đổi

# - Có thứ tự: các phần tử được sắp xếp theo thứ tự
fruits = ("apple", "banana", "cherry")
print(fruits[0], "\n")
print(fruits[2], "\n")
print(fruits[-1], "\n")

# - Chứa được nhiều kiểu dữ liệu khác nhau
student = ("Nhi", 21, 9.9)
print(student, "\n")

# - Có thể chứa các dữ liệu trùng nhau
duplicate_info = ("Nhi", "Nhi", 22, 12)
print(duplicate_info, "\n")

###################################################################################
# 3. Một số cách tạo tuple
# - Tạo tuple bằng dấu ngoặc tròn
my_name = ("Nguyễn", "Thị", "Yến", "Nhi")
print(my_name, "\n")

# - Tạo tuple không cần ngoặc tròn
countries = "Vietnam", "Japan", "Korea"
print(countries, "\n")

# - Tạo tuple rỗng
empty_tuple = ()
print(empty_tuple, "\n")
another_empty_tuple = tuple()
print(another_empty_tuple, "\n")

# - Tạo tuple từ list
new_tuple_list = tuple(list_mutable)
print(new_tuple_list, "\n")

# - Tạo tuple từ chuỗi (str)
text = "Python"
char_tuple = tuple(text)
print(char_tuple, "\n")

# - Chú ý khi tạo tuple có một phần tử
# Không phải tuple
single_number = (5)
print(single_number, "\n")
print(type(single_number), "\n") #In ra kiểu int

# Là tuple
single_number_tuple = (5,)
print(single_number_tuple, "\n")
print(type(single_number_tuple), "\n")

###################################################################################
# 4. Các thao tác cơ bản với tuple: len, slicing, in,...
def tuple_operation():
    # 4.1. Lấy chiều dài của tuple: len() - length
    colors = ("red", "green", "blue", "yellow", "white")
    print(f"Có tổng số {len(colors)} màu sắc", "\n")

    # 4.2. Truy cập một phần tử ở vị trí i
    print(colors[1], "\n")

    # 4.3. Slicing (cắt một phần tuple)
    # clolors[start:stop:step]
    print(colors[::], "\n") # <=> colors[0:5:1] => all phần tử trong tuple
    print(colors[1:3], "\n") # <=> colors[1:3:1]
    print(colors[:3:], "\n") # <=> colors[0:3:1]
    print(colors[::2], "\n") # <=> colors[0:5:2]

    # 4.4. Kiểm tra 1 phần tử có nằm trong tuple không?
    if "green" in colors:
        print("Yes", "\n")
    else:
        print("No", "\n")

    # 4.5. Nối tuple
    tuple_1 = (1, 2, 3)
    tuple_2 = (4, 5, 6)
    mix_tuple = tuple_1 + tuple_2
    print(mix_tuple, "\n")

    # 4.6. Lặp lại các phần tử trong tuple
    repeated = tuple_1 * 3
    print(repeated, "\n")

# tuple_operation()

###################################################################################
# 5. Các phương thức (function, method) của Tuple: index, count
def tuple_method():
    # count()
    numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 2, 2, 2, 2)
    print(f"Có tổng {numbers.count(2)} số 2", "\n")
    print(f"Có tổng {numbers.count(3)} số 3", "\n")

    # index()
    print(f"Số 2 xuất hiện lần đầu ở vị trí số {numbers.index(2)}", "\n")
    print(f"Số 3 xuất hiện lần đầu ở vị trí số {numbers.index(3)}", "\n")
    print(f"Số 2 xuất hiện lần đầu tính từ vị trí 2 đổ đi nằm ở vị trí số {numbers.index(2,2)}", "\n")

# tuple_method()

###################################################################################
# 6. Các phần tử trong tuple
# 6.1. Duyệt dùng for & in
def loop_through_tuple():
    numbers = ("Nguyễn", "Thị", "Yến", "Nhi")
    for item in numbers:
        print(item, "\n")

    # for item in range()
    for index in range(len(numbers)):
        print(numbers[index], "\n")

loop_through_tuple()

# Nguyễn Thị Yến Nhi - 2026