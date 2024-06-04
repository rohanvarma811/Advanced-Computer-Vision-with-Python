from time import sleep
import random

palabra = "Hello world"
abc = list(' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
txt = ""

j = 0
while j < len(palabra):
    random_char = abc[random.randint(0, len(abc)-1)]
    print(txt + random_char, end="\r", flush=True)
    sleep(0.02)
    if random_char == palabra[j]:
        txt += random_char
        j += 1

    # To ensure the final result is displayed correctly without the carriage return effect
    print(txt)