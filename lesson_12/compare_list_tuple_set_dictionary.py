# SO SÁNH LIST, TUPLE, SET, DICTIONARY

# 1. CÁCH TẠO
# List: []
fruits_list = ["apple", "banana", "cherry"]
print(fruits_list, "\n")
print(type(fruits_list), "\n")

# Tuple: () - Chú ý tuple có môt phần tử thì sau phần tử đấy phải có dấu phẩy
fruits_tuple = ("apple", "banana", "cherry")
print(fruits_tuple, "\n")
print(type(fruits_tuple), "\n")

# Set: {}
# Nếu có phần tử trùng lặp -> Lấy 1 phần tử trùng lăp đại diện
fruits_set = {"apple", "grape","banana", "cherry", "grape"}
print(fruits_set, "\n")
print(type(fruits_set), "\n")

# Dictionary: {} - Mỗi phần tử là một cặp key : value
# Nếu trùng thì chỉ giữ lại cặp key : value cuối (thêm sau)
fruits_dictionary = {
    "apple" : "Táo",
    "banana" : "Chuối",
    "grape" : "Nho",
    "grape" : "Nhi"
}
print(fruits_dictionary, "\n")
print(type(fruits_dictionary), "\n")

###############################################################################
# 2. CÁC PHẦN TỬ CÓ THỨ TỰ HAY KHÔNG? - (ORDER)
def collection_order():
    # Yes: List, Tuple,  Dictionary (với Python ver 3.7+ )
    print(fruits_list, "\n")
    print(fruits_list[0], "\n")

    print(fruits_tuple, "\n")
    print(fruits_tuple[1], "\n")

    print(fruits_dictionary, "\n")
    print(list(fruits_dictionary.keys())[1], "\n") # Ép kiểu thành list rồi gọi nó ra theo index
    print(list(fruits_dictionary.values())[1], "\n")
    print(fruits_dictionary["grape"], "\n")

    # No: Set, Dictionary (với Python ver thấp hơn 3.7)
    print(fruits_set, "\n")
    #print(fruits_set[0]) #Lỗi

# collection_order()

###############################################################################
# 3. THAY ĐỔI ĐƯỢC KHÔNG? - (MUTABLE)
def collection_mutable():
    # Yes: List, Set, Dictionary
    print(fruits_list, "\n")
    fruits_list.append("Nhi")
    print(fruits_list, "\n")

    print(fruits_set, "\n")
    fruits_set.add("Nhi")
    print(fruits_set, "\n")

    print(fruits_dictionary, "\n")
    fruits_dictionary["name"] = "Nguyễn Thị Yến Nhi"
    print(fruits_dictionary, "\n")

    # No: Tuple
    print(fruits_tuple, "\n")
    # fruits_tuple.add("Nhi") # Lỗi

# collection_mutable()

###############################################################################
# 4. CHỨA PHẦN TỬ TRÙNG LẶP? - (DUPLICATE)
def collection_duplicate():
    # Yes: List, Tuple
    colors_list = ["red", "green", "blue", "red", "green", "blue", "red", "green", "blue", "red", "green", "blue"]
    print(colors_list, "\n")

    colors_tuple = ["red", "green", "blue", "red", "green", "blue", "red", "green", "blue", "red", "green", "blue"]
    print(colors_tuple, "\n")

    # No: Set
    colors_set = {"red", "green", "blue", "red", "green", "blue", "red", "green", "blue"}
    print(colors_set, "\n")

    # Special: Dictionary (key - No : Value - Yes)
    my_info = {
        "name": "Nguyễn Thị Yến Nhi",
        "nick_name": "Nguyễn Thị Yến Nhi",
        "age": 18,
        "age": 21,
        "duplicate": False
    }
    print(my_info, "\n")

# collection_duplicate()
###############################################################################
# TỔNG KẾT
# COLLECTION   CREATE     MUTABLE   ORDER     DUPLICATE
# list:        []         Yes       Yes       Yes
# tuple:       ()         No        Yes       Yes
# set:         {}         Yes       No        No
# dictionary:  {}         Yes       Yes       No - key, Yes - Value

# Nguyễn Thị Yến Nhi - 2026