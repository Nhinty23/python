# EXCEPTION HANDLING
# Exception error: Lỗi xảy ra khi chương trình thực hiện
# một phép tính toán hoặc thao tác không hợp lệ:
# Ví dụ: chia một số cho số 0, chuyển đổi một chuỗi sang một

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

divide1()

# Nguyễn Thị Yến Nhi - 2026