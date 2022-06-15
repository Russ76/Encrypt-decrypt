# encrypt-it.py
# Reads a line from file, removes spaces
# writes it out to second file in reverse format for each line
# and inserts additional padding to obfuscate message.
# Continues reading all lines in read file
# 54 characters below in padding string, adding other letters
import random
import os
import string

g = "aaabccddeeeffgghhiiijkllmmnnnoooppqrrrssstttuuvvwwxzy"
with open("output_code.txt", "a") as target:
    # Delete this file after processing done
    with open("new_input.txt", "r") as source:
        for line in source:
            # reject lines that are too short
            if len(line) < 2 : continue
            # slicing the string in reverse fashion 
            for element in line[ : :-1]:
                # 
                if element == "x": element = "í"
                if element == " ": element = "x"
                # if element == chr(10): continue
                # if element == "'": element = ""
                var2 = random.choice(g)
                target.write(element)
                target.write(var2)
                # print(element, end ='')
                # print(var2, end='')
                # print(ord(element))
            # print('\n')

# Changes file into "words" of five characters each and adds spaces.
def read_file():
    sp=" "
    chunk_size = 5
    while (contents := source.read(chunk_size)):
        target.write(contents)
        target.write(sp)
        print(contents, end=" ")
        # print(" ")
with open("output_new.txt", "a") as target:
    # comment
    with open("output_code.txt", "r") as source:
        read_file()
        # target.close()

# Now change ascii of each character by three
with open("output_encrypted.txt", "a") as target:
    # The above is final file
    with open("output_new.txt", "r",) as source:
        for line in source:
            # reject lines that are too short
            if len(line) < 2 : continue
            # slicing the string by each character
            for element in line[ : :1]:
                # 
                if element == " ":
                    target.write(element)
                    # spaces are fine, send through
                    continue
                s = ord(element)
                if s > 250 : s = 250
                # print(s, end=" ")
                s = s - 3
                # change these characters to others
                target.write(chr(s)) 
                # if element == chr(13): continue
                # Now message is really hidden. NOT MILITARY STRENGTH

if os.path.exists("output_code.txt"):
    os.remove("output_code.txt")
if os.path.exists("output_new.txt"):
    os.remove("output_new.txt")
    # remove working files, not needed again