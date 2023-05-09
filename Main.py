import random

import string

import zxcvbn

def generate_password(length=20, complexity=3):

    character_sets = {

        1: string.ascii_letters,

        2: string.ascii_letters + string.digits,

        3: string.ascii_letters + string.digits + string.punctuation

    }

    password = ''

    while len(password) < length:

        character_set = character_sets.get(complexity, string.ascii_letters)

        password += random.choice(character_set)

    return password

def check_password_strength(password):

    result = zxcvbn.zxcvbn(password)

    strength = result['score']

    return strength

def generate_passwords(num_passwords=10, length=20, complexity=3):

    password_list = []

    for i in range(num_passwords):

        password = generate_password(length, complexity)

        strength = check_password_strength(password)

        password_list.append((password, strength))

    password_list = sorted(password_list, reverse=True)

    return password_list

password_length = 20

password_complexity = 3

num_passwords = 10

passwords = generate_passwords(num_passwords, password_length, password_complexity)

for password, strength in passwords:

    print('Password:', password, '- Strength:', strength)
