import password as password

import random

symbols = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

password_length = int (input('Какую длину пароля вы хотите?'))

password = ''

for i in range(password_length):
    password = password + random.choice(symbols)

print(password)

