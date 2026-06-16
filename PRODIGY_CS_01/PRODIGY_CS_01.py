def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.upper()
            encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            result += encrypted_char if is_upper else encrypted_char.lower()
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

while True:

    print("\n--- Caesar Cipher ---")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        text = input("Enter message: ")
        shift = int(input("Enter shift: "))
        print("Encrypted:", encrypt(text, shift))

    elif choice == "2":
        text = input("Enter encrypted message: ")
        shift = int(input("Enter shift: "))
        print("Decrypted:", decrypt(text, shift))

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")