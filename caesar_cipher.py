letters= 'abcdefghijklmnopqrstuvwxyz'
num_letters= len(letters)

# def encrypt(plaintext, key):
#     ciphertext=' '
#     for letter in plaintext:
#         letter= letter.lower()
#         if not letter == ' ':
#             index= letter.find(letter)
#             if index == -1:
#                 ciphertext += letter
#             else:
#                 newindex= index + key
#                 if new_index >= 26:
#                     new_index -= 26
#                 ciphertext += letters[new_index]
#     return ciphertext


# def decrypt(ciphertext, key):
#     plaintext=' '
#     for letter in plaintext:
#         letter= letter.lower()
#         if not letter == ' ':
#             index= letter.find(letter)
#             if index == -1:
#                 plaintext += letter
#             else:
#                 new_index= index - key
#                 if new_index >0:
#                     new_index += 26
#                 plaintext += letters[new_index]
#     return plaintext

def encrypt_decrypt(text, mode, key):
    result = ""
    if mode == 'decrypt':
        key=-key

    for letter in text:
        letter = letter.lower()
        if letter == ' ':
            result += letter
        else:
            index= letters.find(letter)
            if index == -1:
                result += letter
            else:
                new_index= index+key
                if new_index >= num_letters:
                    new_index -= num_letters
                elif new_index < 0:
                    new_index+=num_letters
                result+= letters[new_index]
    return result


def main():
    print("*--*CAESAR CIPHER*--*")
    mode = input("Do you want to encrypt or decrypt? ").lower()
    key = int(input("Enter the key (1 through 26): "))
    text = input("Enter the message: ")
    result = encrypt_decrypt(text, mode, key)
    print(f"The result is: {result}") 

if __name__ == "__main__":
    main()


    


# print()


# print()
# print('*--*CAESAR CIPHER*--*')
# print('Do you want to encrypt or decrypt? ')
# user_input= input('encrypt/decrypt: ').lower()

# print()


# if user_input == 'encrypt':
#     print('ENCRYPTION MODE SELECTED')
#     print()
#     key= int(input('Enter the key(1 through 26): '))
#     text= input('Enter the text to encrypt: ')
#     ciphertext= encrypt_decrypt(text, 'encrypt', key)
#     print(f'CIPHERTEXT: {ciphertext}')

# elif user_input == 'decrypt':
#     print('ENCRYPTION MODE SELECTED')
#     print()
#     key= int(input('Enter the key(1 through 26): '))
#     text= input('Enter the text to encrypt: ')
#     plaintext= encrypt_decrypt(text, 'decrypt', key)
#     print(f'PLAINTEXT: {plaintext}')


