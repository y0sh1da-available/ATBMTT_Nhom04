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

def xor(bits1, bits2):
    return [b1 ^ b2 for b1, b2 in zip(bits1, bits2)]

# Bảng hoán vị PC1
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

# Lịch dịch trái cho 16 vòng
SHIFT_SCHEDULE = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

# Bảng hoán vị PC2
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

# Bảng hoán vị IP (Initial Permutation)
IP = [
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7
]

# Bảng mở rộng E (Expansion)
E = [
    32, 1, 2, 3, 4, 5,
    4, 5, 6, 7, 8, 9,
    8, 9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32, 1
]

# 8 bảng S-box
S_BOXES = {
    1: [
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
    ],
    2: [
        [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
    ],
    3: [
        [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
    ],
    4: [
        [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
    ],
    5: [
        [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
    ],
    6: [
        [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
    ],
    7: [
        [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
    ],
    8: [
        [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
    ]
}

# Bảng hoán vị P (Permutation) cho hàm f
P = [
    16, 7, 20, 21,
    29, 12, 28, 17,
    1, 15, 23, 26,
    5, 18, 31, 10,
    2, 8, 24, 14,
    32, 27, 3, 9,
    19, 13, 30, 6,
    22, 11, 4, 25
]

# Bảng hoán vị cuối cùng IP^-1 (inverse IP)
IP_INV = [
    40, 8, 48, 16, 56, 24, 64, 32,
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9, 49, 17, 57, 25
]

#Sinh khóa DES
def generate_keys(key_hex):
    # Chuyển khóa từ hex sang danh sách bit 64 bit
    key_bits = str_to_bitlist(key_hex)
    # Thực hiện hoán vị PC1 (64->56 bit)
    key_pc1 = permutate(key_bits, PC1)
    C = key_pc1[:28]
    D = key_pc1[28:]

    round_keys = []
    for i in range(16):
        shift = SHIFT_SCHEDULE[i]
        C = left_shift(C, shift)
        D = left_shift(D, shift)
        combined = C + D
        Ki = permutate(combined, PC2)  # mỗi khóa Ki 48 bit
        round_keys.append(Ki)
    return round_keys

#Hàm f của DES
def f_function(R, K):
    ER = permutate(R, E)  # Mở rộng từ 32 -> 48 bit theo bảng E
    x = xor(ER, K)
    output = []
    for i in range(8):
        block = x[i * 6:(i + 1) * 6]
        row = block[0] * 2 + block[5]  # hàng: bit đầu và cuối
        col = block[1] * 8 + block[2] * 4 + block[3] * 2 + block[4]  # cột: 4 bit giữa
        s_val = S_BOXES[i + 1][row][col]
        s_bits = [int(b) for b in bin(s_val)[2:].zfill(4)]
        output.extend(s_bits)
    # Hoán vị P (32 -> 32 bit)
    F = permutate(output, P)
    return F

#Main DES encryption
if __name__ == "__main__":
    try:
        with open("input911.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()
        M_hex = lines[0].split("=")[1].strip()
        key_hex = lines[1].split("=")[1].strip()
        F_hex_input = lines[2].split("=")[1].strip()
    except Exception as e:
        print("Lỗi khi đọc file input911.txt:", e)
        exit(1)

    # Sinh 16 khóa con từ khóa K
    round_keys = generate_keys(key_hex)

    # Bước 4: Hoán vị IP ban đầu trên bản tin M
    M_bits = str_to_bitlist(M_hex)
    M_IP = permutate(M_bits, IP)
    L = []  # danh sách L0, L1, ..., L16
    R = []  # danh sách R0, R1, ..., R16
    L0 = M_IP[:32]
    R0 = M_IP[32:]
    L.append(L0)
    R.append(R0)
    print("Hoán vị IP")
    print("Input: M =", M_hex)
    print("Output: L0 =", bitlist_to_str(L0))
    print("        R0 =", bitlist_to_str(R0))
    print("=" * 50)

    # Vòng lặp thứ nhất (i = 1)
    # Ở vòng 1: thay vì tính f(R0, K1) ta dùng giá trị F đọc từ file
    F1 = str_to_bitlist(F_hex_input)
    L1 = R0[:]  # L1 = R0
    R1 = xor(L0, F1)
    L.append(L1)
    R.append(R1)
    print("Câu 9:")
    print("Vòng 1:")
    print("Input: L0 =", bitlist_to_str(L0), "; R0 =", bitlist_to_str(R0))
    print("       F (đọc từ file) =", bitlist_to_str(F1))
    print("Output: L1 = R0 =", bitlist_to_str(L1))
    print("        R1 = L0 ⊕ F =", bitlist_to_str(R1))
    print("=" * 50)

    print("Câu 10: ")
    # Vòng lặp từ 2 đến 16:
    for i in range(2, 17):
        # Tính f(R(i-1), Ki)
        Fi = f_function(R[i - 1], round_keys[i - 1])
        Li = R[i - 1][:]  # L(i) = R(i-1)
        Ri = xor(L[i - 1], Fi)  # R(i) = L(i-1) ⊕ f(R(i-1), Ki)
        L.append(Li)
        R.append(Ri)
        print("Vòng {}:".format(i))
        print("Input: L{} = {}".format(i - 1, bitlist_to_str(L[i - 1])),
              "; R{} = {}".format(i - 1, bitlist_to_str(R[i - 1])))
        print("       f(R{}, K{}) = {}".format(i - 1, i, bitlist_to_str(Fi)))
        print("Output: L{} = R{} = {}".format(i, i - 1, bitlist_to_str(Li)))
        print("        R{} = L{} ⊕ f(R{}, K{}) = {}".format(i, i - 1, i - 1, i, bitlist_to_str(Ri)))
        print("=" * 50)

    # Sau vòng lặp thứ 16:
    # Theo DES, sau 16 vòng thực hiện swap 2 nửa, tức preoutput = R16 || L16
    preoutput = R[16] + L[16]
    print("Preoutput (sau 16 vòng, sau hoán vị swap):", bitlist_to_str(preoutput))

    # Bước 11: Thực hiện hoán vị cuối cùng IP⁻¹ để thu được bản mã C
    ciphertext_bits = permutate(preoutput, IP_INV)
    ciphertext = bitlist_to_str(ciphertext_bits)
    print("Câu 11: Hoán vị cuối cùng IP⁻¹")
    print("Input: preoutput =", bitlist_to_str(preoutput))
    print("Output: C (bản mã cần tìm) =", ciphertext)
    print("============ KẾT QUẢ MÃ HÓA ============")
