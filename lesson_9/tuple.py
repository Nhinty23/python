# 1. Tuple là gì?
# - Tuple là một cấu trúc dữ liệu trong python dùng để lưu trữ nhiều giá trị trong
# một biến duy nhất, tương tự như list. Tuy nhiên, khác với list, một tuple sau khi
# được tạo ra thì sẽ không thể thay đổi được (immutable), tức là không thể thêm,
# xóa, sửa các giá trị bên trong của tuple
from multiprocessing.reduction import duplicate

from lesson_8.list import students

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
# Nguyễn Thị Yến Nhi - 2026