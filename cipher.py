from art import logo

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
    'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
    't', 'u', 'v', 'w', 'x', 'y', 'z'
]


def caesar(start_text, shift_amount, direction):
    if direction == "decode":
        shift_amount *= -1
    elif direction != "decode" and direction != "encode":
        print("Enter \"encode\" or \"decode\" ")
        return

    end_text = ""
    for char in start_text:
        if char not in alphabet:
            end_text += char
        else:
            end_text += alphabet[alphabet.index(char) + shift_amount]
    print(f"Here's the {direction}d result: {end_text}")


print(logo)

should_end = False
while not should_end:
    direction = input(
        "Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26
    caesar(start_text=text, shift_amount=shift, direction=direction)

    restart = input(
        "Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if restart == "no":
        should_end = True
        print("Goodbye")
