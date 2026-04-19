# Random module
import random

# 1. Tạo ra số ngẫu nhiên: có thể là số nguyên, số thực
print(f"Số ngẫu nhiên: {random.random()}")
print(f"Số ngẫu nhiên trong khoảng từ 2 => 22: {random.uniform(2, 22)}")
print(f"Số nguyên ngẫu nhiên trong khoảng từ 1 => 10: {random.randint(1, 10)}")
print(f"Số ngẫu nhiên trong range: {random.randrange(1,10,2)}") # [1, 3, 5, 7, 9]

# 2. Lấy một hoặc nhiều giá trị ngẫu nhiên trong một danh sách có sẵn
students = ["Nhi", "Huệ", "Dương", "Mai"]
print(f"Lấy ra 1 học sinh ngẫu nhiên trong danh sách: {random.choice(students)}")
print(f"Lấy ra nhiều học sinh ngẫu nhiên trong danh sách (trùng nhau): {random.choices(students, k=2)}")
print(f"Lấy ra nhiều học sinh ngẫu nhiên trong danh sách (không trùng nhau): {random.sample(students, k=2)}")

# 3. Xáo trộn thứ tự các phần tử trong một danh sách
numbers = list(range(1, 11)) # 1 => 10
random.shuffle(numbers)
print(f"Xáo trộn thứ tự các phần tử trong danh sách: {numbers}")

# Nguyễn Thị Yến Nhi - 2026