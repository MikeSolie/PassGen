##########################################
# Mike Solie                             #
# 03/01/2023                             #
# Version 1.2                            #
#   -->Added Username Function           #
#                                        #
# Description:                           #
# Username Password Generator - Takes    #
# user input to create a username and    #
# the desired length of the new password #
##########################################

#####
# Import random to randomize characters
# Import string for simplicity
#####
import random
import string

#####
# function: username_generator
# purpose: to create a username
# inputs: first and last name
# returns: sliced username
#####
def username_generator(first, last):
    username = first[:1] + last[:5]
    return username

#####
# function: password generator
# purpose: create randomized password given user parameters
# inputs: password length
# returns: new password
#####
def password_generator():
    new_password = ''
    password_length = int(input('Desired Password Length: '))
    pass_chars = string.ascii_letters + string.punctuation + string.digits
    for c in range(password_length):
        new_password = new_password + random.choices(pass_chars)[0]
    return new_password

#####
# function: main
# purpose: to provide new password
# inputs: names and account
# returns: nothing
#####
def main():
    name = input('Enter First + Last Name: ').split(' ')
    user = username_generator(name[0], name[1]).lower()
    account = str(input('What is this for?: '))
    password = password_generator()
    print(f'Your new username is {user}')
    print(f'Your new password for your {account} account is {password}')

# call to start program
##---->>
main()
##<<----

