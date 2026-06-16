from PIL import Image


def encrypt_image(input_path, output_path, key):

    img = Image.open(input_path)

    pixels = img.load()

    width, height = img.size

    for x in range(width):
        for y in range(height):

            r, g, b, a = pixels[x, y]

            pixels[x, y] = (
                (r + key) % 256,
                (g + key) % 256,
                (b + key) % 256,
                a
            )

    img.save(output_path)


def decrypt_image(input_path, output_path, key):

    img = Image.open(input_path)

    pixels = img.load()

    width, height = img.size

    for x in range(width):
        for y in range(height):

            r, g, b, a = pixels[x, y]

            pixels[x, y] = (
                (r - key) % 256,
                (g - key) % 256,
                (b - key) % 256,
                a
            )

    img.save(output_path)


while True:

    print("\n=== Image Encryption Tool ===")
    print("1. Encrypt Image")
    print("2. Decrypt Image")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        image_path = input("Image path: ")
        key = int(input("Key: "))

        encrypt_image(
            image_path,
            "encrypted.png",
            key
        )

        print("Encrypted image saved as encrypted.png")

    elif choice == "2":

        image_path = input("Encrypted image path: ")
        key = int(input("Key: "))

        decrypt_image(
            image_path,
            "decrypted.png",
            key
        )

        print("Decrypted image saved as decrypted.png")

    elif choice == "3":
        break

    else:
        print("Invalid choice")