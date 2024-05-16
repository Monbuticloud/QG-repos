
try:
    import os
    import random
    import math
    import time
    import sys
    from decimal import Decimal
    from colorama import Fore

except ImportError as e:
    print("Error -> ", e)    

sys.set_int_max_str_digits(100000000)


os.system("clear")

print(Fore.BLUE+"Made by Mon")
print("Made by Nguyen Hoang Quoc Anh")
print("Version 1.00.00 -- The first version")
print("-- QG --"+Fore.RESET)
time.sleep(4)
os.system("clear")
isNotNum = True

while isNotNum:
    try:
        diff = int(input(Fore.YELLOW+f'enter a valid number to change the diffuculty 1-infinity\n\n'+Fore.RESET))

        isNotNum = False
    except:
        print(Fore.RED+"please enter a valid number"+Fore.RESET)

        isNotNum = True

print(Fore.GREEN)




mag = Decimal(10) ** Decimal(diff)

data = "Data Dump Recollection"
os.system("clear")

for _ in range(10):
    num1 = random.randint(1,mag)
    num2 = random.randint(1,mag)

    x = random.randint(1,mag)

    xs = x * x

    xsa = num1 * xs

    bx = num2  * x

    tt = xsa + bx

    ttn = 0 - tt
    data = data + "\n" + (str(num1)+"x²+"+str(num2)+"x+"+str(ttn)+"=0")
    print(str(num1),"x²+",str(num2),"x+",str(ttn),"=0")
print(Fore.RESET)
f = open("dataQG.txt", "w")

f.write(data)

f.close