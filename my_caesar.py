def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shifted = (ord(char) - ord("a") + shift) % 26
            result += chr(ord("a") + shifted)
        else:
            result += char

    return result

message = input("What message would you like to encrypt?\n")
shift = int(input("How much would you like to shift this by?\n"))

print(encrypt(message, shift))