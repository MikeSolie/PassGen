import random
import string


password_length = int(input('Desired Password Length: '))              # user input for password length
pass_chars = string.ascii_letters + string.punctuation + string.digits # replaced by string
new_password = ''                                                      # empty password string
account = str(input('What is this for? '))                             # Account variable
for c in range(password_length):                                       # iterate over the password length w/random chars
	new_password = new_password + random.choices(pass_chars)[0]

print(f'The new password for your {account} account is {new_password}')


