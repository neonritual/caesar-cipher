alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
if direction != "encode" and direction != "decode":
  print("Sorry, I don't know what you mean.")
else:
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))



def caesar(plain_text, shift_amount, order):
  cipher_text = ""
  for letter in plain_text:
    position = alphabet.index(letter)
    if position > 23:
      position = -1
    if order == "encode":
       new_position = position + shift_amount
    elif order == "decode":
       new_position = position - shift_amount
    new_letter = alphabet[new_position]
    cipher_text += new_letter
  print(f"The {order}d text is {cipher_text}.") 


caesar(plain_text=text, shift_amount=shift, order=direction)


# def encrypt(plain_text, shift_amount):
  # cipher_text = ""
  # for letter in plain_text:
  #   position = alphabet.index(letter)
  #   if position > 23:
  #     position = -1
  #   new_position = position + shift_amount
  #   new_letter = alphabet[new_position]
  #   cipher_text += new_letter
  # print(f"The encoded text is {cipher_text}.")



# def decrypt(plain_text, shift_amount):
#   cipher_text = ""
#   for letter in plain_text:
#     position = alphabet.index(letter)
#     if position > 23:
#       position = -1
#     new_position = position - shift_amount
#     new_letter = alphabet[new_position]
#     cipher_text += new_letter
#   print(f"The decoded text is {cipher_text}.")


# if direction == "encode":
#   encrypt(plain_text=text, shift_amount=shift)
# if direction == "decode":
#   decrypt(plain_text=text, shift_amount=shift)

