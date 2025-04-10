
def read_input(filename):
    params = {}
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            if "=" in line:
                key, value = line.split("=")
                params[key.strip()] = int(value.strip())
    return params

def main():
    params = read_input("input1.txt")
    q = params.get("q")
    a = params.get("a")
    xA = params.get("xA")
    xB = params.get("xB")

    if None in (q, a, xA, xB):
        print("File input không đầy đủ các tham số cần thiết!")
        return

    yA = pow(a, xA, q)
    yB = pow(a, xB, q)

    K_from_A = pow(yB, xA, q)
    K_from_B = pow(yA, xB, q)

    print("=== Kết quả trao đổi khoá Diffie–Hellman ===")
    print("Với An:")
    print("  Khoá công khai yA = a^(xA) mod q = {}^{} mod {} = {}".format(a, xA, q, yA))
    print("  Khoá phiên K = yB^(xA) mod q = {}^{} mod {} = {}".format(yB, xA, q, K_from_A))
    print("")
    print("Với Ba:")
    print("  Khoá công khai yB = a^(xB) mod q = {}^{} mod {} = {}".format(a, xB, q, yB))
    print("  Khoá phiên K = yA^(xB) mod q = {}^{} mod {} = {}".format(yA, xB, q, K_from_B))
    print("")
    if K_from_A == K_from_B:
        print("=> Khoá phiên K chung: {}".format(K_from_A))
    else:
        print("Có sự không khớp trong tính toán khoá phiên!")

if __name__ == "__main__":
    main()
