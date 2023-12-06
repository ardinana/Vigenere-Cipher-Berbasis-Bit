while True:
    print("\n=== VIGENERE CIPHER ===")
    print("Menu")
    print("1. Enkripsi")
    print("2. Dekripsi")
    print("3. Keluar")

    action = input("Pilih menu: ")

    if action == '3':
        print("Keluar dari program.")
        break

    message = input("Masukkan pesan: ")
    key = input("Masukkan key: ")

    # Menyamakan panjang pesan dan kunci
    key = key * (len(message) // len(key)) + key[:len(message) % len(key)]

    # Konversi karakter ke bit
    message_bits = ''.join([format(ord(char), '08b') for char in message])
    key_bits = ''.join([format(ord(char), '08b') for char in key])

    print("\nBit pesan:")
    for i, char in enumerate(message):
        print(f"Karakter {char}: {message_bits[i*8:(i+1)*8]}")

    print("\nHasil XOR dari bit pesan dan bit key:")
    for i, char in enumerate(message):
        xor_result = '1' if message_bits[i*8:(i+1)*8] != key_bits[i*8:(i+1)*8] else '0'
        print(f"{message_bits[i*8:(i+1)*8]} XOR {key_bits[i*8:(i+1)*8]} = {xor_result}")

    # Proses enkripsi atau dekripsi
    result_bits = ''.join('1' if message_bits[i] != key_bits[i] else '0' for i in range(len(message_bits))) if action == '1' else ''.join('1' if message_bits[i] != key_bits[i] else '0' for i in range(len(message_bits)))

    print(f"\nHasil {'enkripsi' if action == '1' else 'dekripsi'} bentuk bit:")
    print(result_bits)

    # Output hanya karakter terenkripsi atau terdekripsi
    result_message = ''.join(chr(int(result_bits[i*8:(i+1)*8], 2)) for i in range(len(result_bits)//8))

    print(f"\nHasil {'enkripsi' if action == '1' else 'dekripsi'} bentuk karakter:")
    print(result_message)