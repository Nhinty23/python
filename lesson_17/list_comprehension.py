# LIST COMPREHENSION
# 1. List comprehension?
# - Kỹ thuật tạo ra list (danh sách) bằng chỉ một dòng code
# trong đó kết hợp vòng lặp (for) và các điều kiện (nếu cần)

# - List comprehension là cách ngắn gọn để tạo ra một list

# Ví dụ:
numbers = [1, 2, 3, 4, 5]
# number_x2 = [2, 4, 6, 8, 10]
# - Dùng vòng lặp for
# numbers_x2 = []
# for number in numbers:
#     numbers_x2.append((number * 2))
# print(numbers_x2, "\n")

# - Dùng list comprehension
# Syntax:
# new_list = [expression/operation for item in iterable if condition] # if là optional
numbers_x2 = [number * 2 for number in numbers]
print(numbers_x2, "\n")

colors = ["red", "green", "blue", "cyan"]
contain_e = [color for color in colors if color.__contains__("e")] # Tạo ra danh sách mới gồm các phần tử chứa ký tự e
print(contain_e, "\n")
