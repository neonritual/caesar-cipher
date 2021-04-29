alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

# def Convert(string):
#     text_as_list=[]
#     text_as_list[:0]=string
#     return text_as_list
# print(Convert(text))


    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛


#MY ORIGINAL TRY (works but not great)
# n = len(text)
# cipher_list = []

# def encrypt(text, shift):
#   x = 0
#   while x != n: 
#     index = alphabet.index(text[x])
#     outcode = alphabet[index + shift]
#     x += 1
#     cipher_list.append(outcode)
#   print(*cipher_list, sep='' ) 

#TEACHER's VERSION for study

def encrypt(plain_text, shift_amount):
  cipher_text = ""
  for letter in plain_text:
    position = alphabet.index(letter)
    if position > 23:
      position = -1
    new_position = position + shift_amount
    new_letter = alphabet[new_position]
    cipher_text += new_letter
  print(f"The encoded text is {cipher_text}")

encrypt(plain_text=text, shift_amount=shift)

# print(cipher_list)

# TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
# 