# 1. Check data type of value using type() function
print("1. Kiểu dữ liệu")
print(f"Kiểu dữ liệu của số 10 là {type(10)} ")
print(f"Kiểu dữ liệu của số 2.0 là {type(2.0)} ")
print(f"Kiểu dữ liệu của chữ \"Hello Nhi\" là {type("Hello Nhi")} ")
print(f"Kiểu dữ liệu của True là {type(True)} ")

int_num = 10
print(type(int_num))

print("2. Ép kiểu")
# Dữ liệu dạng str
str_num = '100'
print(type(str_num))

# Ép kiểu từ str sang int
int_num = int(str_num)
print(type(int_num))

# Ép kiểu từ int sang float
float_num = float(int_num)
print(type(float_num))

print("\nChú ý: Không ép kiểu từ dạng  chữ sang kiểu dữ liệu khác nhé !!!")

# Nguyễn Thị Yến Nhi - 2026