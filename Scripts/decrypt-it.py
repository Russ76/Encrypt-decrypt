# decrypt-it.py
# Decrypt text file that was encrypted by encrypt-it.py
# NOT MILITARY STRENGTH
# Just for fun, and learning Python!
import os

with open("intermediate.txt", "a") as target:
    # working file, just to help manage things
    with open("output_encrypted.txt", "r") as source:
        for line in source:
            if len(line) < 2 : continue
            # slicing the string in single characters
            for element in line[ : :1]:
                # b=(element[1:2])
                # Throw out the fake spaces
                if element == " ": continue
                s = ord(element)
                if s > 250 : s = 250
                # print(s, end=" ")
                s = s + 3
                # change these characters to others
                target.write(chr(s)) 
                # if element == chr(13): continue
                # target.write(var2)
                # print(element, end ='')
                # print(var2, end='')
                # print('\n')
            target.write('\n')

with open("decrypted_code.txt", "a") as target:
    # The above is our final file
    with open("intermediate.txt", "r") as source:
        for line in source:
            if len(line) < 2 : continue
            # slicing the string in reverse fashion
            # Only getting letter with meaning
            for element in line[ : :-2]:
                # b=(element[1:2]) 
                # if element == " ": element = ""
                if element == "x": element = " "
                if element == "í": element = "x"
                # if element == "'": element = ""
                # var2 = random.choice(g)
                target.write(element)
                # target.write(var2)
                print(element, end ='')
                # print(var2, end='')
                # print('\n')

if os.path.exists("intermediate.txt"):
    os.remove("intermediate.txt")
# This file not needed further