#MẬT MÃ CAESAR
def caesar_cipher(text, key):
    result = []
    for ch in text:
        if ch.isalpha():
            base = 'A' if ch.isupper() else 'a'
            result.append(chr((ord(ch) - ord(base) + key) % 26 + ord(base)))
        else:
            result.append(ch)
    return ''.join(result)

#MẬT MÃ VIGENERE – LẶP KHÓA
def vigenere_cipher(text, key, auto_key=False):
    text = text.upper()
    key = key.upper()
    result = []
    extended_key = key + text if auto_key else key

    for i in range(len(text)):
        shift = ord(extended_key[i % len(extended_key)]) - ord('A')
        encrypted_char = chr((ord(text[i]) - ord('A') + shift) % 26 + ord('A'))
        result.append(encrypted_char)

    return ''.join(result)

#MẬT MÃ VIGENERE – AUTOKEY
def vigenere_cipher_auto_key(text, key):
    text = text.upper()
    key = key.upper()
    result = []

    # Sử dụng Auto-key: mỗi ký tự trong văn bản được thêm vào khóa sau mỗi bước mã hóa
    for i in range(len(text)):
        shift = ord(key[i % len(key)]) - ord('A')  # Dịch chuyển dựa trên ký tự trong khóa
        encrypted_char = chr((ord(text[i]) - ord('A') + shift) % 26 + ord('A'))
        result.append(encrypted_char)

        # Mở rộng khóa tự động bằng cách lấy ký tự mã hóa và thêm vào khóa
        key += encrypted_char

    return ''.join(result)

#MÃ HÓA CHỮ ĐƠN
def monoalphabetic_cipher(text, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    mapping = {alphabet[i]: key[i] for i in range(26)}
    result = []

    for ch in text:
        result.append(mapping.get(ch, ch))

    return ''.join(result)

#MẬT MÃ MA TRẬN KHÓA PLAYFAIR
def playfair_cipher(text, key):
    key = key.upper().replace("J", "I")
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    key_square = []
    for c in (key + alphabet):
        if c not in key_square:
            key_square.append(c)

    text = text.upper().replace("J", "I")
    formatted_text = text
    encrypted_text = []

    i = 0
    while i < len(formatted_text):
        if i + 1 == len(formatted_text) or formatted_text[i] == formatted_text[i + 1]:
            formatted_text = formatted_text[:i + 1] + 'X' + formatted_text[i + 1:]
        i += 2

    for i in range(0, len(formatted_text), 2):
        a = key_square.index(formatted_text[i])
        b = key_square.index(formatted_text[i + 1])
        rowA, colA = divmod(a, 5)
        rowB, colB = divmod(b, 5)

        if rowA == rowB:
            encrypted_text.append(key_square[rowA * 5 + (colA + 1) % 5])
            encrypted_text.append(key_square[rowB * 5 + (colB + 1) % 5])
        elif colA == colB:
            encrypted_text.append(key_square[((rowA + 1) % 5) * 5 + colA])
            encrypted_text.append(key_square[((rowB + 1) % 5) * 5 + colB])
        else:
            encrypted_text.append(key_square[rowA * 5 + colB])
            encrypted_text.append(key_square[rowB * 5 + colA])

    return ''.join(encrypted_text)

#MẬT MÃ HOÁN VỊ
def transposition_cipher(text, key):
    grid = [['' for _ in range(len(text))] for _ in range(key)]

    row, col = 0, 0
    going_down = True
    for i in range(len(text)):
        grid[row][col] = text[i]
        if going_down:
            row += 1
            col += 1
            if row == key:
                row = key - 2
                going_down = False
        else:
            row -= 1
            col += 1
            if row == -1:
                row = 1
                going_down = True

    result = []
    for i in range(key):
        for j in range(len(text)):
            if grid[i][j]:
                result.append(grid[i][j])

    return ''.join(result)


# Đọc dữ liệu từ input.txt
with open('input.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

# Gán các giá trị từ file
text_1, key_1 = lines[0], int(lines[1])
text_2, key_2 = lines[2], lines[3]
text_4, key_4 = lines[4], lines[5]
text_5, key_5 = lines[6], lines[7]
text_6, key_6 = lines[8], int(lines[9])


# --- (đặt tất cả các hàm mã hóa ở đây) ---

# Thực hiện mã hóa và in kết quả
print("Mã hóa Caesar: ", caesar_cipher(text_1, key_1))
print("Mã hóa Vigenere (Lặp khóa): ", vigenere_cipher(text_2, key_2, auto_key=False))
print("Mã hóa Vigenere (Auto-key): ", vigenere_cipher_auto_key(text_2, key_2))
print("Mã hóa Monoalphabetic: ", monoalphabetic_cipher(text_4, key_4))
print("Mã hóa Playfair: ", playfair_cipher(text_5, key_5))
print("Mã hóa Hoán Vị: ", transposition_cipher(text_6, key_6))
