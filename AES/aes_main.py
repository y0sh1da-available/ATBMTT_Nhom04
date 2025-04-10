import re
from aes_encrypt import encrypt_perform, hex_string_to_byte_array, generate_round_keys, word_array_to_hex_string

def read_input_file():
    try:
        with open("input.txt", "r") as f:
            lines = f.read().splitlines()
            if len(lines) < 2:
                print("Input file must have at least two lines (plaintext and key).")
                return None, None

            plaintext = lines[0].strip().upper()
            key = lines[1].strip().upper()
            return plaintext, key
    except FileNotFoundError:
        print("File 'input.txt' not found.")
        return None, None


def encrypt_menu():
    print("\n---- ENCODE TEXT ----")
    plaintext, key = read_input_file()
    if plaintext is None or key is None:
        return

    if len(plaintext) != 32 or not re.fullmatch(r'[0-9A-F]+', plaintext):
        print("Invalid plaintext in file. Must be 32 hex characters.")
        return

    if len(key) != 32 or not re.fullmatch(r'[0-9A-F]+', key):
        print("Invalid key in file. Must be 32 hex characters.")
        return

    encrypt_perform(plaintext, key)


def generate_keys_menu():
    print("\n---- GENERATE AND DISPLAY ROUND KEYS ----")
    _, key = read_input_file()
    if key is None:
        return

    if len(key) != 32 or not re.fullmatch(r'[0-9A-F]+', key):
        print("Invalid key in file. Must be 32 hex characters.")
        return

    key_bytes = hex_string_to_byte_array(key)
    round_keys = generate_round_keys(key_bytes)

    print("\nRound Keys:")
    for i in range(11):
        print(f"Round Key {i}: {word_array_to_hex_string(round_keys[i])}")


def main():
    running = True
    while running:
        print("\n======== AES ENCODE/DECODE ========")
        print("1. Encode (read from input.txt)")
        print("2. Generate and display Round Keys (read from input.txt)")
        print("3. Exit")
        choice_input = input("Select: ").strip()

        if not choice_input.isdigit() or not 1 <= int(choice_input) <= 3:
            print("[1-3] only")
            continue

        choice = int(choice_input)

        if choice == 1:
            encrypt_menu()
        elif choice == 2:
            generate_keys_menu()
        elif choice == 3:
            running = False


if __name__ == "__main__":
    main()
