import random

temperature = random.randint(30, 100)
print(f'DEBUG - temperature: {temperature}')
if temperature in range (65 , 81):
    print("It's a nice day!")
else:
    print("It's not nice out.")