# program to generate long random string

import random
import string

def randomString(stringLength=100):
    """Generate a random string of letters numbers special characters and symbols """
    # Get the ascii characters
    lettersAndDigits = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))

with open("secret.txt", "w") as f:
    f.write(randomString(320))