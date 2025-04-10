def modinv(a, m):
    """Tính nghịch đảo modulo của a mod m (a^(-1) mod m)"""
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None


def dsa_signature(p, q, h, xA, k, H):
    # Bước 1: Tính g
    g = pow(h, (p - 1) // q, p)

    # Bước 2: Tính khóa công khai yA
    yA = pow(g, xA, p)

    # Bước 3: Tính r
    r = pow(g, k, p) % q

    # Bước 4: Tính s
    k_inv = modinv(k, q)
    s = (k_inv * (H + xA * r)) % q

    return (g, yA, r, s)


def dsa_verify(p, q, g, yA, r, s, H):
    # Bước 1: Kiểm tra r, s hợp lệ
    if not (0 < r < q and 0 < s < q):
        return False

    # Bước 2: Tính w = s^(-1) mod q
    w = modinv(s, q)

    # Bước 3: Tính u1, u2
    u1 = (H * w) % q
    u2 = (r * w) % q

    # Bước 4: Tính v
    v = ((pow(g, u1, p) * pow(yA, u2, p)) % p) % q

    return v == r


# Đọc file input
def read_input(file_path):
    with open(file_path, 'r') as f:
        data = {}
        for line in f:
            if '=' in line:
                key, value = line.strip().split('=')
                data[key.strip()] = int(value.strip())
        return data


# Chạy chương trình
if __name__ == "__main__":
    data = read_input("input5.txt")

    p = data['p']
    q = data['q']
    h = data['h']
    xA = data['xA']
    k = data['k']
    H = data['H']

    g, yA, r, s = dsa_signature(p, q, h, xA, k, H)
    print(f"Khóa công khai yA: {yA}")
    print(f"Chữ ký số (r, s): ({r}, {s})")

    # Xác minh
    is_valid = dsa_verify(p, q, g, yA, r, s, H)
    print(f"Chữ ký hợp lệ? {is_valid}")
