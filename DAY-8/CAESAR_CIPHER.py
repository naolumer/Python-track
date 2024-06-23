# PROJECT: CAESAR CIPHER ENCRYPTION

# print("welcome to CESAR CIPHER ENCRYPTION")
# should_continue= True
# while should_continue:


#     alphabet=['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#     direction=input("Type 'encode' to encrypt and 'decode' to decrypt \n")
#     text=input("What is your message: \n").lower()
#     shift= int(input("What is your shift: \n"))
#     shift= shift%26


# two function with if else
# def encode(text, shift):
#     cipher_text=""
#     for position in range(len(text)):

#         letter=ord(text[position]) - 96
#         shift= shift%26
#         new_letter= letter + shift
#         new_leter= alphabet[new_letter-1]
#         cipher_text+= new_leter
#     print(f"The ciphered text is '{cipher_text}' ")

# encode(text, shift)

# def decode(text, shift):
#    plain_text=""
#    for position in range(len(text)):
#       letter= ord(text[position])-96
#       shift= shift%26
#       new_letter= letter - shift
#       new_leter= alphabet[new_letter-1]
#       plain_text+=new_leter


#    print(f"the plain text is '{plain_text}' ")

# decode(text, shift)
# if direction == "encode":
#    encode(text, shift)
# elif direction =="decode":
#    decode(text, shift)
# else:
#    print("invalid input")

# single function method
    # def cesar(start_text, shift_amount, caesar_direction):
    #     end_text=""
    #     if caesar_direction== "decode":
    #         shift_amount*=-1
    #     for char in start_text:
    #         if char in alphabet:
    #            position= alphabet.index(char)
    #            new_position= position + shift_amount
    #            end_text+= alphabet[new_position]
    #         else:
    #             end_text+= char
    #     print(f"the {caesar_direction}d text is {end_text}")

    # cesar(start_text=text, shift_amount=shift, caesar_direction=direction)
    # result= input("If you want to continue type 'yes' otherwise type 'no': \n")
    # if result=="no":
    #     should_continue= False
    #     print("Goodbye")