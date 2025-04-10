# Hàm tính lũy thừa modulo sử dụng phương pháp bình phương liên tiếp
def mod_exp(a, m, n):
    result = 1
    a = a % n
    while m > 0:
        if m % 2 == 1:
            result = (result * a) % n
        m = m // 2
        a = (a * a) % n
    return result

# Hàm tính nghịch đảo modulo sử dụng Thuật toán Euclid mở rộng
def mod_inverse(a, n):
    t, new_t = 0, 1
    r, new_r = n, a
    while new_r != 0:
        quotient = r // new_r
        t, new_t = new_t, t - quotient * new_t
        r, new_r = new_r, r - quotient * new_r
    if r > 1:
        return None  # Không có nghịch đảo
    if t < 0:
        t = t + n
    return t

# Hàm tính hàm Euler φ(n)
def euler_totient(n):
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n = n // p
            result -= result // p
        p += 1
    if n > 1:
        result -= result // n
    return result

# Hàm tính theo định lý Fermat
def fermat_exp(a, m, n):
    if m >= n:
        m = m % (n - 1)  # Định lý Fermat
    return mod_exp(a, m, n)

# Định lý CRT đơn giản
def chinese_remainder_theorem_exp(a, k, n):
    return mod_exp(a, k, n)

# Giải hệ phương trình bằng CRT
def chinese_remainder_theorem_system(m1, m2, m3, a1, a2, a3):
    def extended_gcd(a, b):
        if b == 0:
            return a, 1, 0
        g, x1, y1 = extended_gcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return g, x, y

    def mod_inverse(a, m):
        g, x, _ = extended_gcd(a, m)
        if g != 1:
            return None
        return x % m

    M = m1 * m2 * m3
    M1 = M // m1
    M2 = M // m2
    M3 = M // m3

    inv_M1 = mod_inverse(M1, m1)
    inv_M2 = mod_inverse(M2, m2)
    inv_M3 = mod_inverse(M3, m3)

    if inv_M1 is None or inv_M2 is None or inv_M3 is None:
        return None

    x = (a1 * M1 * inv_M1 + a2 * M2 * inv_M2 + a3 * M3 * inv_M3) % M
    return x

# Kiểm tra căn nguyên thủy
def is_primitive_root(a, n):
    phi_n = euler_totient(n)
    for i in range(1, phi_n):
        if mod_exp(a, i, n) == 1:
            return False
    return True

# Logarithm rời rạc
def discrete_log(a, b, n):
    m = int(n ** 0.5) + 1
    value = {}
    current = 1
    for j in range(m):
        value[current] = j
        current = (current * a) % n
    inv_a_m = mod_inverse(mod_exp(a, m, n), n)
    current = b
    for i in range(m):
        if current in value:
            return i * m + value[current]
        current = (current * inv_a_m) % n
    return None

# Đọc input.txt
with open('input.txt', 'r') as file:
    lines = [list(map(int, line.strip().split())) for line in file.readlines()]

# Gán giá trị từ file
a1, m1, n1 = lines[0]
a2, n2 = lines[1]
a3, m3, n3 = lines[2]
n4 = lines[3][0]
a5, m5, n5 = lines[4]
a6, k6, n6 = lines[5]
m1_crt, m2_crt, m3_crt = lines[6]
a1_crt, a2_crt, a3_crt = lines[7]
a8, n8 = lines[8]
a9, b9, n9 = lines[9]
a, b, x, y, n = lines[10]

# Tính toán
b1 = mod_exp(a1, m1, n1)
x2 = mod_inverse(a2, n2)
b3 = fermat_exp(a3, m3, n3)
phi_n4 = euler_totient(n4)
b5 = mod_exp(a5, m5, n5)
b6 = chinese_remainder_theorem_exp(a6, k6, n6)
x7 = chinese_remainder_theorem_system(m1_crt, m2_crt, m3_crt, a1_crt, a2_crt, a3_crt)
is_primitive = is_primitive_root(a8, n8)
k9 = discrete_log(a9, b9, n9)

A1 = (mod_exp(a, x, n) + mod_exp(b, y, n)) % n
A2 = (mod_exp(a, x, n) - mod_exp(b, y, n)) % n
A3 = (mod_exp(a, x, n) * mod_exp(b, y, n)) % n
A4 = mod_inverse(mod_exp(b, y, n), n)
A5 = (mod_exp(a, x, n) * A4) % n if A4 is not None else None

# In kết quả
print(f"1. b = a^m mod n = {b1}")
print(f"2. x = a^(-1) mod n = {x2}")
print(f"3. b = a^m mod n sử dụng Định lý Fermat = {b3}")
print(f"4. φ(n) = {phi_n4}")
print(f"5. b = a^m mod n sử dụng Định lý Euler = {b5}")
print(f"6. b = a^k mod n sử dụng Định lý Số dư Trung Hoa = {b6}")
print(f"7. Giải hệ phương trình modulo = {x7}")
print(f"8. Kiểm tra căn nguyên thủy của {a8} đối với {n8}: {is_primitive}")
print(f"9. k = logarithm rời rạc = {k9}")
print(f"10. A1 = {A1}, A2 = {A2}, A3 = {A3}, A4 = {A4}, A5 = {A5}")
