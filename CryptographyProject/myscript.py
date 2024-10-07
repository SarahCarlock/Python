# First message decoding help used
alphabet = "abcdefghijklmnopqrstuvwxyz"
message = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"

translated_message = ""

for character in message:
  if character in alphabet:
    character_value = alphabet.find(character)
    translated_message += alphabet[(character_value + 10) % 26]
  else:
    translated_message += character

print(translated_message)




# First message encoding help used
message_for_v = "hey vishal! This is a super cool cipher, thanks for showing me! What else you got?"

translated_message_for_v = ""

for character in message_for_v:
  if character in alphabet:
    character_value = alphabet.find(character)
    translated_message_for_v += alphabet[(character_value - 10) % 26]
  else:
    translated_message_for_v += character
        
print(translated_message_for_v)





# Decoding a message
alphabet = "abcdefghijklmnopqrstuvwxyz"
# message = "jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud."
# message = "bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!"

def caesar_decode(message, offset):
  decodedMessage = ""
  for character in message:
      if character in alphabet:
          character_value = alphabet.find(character)
          decodedMessage += alphabet[(character_value + offset) % 26]
      else:
          decodedMessage += character
  print(decodedMessage)

caesar_decode("jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud.", 10)
caesar_decode("bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!", 14)





# Encoding a message
alphabet = "abcdefghijklmnopqrstuvwxyz"
# message = "let's go"

def caesar_encode(message, offset):
  encodedMessage = ""
  for character in message:
      if character in alphabet:
          character_value = alphabet.find(character)
          encodedMessage += alphabet[(character_value - offset) % 26]
      else:
          encodedMessage += character
  print(encodedMessage)

caesar_encode("let's go!", 10)




# First message decoding help used
alphabet = "abcdefghijklmnopqrstuvwxyz"
message = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"
translated_message = ""
for character in message:
  if character in alphabet:
    character_value = alphabet.find(character)
    translated_message += alphabet[(character_value + 10) % 26]
  else:
    translated_message += character
print(translated_message)
# First message encoding help used
message_for_v = "hey vishal! This is a super cool cipher, thanks for showing me! What else you got?"
translated_message_for_v = ""
for character in message_for_v:
  if character in alphabet:
    character_value = alphabet.find(character)
    translated_message_for_v += alphabet[(character_value - 10) % 26]
  else:
    translated_message_for_v += character     
print(translated_message_for_v)
# Decoding a message
alphabet = "abcdefghijklmnopqrstuvwxyz"
# message = "jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud."
# message = "bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!"
def caesar_decode(message, offset):
  decodedMessage = ""
  for character in message:
      if character in alphabet:
          character_value = alphabet.find(character)
          decodedMessage += alphabet[(character_value + offset) % 26]
      else:
          decodedMessage += character
  return decodedMessage
caesar_decode("jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud.", 10)
caesar_decode("bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!", 14)
# Encoding a message
alphabet = "abcdefghijklmnopqrstuvwxyz"
# message = "let's go"
def caesar_encode(message, offset):
  encodedMessage = ""
  for character in message:
      if character in alphabet:
          character_value = alphabet.find(character)
          encodedMessage += alphabet[(character_value - offset) % 26]
      else:
          encodedMessage += character
  return encodedMessage
caesar_encode("let's go!", 10)
#Brute force a message, solving without knowing the offset
brute_force_message = "vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl tl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx."

for i in range(1, 26):
  print("Offset: {}".format(i))
  print("\t {}".format(caesar_decode(brute_force_message, i)))
# Offset = 7



# Vigenere Cypher
def vigenere_decode(message, keyword):
  keyword_phrase = ""
  keyword_index = 0

  for character in message:
    if keyword_index >= len(keyword):
      keyword_index = 0
    if character in alphabet:
      keyword_phrase += keyword[keyword_index]
      keyword_index += 1
    else:
      keyword_phrase += character

  decoded_message = ""

  for i in range(len(message)):
    if message[i] in alphabet:
      old_character_index = alphabet.find(message[i])
      offset_index = alphabet.find(keyword_phrase[i])
      new_character = alphabet[(old_character_index + offset_index) % 26]
      decoded_message += new_character
    else:
      decoded_message += message[i]
    
  return decoded_message

vigenere_message = "txm srom vkda gl lzlgzr qpdb? fepb ejac! ubr imn tapludwy mhfbz cza ruxzal wg zztcgcexxch!"
vigenere_keyword = "friends"
alphabet = "abcdefghijklmnopqrstuvwxyz"
print(vigenere_decode(vigenere_message, vigenere_keyword))

#Vigenere Encoder
def vigenere_encode(message, keyword):
  keyword_phrase = ""
  keyword_index = 0

  for character in message:
    if keyword_index >= len(keyword):
      keyword_index = 0
    if character in alphabet:
      keyword_phrase += keyword[keyword_index]
      keyword_index += 1
    else:
      keyword_phrase += character

  encoded_message = ""

  for i in range(len(message)):
    if message[i] in alphabet:
      old_character_index = alphabet.find(message[i])
      offset_index = alphabet.find(keyword_phrase[i])
      new_character = alphabet[(old_character_index - offset_index) % 26]
      encoded_message += new_character
    else:
      encoded_message += message[i]
    
  return encoded_message

vigenere_message_for_v = "thanks for teaching me all these cool ciphers! you really are the best!"
keyword_for_v = "besties"

print(vigenere_encode(vigenere_message_for_v, keyword_for_v))
print(vigenere_decode(vigenere_encode(vigenere_message_for_v, keyword_for_v), keyword_for_v))