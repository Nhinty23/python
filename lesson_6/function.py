# Cơ bản về hàm (function)

# 1. Hàm
# - Tập hợp các dòng code thực hiện một công việc cụ thể
# - Mỗi hàm có một tên riêng, chỉ chạy khi được gọi
# - Có thể được gọi 1 hoặc nhiều lần

# 2. Cú pháp
'''
def ten_ham(tham_so_1, tham_so_2,...)
    code
    code
    code
    return gia_tri
'''

# 3. Bài tập về hàm
# Viết hàm tính tổng 2 số, in ra kết quả
# - Có 2 tham số a và b
# - Có giá trị trả về dùng return
# - Code trong hàm chỉ chạy khi hàm được gọi

def sum(a , b):
    c = a + b
    return c

c = sum(8,2)

print(f"Tổng của 2 số là {c}")

# Nguyễn Thị Yến Nhi - 2026