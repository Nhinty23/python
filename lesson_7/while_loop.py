# Vòng lặp while
# Điều kiện = True => Lặp lại, chạy mãi
# Điều kiện = False => Kết thúc vòng lặp

# Ví dụ 1: while True, while False

# Đừng chạy cái này nếu bạn không muốn bị lặp vô hạn
# while True:
#     print("Mình là Nhi nè")
# print("Done")

# Ví dụ 2: Yêu cầu nhập tuổi. Nhỏ hơn 0 -> Nhập . Nhỏ hơn 8 -> Nhập lại. Lớn hơn 8 -> In ra tuổi người dùng nhập vào
# age = 10
# while age < 0:
#     age = int(input(f"Mời bạn nhập tuổi: "))
# print(f"Tuổi của bạn là {age} tuổi")

# Ví dụ 3: Nhập điểm từ 0 đến 10
# Nếu điểm không hợp lệ yêu cầu nhập lại cho đến khi hợp lệ
# Nếu điểm hợp lệ:
# - Nhỏ hơn 5 => Không đạt
# - Từ 5 trở lên => Đạt

# Cách 1:
score = float(input(f"Mời bạn nhập số điểm: "))
while score < 5 or score > 5:
    if score < 5:
        print(f"Số điểm của bạn là {score}")
        print("Không đạt\n")
        score = int(input(f"Mời bạn nhập lại số điểm: "))
    elif 5 < score <= 10:
        print(f"Số điểm của bạn là {score}")
        print("Đạt")
        break
    else:
        print(f"Số điểm của bạn là {score}")
        print("Không hợp lệ\n")
        score = int(input(f"Mời bạn nhập lại số điểm: "))

# Cách 2:
# score = float(input(f"Mời bạn nhập số điểm: "))
#
# while score < 5:
#     print(f"Số điểm của bạn là {score} \n")
#     score = int(input(f"Mời bạn nhập lại số điểm: "))
# print(f"Số điểm của bạn là {score} bạn đã vượt qua kỳ thi")

# Nguyễn Thị Yến Nhi - 2026