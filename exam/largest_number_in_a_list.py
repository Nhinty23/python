# Tìm ra số lớn nhất trong một danh sách ngẫu nhiên
import random

def generate_random_numbers(n=10, start=0, stop=100):
    return [random.randint(start, stop) for _ in range(n)]

def find_largest(numbers: list[int]):
    if len(numbers) < 1:
        print("Vui lòng cung cấp danh sách hợp lệ")
        return None

    max_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number

# Lấy ra 5 số bất kỳ trong khoảng từ 50 đến 70 rồi in ra số lớn nhất
numbers_list = generate_random_numbers(5, 50, 70)
print(f"Danh sách bao gồm các số sau: \n {numbers_list}", "\n")
largest_number = find_largest(numbers_list)
if largest_number is not None:
    print(f"Số lớn nhất trong danh sách là {largest_number}")

# Nguyễn Thị Yến Nhi - 2026