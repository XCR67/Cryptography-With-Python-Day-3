#DAY 3 - SYMMETRIC ENCRPTION
#Dependencies
import random
import string
#Converts readable text into Hexadecimal
def conHex(message):
  result = ""
  for i in range(len(message)):
    result += str(hex(ord(message[i]))) #Convert its to ascii > Hexadecimal > String
  return result
#Reverts the Hexadecimal string back into readable text
def revHex(hexmessage):
  result = ""
  letter = 2
  while letter < len(hexmessage): #Go though every letter in the message
    tenplc = int(hexmessage[letter], 16) * 16
    onesplc = int(hexmessage[letter + 1], 16) 
    result += chr(tenplc + onesplc) #Converts sum into its letter equivalent using ascii
    letter += 4 #Move to the next letter
  return result
#Encrypts the message by adding the key to the message
def encryptSymm(message, key):
  #Variable initializationa nd converts key and message to encryptable hex values
  message = conHex(message)
  key = conHex(key)
  index = 2
  cipherText = ""
  while index < len(message) - 1: #Go thorugh eac letter in message
    #Swap hex values of message and key by adding their tens and ones places
    ten = int(message[index], 16) * 16 + int(key[index + 1], 16)
    one = int(message[index + 1], 16) + int(key[index], 16) * 16
    cipherText += chr(ten + one) #Converts sum into its letter equivalent using ascii
    index += 4
  return cipherText
#Decrypts the encrypted text with the same key
def decryptSymm(cipherText, key):
  #Variable initializationa nd converts key and message to decryptable hex values
  cipherText = conHex(cipherText)
  key = conHex(key)
  index = 2
  message = ""
  while index < len(cipherText) - 1: #Go thorugh eac letter in message
    #Revert hex values of message and key by subtracting their tens and oens places
    ten = int(cipherText[index], 16) * 16 - int(key[index + 1], 16)
    one = int(cipherText[index + 1], 16) - int(key[index], 16) * 16
    message += chr(ten + one) #Converts sum into its letter equivalent using ascii
    index += 4
  return message
#Encryption and Key Generation
message = input("Enter your secret message: ")
key = input("Enter a key of at least length " + str(len(message)) + ":")
while len(key) < len(message): #Makes sure the key is as long as the message
  key = input("Key must be at least length " + str(len(message)) + ":")
print("Key is " + key)
cipherText = encryptSymm(message, key)
print(cipherText)
#Decryption
print(decryptSymm(cipherText, key))
