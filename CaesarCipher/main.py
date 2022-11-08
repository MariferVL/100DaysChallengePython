
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

outOfRange = len(alphabet) - 1


def encrypt():
    instruction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    og_msg = input(f"Type the message to {instruction} :\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    final_msg = ""
    if instruction == "decode":
        shift *= -1
    for letter in og_msg:
        if letter in alphabet:
            og_index = alphabet.index(letter)
            print(shift)
            new_index = og_index + shift
            final_msg += alphabet[new_index]
        elif instruction != "decode" and instruction != "encode":
            print("Wrong option.")
            i = 0
            if i < 3:
                encrypt()
            print("Program ended. Goodbye")
            break
        else:
            final_msg += letter

    print(f"The {instruction}d message is {final_msg}")


should_end = False
while not should_end:
    encrypt()

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
        print("Goodbye")
