# Caesar Cipher program which will encode and decode text
# e.g.
#cipher_text = "mjqqt"
#shift = 5
#plain_text = "hello"
# print output: "The decoded text is hello"


logo = """


   ██████  █████  ███████ ███████  █████  ██████      
  ██      ██   ██ ██      ██      ██   ██ ██   ██     
  ██      ███████ █████   ███████ ███████ ██████      
  ██      ██   ██ ██           ██ ██   ██ ██   ██     
   ██████ ██   ██ ███████ ███████ ██   ██ ██   ██     
                                                     
                                                     
       ██████ ██ ██████  ██   ██ ███████ ██████       
      ██      ██ ██   ██ ██   ██ ██      ██   ██      
      ██      ██ ██████  ███████ █████   ██████       
      ██      ██ ██      ██   ██ ██      ██   ██      
       ██████ ██ ██      ██   ██ ███████ ██   ██      
                                                     
                                                      
                                                    

"""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(start_text, shift_amount, cipher_direction):
    """
caesar function will encode and decode the text based on shift amount nubmer.
Inside the 'decrypt' option, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.
    """
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        # if input value not in alplabets
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char

    print(f"Here's the {cipher_direction}d result: {end_text}")


print(logo)

# should continue
should_continue = True

while should_continue:
    # input options
    direction = input(
        "Type 'encode' to encrypt, type 'decode' to decrypt:\n => ")
    text = input("Type your message:\n => ").lower()
    shift = int(input("Type the shift number:\n => "))
    shift = shift % 25
    # calling the caesar function
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    result = input(
        "Type 'yes' if you want to go again. Otherwise type 'no'. \n => ")
    if result == "no":
        should_continue = False
        print("Goodbye")
