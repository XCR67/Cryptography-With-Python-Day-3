#DAY 3 - SYMMETRIC ENCRYPTION
#Dependencies (random and string

#Converts readable text into Hexadecimal
#def conHex(message):
  #Make result string

  #Loop through each letter
    #Convert the ascii value of the letter into hexadecimal and add it to result by casting it to a string

  #Return the result


#Reverts the Hexadecimal string back into readable text
#def revHex(hexmessage):
  #Make result string and a letter variable at 2

  #Go though every 2 digit hex value in the message using a while loop
    #Convert the tens place from hexadecimal to decimal using int(hex, 16) * 16

    #Convert the ones place from hexadecimal to decimal using int(hex, 16

    #Converts sum of the ones place and tens place into its letter equivalent using chr()

    #Move to the next set of 2 digit hex value

  #Return the result


#Encrypts the message by adding the key to the message
#def encryptSymm(message, key):
  #Variable initialization and converts key and message to encryptable hex values

  #Also make result string and a letter variable at 2

  #Go though every 2 digit hex value in the message using a while loop
    #Add the hex decimal value of the tens place of msg with the decimal 
    #value of the ones place of key and vice versa

    #Converts sum of the math done above into its letter equivalent using ascii

    #Move to the next set of 2 digit hex value

  #Return the result


#Decrypts the encrypted text with the same key
#def decryptSymm(cipherText, key):
  #Variable initialization and converts key and cipherText to decryptable hex values

  #Also make result string and a letter variable at 2

  #Go though every 2 digit hex value in the message using a while loop
    #Add the hex decimal value of the tens place of cipherText with the decimal 
    #value of the ones place of key and vice versa (cipheText is always subtracted by key

    #Converts sum into its letter equivalent using ascii

    #Move to the next set of 2 digit hex value

  #Return the result

#Encryption and Key Generation

#Make sure the key is as long as the message

#Decryption

