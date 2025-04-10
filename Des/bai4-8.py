def str_to_bitlist(s):
    scale = 16
    num_of_bits = len(s) * 4
    bin_str = bin(int(s, scale))[2:].zfill(num_of_bits)
    return [int(b) for b in bin_str]

def bitlist_to_str(b_list):
    return ''.join(str(bit) for bit in b_list)

def permutate(bits, table):
    return [bits[i - 1] for i in table]

def xor(bits1, bits2):
    return [b1 ^ b2 for b1, b2 in zip(bits1, bits2)]

# Bảng IP (Initial Permutation)
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

# Bảng P (Permutation)
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

# 8 bảng S-box
S_BOXES = {
    1: [
        [14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],
        [0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],
        [4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],
        [15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]
    ],
    2: [
        [15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],
        [3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5],
        [0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],
        [13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]
    ],
    3: [
        [10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8],
        [13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1],
        [13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7],
        [1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]
    ],
    4: [
        [7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15],
        [13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9],
        [10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4],
        [3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14]
    ],
    5: [
        [2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9],
        [14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6],
        [4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14],
        [11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]
    ],
    6: [
        [12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11],
        [10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8],
        [9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6],
        [4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]
    ],
    7: [
        [4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1],
        [13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6],
        [1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2],
        [6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]
    ],
    8: [
        [13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7],
        [1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2],
        [7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8],
        [2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]
    ]
}

def s_box_substitution(bits48):
    output = []
    for i in range(8):
        block = bits48[i*6:(i+1)*6]
        row = block[0]*2 + block[5]
        col = block[1]*8 + block[2]*4 + block[3]*2 + block[4]
        s_val = S_BOXES[i+1][row][col]
        s_bits = [int(x) for x in bin(s_val)[2:].zfill(4)]
        output.extend(s_bits)
    return output

if __name__ == "__main__":
    # Đọc dữ liệu từ file input45.txt
    with open("input48.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
    M_hex = lines[0].split("=")[1].strip()
    K1_hex = lines[1].split("=")[1].strip()

    # Câu 4: Hoán vị IP cho bản tin M (64 bit)
    M_bits = str_to_bitlist(M_hex)
    M_IP = permutate(M_bits, IP)
    L0 = M_IP[:32]
    R0 = M_IP[32:]
    print("Câu 4: Hoán vị IP")
    print("Input: M =", M_hex)
    print("Output: L0 =", bitlist_to_str(L0))
    print("        R0 =", bitlist_to_str(R0))
    print("="*30, "CHI TIẾT VÒNG LẶP THỨ NHẤT", "="*30)

    # Câu 5: Hàm mở rộng E cho R0 (32 -> 48 bit)
    ER0 = permutate(R0, E)
    print("-" * 50)
    print("Câu 5: Hàm mở rộng E")
    print("Input: R0 =", bitlist_to_str(R0))
    print("Output: ER0 =", bitlist_to_str(ER0))

    # Câu 6: Thực hiện XOR giữa ER0 và khóa K1 (48 bit)
    K1_bits = str_to_bitlist(K1_hex)
    A = xor(ER0, K1_bits)
    print("-" * 50)
    print("Câu 6: Thực hiện XOR")
    print("Input: ER0 =", bitlist_to_str(ER0))
    print("Output: A  =", bitlist_to_str(A))

    # Câu 7: Phép thế S-box
    B = s_box_substitution(A)
    print("-" * 50)
    print("Câu 7: Phép thế S-box")
    print("Input: A =", bitlist_to_str(A))
    print("Output: B = S(A) =", bitlist_to_str(B))

    # Câu 8: Hoán vị P (32 -> 32 bit)
    F = permutate(B, P)
    print("-" * 50)
    print("Câu 8: Hoán vị P")
    print("Input: B =", bitlist_to_str(B))
    print("Output: F =", bitlist_to_str(F))
