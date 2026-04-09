# Vòng lặp trong python

# 1. Vòng lặp for với hàm range()
# Ví dụ 1: for & range(stop)
# Dùng hàm range chỉ có đối số stop
# for number in range(10):
#     print(number)
# print("Done")

# Ví dụ 2: for & range(start,stop)
# Dùng hàm range có 2 đối số là start và stop
# In ra dãy số từ 5 đến 10
# for number in range(5,11):
#     print(number)
# print("Done")

# Ví dụ 3: for & range(start, stop, step)
# Dùng hàm range có 3 đối số: start, stop, step
# In ra một dãy số chẵn từ 0 đến 10
# for number in range(0,11,2):
#     print(number)
# print("Done")

# Ví dụ 44: Tính tổng các số từ 1 đến 10
sum = 0
for number in range(1,11):
    sum += number # sum = sum + number
print(f"Tổng của các số là {sum}")