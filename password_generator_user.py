import secrets
import string

alphabet = string.ascii_letters
numbers = string.digits
punctuation = string.punctuation

passwd_complete = alphabet + numbers + punctuation

def validation_psswd():
    '''Create password lenght with users input, and validate it, with some conditions
    (Minimum lenght condition and stablished lenght condition).'''

    while True:

        user = input('''\nRemember! The password must have at least 8 characters
        Enter the lenght of the password: ''')

        if (int(user) < 8):
            print("The password must have 8 characters!")

        elif ((int(user) >= 8) and (int(user) <= 30)):
            password = "".join(secrets.choice(passwd_complete) for i in range (int(user)))
            print(password)

        else:
            print("The maximum lenght is 30!")

validation_psswd()
