def read_input(filename):
    params = {}
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            if "=" in line:
                key, value = line.split("=")
                params[key.strip()] = int(value.strip())
    return params

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = egcd(b % a, a)
        return (g, y - (b // a) * x, x)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception("Không tồn tại nghịch đảo modular của {} mod {}".format(a, m))
    else:
        return x % m

def main():
    params = read_input("input2.txt")

    p = params.get("p")
    q = params.get("q")
    e = params.get("e")
    M = params.get("M")

    if None in (p, q, e, M):
        print("File input2.txt chưa đầy đủ các tham số cần thiết!")
        return

    # Tính n và phi(n)
    n = p * q
    phi_n = (p - 1) * (q - 1)

    # Tính khóa riêng d sao cho e * d ≡ 1 (mod phi(n))
    d = modinv(e, phi_n)

    # Khóa công khai PU = {e, n} và khóa riêng PR = {d, n}
    PU = (e, n)
    PR = (d, n)

    # Mã hóa thông điệp M: C = M^e mod n
    C = pow(M, e, n)

    # Giải mã bản mã C: M_dec = C^d mod n
    M_dec = pow(C, d, n)

    # In kết quả
    print("=== RSA Encryption/Decryption ===")
    print("Các tham số:")
    print("  p =", p)
    print("  q =", q)
    print("  n = p*q =", n)
    print("  phi(n) =", phi_n)
    print("")
    print("a) Khóa công khai của An: PU = {e, n} = {", e, ",", n, "}")
    print("\nb) Khóa riêng của An:  PR = {d, n} = {", d, ",", n, "}")
    print("")
    print("c) Mã hóa thông điệp M =", M)
    print("   Bản mã C = M^e mod n = {}^{} mod {} = {}".format(M, e, n, C))
    print("")
    print("d) Giải mã bản mã C:")
    print("   M = C^d mod n = {}^{} mod {} = {}".format(C, d, n, M_dec))
    print("")
    if M == M_dec:
        print("=> Thông điệp đã được khôi phục chính xác!")
    else:
        print("=> Có lỗi trong quá trình mã hóa/giải mã!")
    print("")
    print("e) Việc mã hóa thông điệp ở câu c) thực hiện nhiệm vụ bảo mật (encryption),")
    print("   không phải nhiệm vụ chữ ký số.")

if __name__ == "__main__":
    main()
