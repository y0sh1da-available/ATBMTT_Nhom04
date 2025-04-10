def str_to_bitlist(s):
    scale = 16
    num_of_bits = len(s) * 4
    bin_str = bin(int(s, scale))[2:].zfill(num_of_bits)
    return [int(b) for b in bin_str]

def bitlist_to_str(b_list):
    return ''.join(str(bit) for bit in b_list)

def permutate(bits, table):
    return [bits[i - 1] for i in table]

def left_shift(bits, n):
    return bits[n:] + bits[:n]

# Bảng PC1 (64 -> 56 bit)
PC1 = [
    57, 49, 41, 33, 25, 17, 9,
    1, 58, 50, 42, 34, 26, 18,
    10, 2, 59, 51, 43, 35, 27,
    19, 11, 3, 60, 52, 44, 36,
    63, 55, 47, 39, 31, 23, 15,
    7, 62, 54, 46, 38, 30, 22,
    14, 6, 61, 53, 45, 37, 29,
    21, 13, 5, 28, 20, 12, 4
]

# dịch trái cho 16 vòng
SHIFT_SCHEDULE = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

# Bảng PC2 (56 -> 48 bit)
PC2 = [
    14, 17, 11, 24, 1, 5,
    3, 28, 15, 6, 21, 10,
    23, 19, 12, 4, 26, 8,
    16, 7, 27, 20, 13, 2,
    41, 52, 31, 37, 47, 55,
    30, 40, 51, 45, 33, 48,
    44, 49, 39, 56, 34, 53,
    46, 42, 50, 36, 29, 32
]

def generate_keys(key_hex):
# Chuyển khóa từ hex sang danh sách bit 64 bit
    key_bits = str_to_bitlist(key_hex)

# Hoán vị PC1 cho khóa K
    key_pc1 = permutate(key_bits, PC1)  # kết quả 56 bit
    C0 = key_pc1[:28]
    D0 = key_pc1[28:]
    print("Câu 1: Hoán vị PC1")
    print("Input: K =", key_hex)
    print("Output: C0 =", bitlist_to_str(C0))
    print("        D0 =", bitlist_to_str(D0))
    print("-" * 50)

    round_keys = []
    Ci = C0.copy()
    Di = D0.copy()

    print("Câu 2:Các giá trị dịch vòng")
    print("Input: C0 =  ", bitlist_to_str(C0)," ;D0 = ", bitlist_to_str(D0))
    for i in range(16):
    # Dịch vòng
        shift = SHIFT_SCHEDULE[i]
        Ci = left_shift(Ci, shift)
        Di = left_shift(Di, shift)
        print("Vòng", i + 1)
        print("Output: C{} =".format(i + 1), bitlist_to_str(Ci))
        print("        D{} =".format(i + 1), bitlist_to_str(Di))

    # Tạo khóa Ki cho vòng i+1
        combined = Ci + Di
        Ki = permutate(combined, PC2)
        round_keys.append(Ki)

    return round_keys

def main():
    # Đọc khóa DES từ file input.txt
    try:
        with open("input13.txt", "r", encoding="utf-8") as file:
            key_hex = file.readline().strip()
        if not key_hex:
            raise ValueError("File input trống hoặc không chứa khóa hợp lệ.")
    except Exception as e:
        print("Lỗi khi đọc file:", e)
        return

    keys = generate_keys(key_hex)

    print("-" * 50)
    print("\nCâu 3:Khoá Ki")
    print("Danh sách khóa Ki cho 16 vòng:")
    for idx, k in enumerate(keys):
        print("K{}: {}".format(idx + 1, bitlist_to_str(k)))

if __name__ == "__main__":
    main()
