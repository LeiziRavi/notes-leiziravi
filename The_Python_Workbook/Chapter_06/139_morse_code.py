from cgitb import text
import re
morse_code_character = {
    "A": ".", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.",
    "H": "....", "I": "..", "J": ".", "K": "-.-", "L": ".-..", "M": "--", "N": "-.",
    "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-", "U": "..-", "V": "...-",
    "W": ".--", "X": "-..-", "Y": "-.--", "Z": "--..",
    "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....",
    "6": "-....", "7": "--...", "8": "---..", "9": "----."
}

msg = input("Enter the message: ")

to_character = re.findall("[a-zA-Z]", msg)
char_upper = [char.upper() for char in to_character]

morse_code = ""
for i in char_upper:
    if(i in morse_code_character):
        morse_code = morse_code + morse_code_character[i] + " "

print(morse_code)
