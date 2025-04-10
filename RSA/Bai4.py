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
    g, x, _ = egcd(a, m)
    if g != 1:
        raise Exception("Không tồn tại nghịch đảo modular của {} mod {}".format(a, m))
    return x % m

def main():
    params = read_input("input4.txt")

    q = params.get("q")
    a = params.get("a")
    xA = params.get("xA")
    k = params.get("k")
    M = params.get("M")

    if None in (q, a, xA, k, M):
        print("File input4.txt chưa đầy đủ các tham số cần thiết!")
        return

    # a) Tính khóa công khai của An: Y_A = a^(xA) mod q
    Y_A = pow(a, xA, q)
    print("a) Khóa công khai của An:")
    print("   PU = {{q, a, Y_A}} = {{ {}, {}, {} }}".format(q, a, Y_A))

    # b) Người gửi (Ba) mã hóa thông điệp M gửi cho An:
    # Tính C1 = a^k mod q và C2 = M * Y_A^k mod q
    C1 = pow(a, k, q)
    C2 = (M * pow(Y_A, k, q)) % q
    print("\nb) Mã hóa thông điệp:")
    print("   Với k = {} và M = {}:".format(k, M))
    print("   Bản mã (C1, C2) = ({}, {})".format(C1, C2))

    # c) Giải mã bản mã (C1, C2) bởi An:
    s = pow(C1, xA, q)
    s_inv = modinv(s, q)
    M_dec = (C2 * s_inv) % q
    print("\nc) Giải mã bản mã:")
    print("   Tính s = C1^(xA) mod q = {}^{} mod {} = {}".format(C1, xA, q, s))
    print("   Nghịch đảo s (mod q) = {}".format(s_inv))
    print("   Khôi phục M = C2 * s_inv mod q = {} * {} mod {} = {}".format(C2, s_inv, q, M_dec))

if __name__ == "__main__":
    main()
