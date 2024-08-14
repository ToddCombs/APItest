import random
import string

# def generate_vin(length=17):
#     characters = string.ascii_uppercase.replace('I', '').replace('O', '').replace('Q', '') + string.digits
#     vin = ''.join(random.choices(characters, k=length))
#     return vin

def generate_random_letter():
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return random.choice(letters)

def generate_random_number():
    return str(random.randint(0, 9))

def generate_vin():
    vin = ''
    for _ in range(17):
        if _ in [8, 13, 17]:
            vin += generate_random_letter()
        else:
            vin += generate_random_number()
    return vin



vin = generate_vin()

print("车架号：", vin)