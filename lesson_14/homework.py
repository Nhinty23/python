# BT1:
# Nhập vào một số nguyên n, xác định n là số chẵn hay số lẻ
# Chẵn in ra "{n} là số chẵn" ngược lại in ra "{n} là số lẻ"
# Ví dụ 1:
# Input: n = 10
# Output: 10 là số chẵn

# Ví dụ 2:
# Input: n = 15
# Output: 15 là số lẻ

while True:
    try:
        a = int(input("Mời bạn nhập số nguyên dương bất kỳ: "))
        if a <= 0:
            print("Vui lòng nhập số nguyên dương (> 0)\n")
            continue
    except ValueError:
        print("Dữ liệu đầu vào không hợp lệ (phải là số nguyên)\n")
        continue
    else:
        if a % 2 == 0:
            print(f"{a} là số chẵn")
        else:
            print(f"{a} là số lẻ")
        break

# Nguyễn Thị Yến Nhi - 2026