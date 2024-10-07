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

# Decoding a message
alphabet = "abcdefghijklmnopqrstuvwxyz"
message = ["jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud.", "bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!"]
decodedMessage = ""
def caesar_decode(message, offset):
    for character in message:
        if character in alphabet:
            character_value = alphabet.find(character)
            decodedMessage += alphabet[(character_value + offset) % 26]
        else:
            decodedMessage += character
    return decodedMessage
print(decodedMessage)
# Encoding a message
alphabet = "abcdefghijklmnopqrstuvwxyz"
message = "let's go"
encodedMessage = ""
def caesar_encode(message, offset):
    for character in message:
        if character in alphabet:
            character_value = alphabet.find(character)
            encodedMessage += alphabet[(character_value - offset) % 26]
        else:
            encodedMessage += character
print(encodedMessage)