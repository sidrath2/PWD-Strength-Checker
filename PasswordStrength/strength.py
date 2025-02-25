'''
Rules of a strong password:

Weak Password: Less than 8 characters, only lowercase letters
Moderate Password: 8+ characters, includes letters and numbers
Strong Password: 12+ characters, includes uppercase, lowercase, numbers, and special characters
Very Strong Password: 16+ characters, high entropy, mix of all character types



Entropy=log 
2
​
 (Character Set Size 
Password Length
 )


In cybersecurity, entropy measures the randomness and unpredictability of a password. 
It helps determine how difficult a password is to guess using brute-force attacks.


Time to Crack= 
Guesses per Second
2 
Entropy−1
 
​


'''


import math
import getpass

def calculate_entropy(password):

    #A dictionary char_sets is created, storing the four possible character types:
    char_sets = {
        "lowercase": "abcdefghijklmnopqrstuvwxyz",
        "uppercase": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        "numbers": "0123456789",
        "special": "!@#$%^&*()-_=+[]{}|;:'\",.<>?/~`"
    }
    
    char_set_size = 0
    if any(c in char_sets["lowercase"] for c in password):
        char_set_size += 26
    if any(c in char_sets["uppercase"] for c in password):
        char_set_size += 26
    if any(c in char_sets["numbers"] for c in password):
        char_set_size += 10
    if any(c in char_sets["special"] for c in password):
        char_set_size += len(char_sets["special"])
    



    if char_set_size == 0:
        return 0


    entropy = math.log2(pow(char_set_size,len(password)))

    return entropy



def classify_strength(entropy):
    if entropy < 40:
        return "This is a VERY WEAK password!"
    elif entropy >= 40 and entropy < 60:
        return "This is a WEAK password!"
    elif entropy >= 60 and entropy < 80:
        return "This is a MODERATE password!"
    else:
        return "This is a STRONG password!"


def time_to_crack(entropy, guesses):
    formula = (pow(2, entropy-1))/guesses
    

    if formula < 60:
        return f"{formula:.2f} seconds"
    elif formula < 3600:
        return f"{formula / 60:.2f} minutes"
    elif formula < 86400:
        return f"{formula / 3600:.2f} hours"
    elif formula < 31536000:
        return f"{formula / 86400:.2f} days"
    elif formula < 3153600000:
        return f"{formula / 31536000:.2f} years"
    else:
        return f"{formula / 3153600000:.2f} centuries"


# Use getpass.getpass() to hide input while typing
pwd = getpass.getpass("Please input your password: ")
calc = calculate_entropy(pwd)
strength = classify_strength(calc)
online_crack_time = time_to_crack(calc, 1_000)  # Online attack (1,000 guesses/sec)
offline_crack_time = time_to_crack(calc, 100_000_000_000)  # Offline attack (100B guesses/sec)
supercomputer_crack_time = time_to_crack(calc, 1_000_000_000_000_000)  # Supercomputer (1 quadrillion/sec)


print ("Entropy: ", calc)
print (strength)
print ("Online crack time:", online_crack_time)
print("Offline crack time:", offline_crack_time)
print("Supercomputer crack time:", supercomputer_crack_time)