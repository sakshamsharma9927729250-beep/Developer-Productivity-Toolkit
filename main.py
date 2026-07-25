import random
import string
import uuid
import hashlib
import qrcode
from datetime import datetime


def save_history(data):
    with open("history.txt", "a") as file:
        file.write(f"{datetime.now()} -> {data}\n")


def password_generator():
    length = int(input("Enter Password Length: "))

    characters = string.ascii_letters + string.digits + "!@#$%^&*"

    password = "".join(random.choice(characters) for _ in range(length))

    print("\nGenerated Password:", password)

    save_history(f"Password Generated: {password}")


def uuid_generator():
    uid = uuid.uuid4()

    print("\nUUID:", uid)

    save_history(f"UUID Generated: {uid}")


def hash_generator():

    text = input("Enter Text: ")

    print("\n1. MD5")
    print("2. SHA1")
    print("3. SHA256")

    choice = input("Choose: ")

    if choice == "1":
        result = hashlib.md5(text.encode()).hexdigest()

    elif choice == "2":
        result = hashlib.sha1(text.encode()).hexdigest()

    elif choice == "3":
        result = hashlib.sha256(text.encode()).hexdigest()

    else:
        print("Invalid Choice")
        return

    print("\nHash:", result)

    save_history(f"Hash Generated: {result}")


def qr_generator():

    text = input("Enter Text or URL: ")

    img = qrcode.make(text)

    img.save("QRCode.png")

    print("\nQR Code Saved as QRCode.png")

    save_history("QR Code Generated")


def username_generator():

    words = [
        "python",
        "coder",
        "dev",
        "ai",
        "unknown",
        "builder",
        "future",
        "pro"
    ]

    username = random.choice(words) + "_" + str(random.randint(100,999))

    print("\nUsername:", username)

    save_history(f"Username Generated: {username}")


while True:

    print("\n========== Developer Productivity Toolkit ==========")

    print("1. Password Generator")
    print("2. UUID Generator")
    print("3. Hash Generator")
    print("4. QR Code Generator")
    print("5. Username Generator")
    print("6. Exit")

    choice = input("Enter Choice: ")

    match choice:

        case "1":
            password_generator()

        case "2":
            uuid_generator()

        case "3":
            hash_generator()

        case "4":
            qr_generator()

        case "5":
            username_generator()

        case "6":
            print("Thank You!")
            break

        case _:
            print("Invalid Choice")