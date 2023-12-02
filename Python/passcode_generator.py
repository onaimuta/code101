import string
import random

print("Welcome to the Password Generator")
## characters to generate lists from
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")
def genetate_random_password():
    ## length of password from user
    length = int(input("Enter password length: "))

    ## shuffling the characters
    random.shuffle(characters)

    ## picking random characters from list
    password = []
    for i in range(length):
        password.append(random.choice(characters))
    
    ## shuffling the resultant password
    random.shuffle(password)

    ## converting the list to a string
    ## printing the list
    print("".join(password))

## invoking the function
genetate_random_password()
