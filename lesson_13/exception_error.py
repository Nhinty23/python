# EXCEPTION HANDLING
# Exception error: Lỗi xảy ra khi chương trình thực hiện
# một phép tính toán hoặc thao tác không hợp lệ:
# Ví dụ: chia một số cho số 0, chuyển đổi một chuỗi sang một
import datetime


# Không bắt exception
# input_number = int(input("Enter a number: "))
# result = input_number / 0 # Lỗi nhe
# print(result, "\n")

# Bắt exception
def divide():
    try:
        a = int(input("Enter a: "))
        b = int(input("Enter b: "))
        result = a / b # Thử nhập b = 0 xem có bắt lỗi không nhé
    except:
        print("Invalid input")
    else:
        print(f"Kết quả của {a} chia {b} là {result}", "\n")
        print("Success")

# divide()

###############################################################
# Xử lý Exception error:
# 1. try  2. except 3. else 4. finally

# ValueError, ZeroDivisionError, TypeError,...

# Bài toán nhập 2 chữ số a và b, thực hiện phép chia: a/b và in ra kết quả

def divide1():
    while True:
        try:
            a = int(input("Enter a: "))
            b = int(input("Enter b: "))
            result = a / b # Thử nhập b = 0 xem có bắt lỗi không nhé
        except ValueError:
            print("Please enter valid numbers")
            continue # Nhập lại
        except ZeroDivisionError:
            print("b must be not zero")
            continue # Nhập lại
        else:
            print(f"Kết quả của {a} chia {b} là {result:.2f}")
            print("Success")
            break # Kết thúc
        finally:
            print("The end \n") # Hợp lệ hay không hợp lệ đều chạy vào đây

# divide1()

# Tạo exception với từ khóa "raise"
# Nhập năm sinh để tính tuổi
# Có thể viết là datetime.today().year nếu sửa thành from datetime import datetime thay vì là import datetime như hiện tại

def calculate_age():
    while True:
        try:
            year_of_birth = int(input("Enter year of birth: "))
            current_year = datetime.datetime.today().year # Lấy năm hiện tại

            if year_of_birth <= 0:
                print("Năm sinh phải > 0\n")
                continue

            if year_of_birth > current_year:
                print("Năm sinh không hợp lệ (ở tương lai)\n")
                continue

            age = current_year - year_of_birth

        except ValueError:
            print("Vui lòng nhập số nguyên hợp lệ\n")
            continue
        else:
            print(f"Tuổi của bạn là {age} tuổi")
            break

# calculate_age()

# Tính chu vi , diện tích hình chữ nhật
def calculate_rectangle():
    while True:
        try:
            length = float(input("Nhập chiều dài: "))
            width = float(input("Nhập chiều rộng: "))

            if length <= 0 or width <= 0:
                print("Kích thước phải lớn hơn 0")
                continue

            if width >= length:
                print("Chiều rộng phải nhỏ hơn chiều dài")
                continue

            perimeter = (length + width) * 2
            area = length * width

        except ValueError:
            print("Vui lòng nhập số hợp lệ")
            continue
        else:
            print(f"Chu vi: {perimeter:.2f}")
            print(f"Diện tích: {area:.2f}")
            break
        finally:
            print("Hoàn thành\n")

calculate_rectangle()

# Nguyễn Thị Yến Nhi - 2026