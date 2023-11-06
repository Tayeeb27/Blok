import random
import string
import io

import pyfiglet


def generate_code():
    x = ''.join(random.choice(string.ascii_uppercase + string.digits) for i in range(5))
    generate_note(x,"text/note_3.txt")
    return x


def generate_note(code,filename):
    f = pyfiglet.Figlet(font="standard")
    # print(f"Code: {code}")
    spaced_code = " ".join(code)
    value = f.renderText(spaced_code)
    with open(filename, mode="w", encoding="utf-8") as file:
        file.write("----------------------------------------------\n\n")
        file.writelines(value)
        file.write("\n----------------------------------------------")
        if filename=="text/note_4.txt":
            file.write("\n\nHmmmm... looks like some kind of cipher. Maybe a ceaser cipher?")

def ceaser_cipher():
    possible_passwords=["hannah", "paris", "magpie", "johndoe"]
    password=random.choice(possible_passwords)
    key = random.randint(1,25)
    cipher=create_cipher(password,key)
    generate_note(cipher,"text/note_4.txt")
    generate_note(str(key),"text/note_5.txt")
    return password
    

def create_cipher(text, key):
  cipher = ''
  for char in text: 
    if char == ' ':
      cipher = cipher + char
    elif  char.isupper():
      cipher = cipher + chr((ord(char) + key - 65) % 26 + 65)
    else:
      cipher = cipher + chr((ord(char) + key - 97) % 26 + 97)
  
  return cipher
