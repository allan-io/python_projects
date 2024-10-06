from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# TODO-2: What happens if the user enters a number/symbol/space?


def caesar():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    program_on = True
    while program_on:
        output_text = ""
        not_text = ""
        if direction == "decode":
            shift *= -1
        for letter in text:
            if letter not in alphabet:
                not_text += letter
            else:
                shifted_position = alphabet.index(letter) + shift
                shifted_position %= len(alphabet)
                output_text += alphabet[shifted_position]
        print(f"Here is the {direction}d result: {output_text + not_text}")

        another_input = input("Type 'yes' if you want to go again. Otherwise, type 'no'.").lower()
        if another_input == "no":
            program_on = False
            print("Goodbye")
        else:
            direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
            text = input("Type your message:\n").lower()
            shift = int(input("Type the shift number:\n"))

# TODO-3: Can you figure out a way to restart the cipher program?




caesar()



