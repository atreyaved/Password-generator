import random
import array
import os

os.system('touch ~/saved-password.txt')



MAX_LEN = 12
  

DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']  
LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                     'z']
  
UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 
                     'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z']
  
SYMBOLS = ['@', '#', '$', '%', '=','?' , '/', '|', '~', '>', 
           '*', '(', ')', '<']
  
COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS
rand_digit = random.choice(DIGITS)
rand_upper = random.choice(UPCASE_CHARACTERS)
rand_lower = random.choice(LOCASE_CHARACTERS)
rand_symbol = random.choice(SYMBOLS)
temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol

for x in range(MAX_LEN - 4):
    temp_pass = temp_pass + random.choice(COMBINED_LIST)
    temp_pass_list = array.array('u', temp_pass)
    random.shuffle(temp_pass_list)

password = ""
for x in temp_pass_list:
        password = password + x

def addToClipBoard():
    os.system('echo "%s" | xsel -i' % password)
def ShowPassword():
    print ("your super strong password is : " + password)
    print ("Password copied to clipboard")
    addToClipBoard()

ShowPassword()

Command = input("What is this password for?(Name of the site):")

def WriteText():
    with open("saved-password.txt", "a+") as file_object:

        file_object.seek(0)
        
        data = file_object.read(100)
        if len(data) > 0 :
            file_object.write("\n")

        file_object.write(Command + " : " + password)
    
    

def SaveToFile():
    print ("Do you want to save the current password to a file?")
    Option = input('Y/N?:')
    if Option == "Y" :
        WriteText()
    elif Option == "N":
        print ("Done")
    else:
        print ("Done")

SaveToFile()
