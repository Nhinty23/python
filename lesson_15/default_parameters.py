# DEFAULT PARAMETERS - Các tham số mặc định
# 1. Default parameters là gì?
# - Là các giá trị mặc định được gán cho các parameters
# - Khi gọi hàm và không truyền giá trị cho các parameters đó
# thì giá trị mặc định sẽ được dùng
# => Làm cho code ngắn gọn hơn, khi gọi hàm thì có thể bỏ qua
# không cần truyền vào default parameter

# Hàm in ra lời chào
def say_hello(name, greeting = "Welcome"):
    print(f"{greeting} {name}!")

# say_hello("Nhi") # Hiện "Welcome Nhi!"

# 2. Khi nào thì nên dùng default parameters?
# Hàm thường có nhiều parameters, parameter nào nên có giá trị mặc định?

# Truyền tham số
def calculate_final_price(price, discount_percent=None, discount_amount=None):
    if price <= 0:
        raise ValueError("Price phải > 0")

    # Phải có ít nhất 1 loại giảm
    if discount_percent is None and discount_amount is None:
        raise ValueError("Phải nhập ít nhất discount_percent hoặc discount_amount")

    total_discount = 0

    # Tính % nếu có
    if discount_percent is not None:
        percent_discount = price * (discount_percent / 100)
        total_discount += percent_discount
    else:
        percent_discount = 0

    # Tính tiền nếu có
    if discount_amount is not None:
        total_discount += discount_amount
    else:
        discount_amount = 0

    # Không cho giảm quá giá
    total_discount = min(total_discount, price)

    final_price = price - total_discount

    # Hiển thị
    print(f"Giá gốc: {price:,} VND")

    if discount_percent is not None:
        print(f"Giảm theo %: {discount_percent}% → {percent_discount:,} VND")

    if discount_amount:
        print(f"Giảm trực tiếp: {discount_amount:,} VND")

    print(f"Tổng giảm: {total_discount:,} VND")
    print(f"Giá cuối: {final_price:,} VND")

    return final_price

# calculate_final_price(100000, 1, 2000)

# Nhập từ bàn phím
def parse_percent(input_str):
    while True:
        input_str = input_str.strip().replace("%", "")
        try:
            value = float(input_str)
            if value < 0 or value > 100:
                raise ValueError
            return value
        except:
            print("Phần trăm phải từ 0 đến 100, vui lòng nhập lại")
            input_str = input("Nhập lại % giảm: ")


def parse_money(input_str, price):
    while True:
        input_str = input_str.strip().replace(",", "")
        try:
            value = float(input_str)
            if value < 0 or value > price:
                raise ValueError
            return value
        except:
            print(f"Số tiền phải từ 0 đến {int(price):,} VND")
            input_str = input("Nhập lại số tiền giảm: ")


def format_vnd(x):
    return f"{int(x):,} VND"


def calculate_final_price_input():
    # Nhập giá
    while True:
        try:
            price = float(input("Nhập giá sản phẩm: ").replace(",", ""))
            if price <= 0:
                raise ValueError
            break
        except:
            print("Giá không hợp lệ, vui lòng nhập lại")

    # ===== Nhập giảm giá có kiểm tra =====
    while True:
        # Nhập %
        percent_input = input("Nhập phần trăm giảm (Enter để bỏ qua): ")
        discount_percent = parse_percent(percent_input) if percent_input else None

        # Nhập tiền
        amount_input = input("Nhập số tiền giảm (Enter để bỏ qua): ")
        discount_amount = parse_money(amount_input, price) if amount_input else None

        # Tính thử tổng giảm
        percent_discount = price * (discount_percent / 100) if discount_percent else 0
        amount_discount = discount_amount if discount_amount else 0

        total_discount = percent_discount + amount_discount

        # Kiểm tra tổng giảm
        if total_discount > price:
            print("Tổng giảm vượt quá giá sản phẩm, vui lòng nhập lại\n")
            continue

        break

    final_price = price - total_discount

    # ===== HIỂN THỊ =====
    print("\n" + "="*40)
    print("        KẾT QUẢ TÍNH TOÁN")
    print("="*40)

    print(f"{'Giá gốc:':25}{format_vnd(price):>15}")

    if discount_percent is not None:
        print(f"{'Giảm (%):':25}{discount_percent}%")
        print(f"{'Tiền giảm (%):':25}{format_vnd(percent_discount):>15}")

    if discount_amount:
        print(f"{'Giảm trực tiếp:':25}{format_vnd(discount_amount):>15}")

    if total_discount == 0:
        print(f"{'Giảm giá:':25}{'0 VND':>15}")

    print("-"*40)
    print(f"{'Tổng giảm:':25}{format_vnd(total_discount):>15}")
    print(f"{'Giá cuối:':25}{format_vnd(final_price):>15}")
    print("="*40)

while True:
    calculate_final_price()

    tiep = input("\nBạn có muốn tính tiếp không? (Y/N): ").strip().lower()
    if tiep != "Y":
        print("Kết thúc chương trình")
        break

calculate_final_price_input()

# Nguyễn Thị Yến Nhi - 2026