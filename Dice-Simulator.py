import random

run = "y"

while run != "n":
    # generate random integer from 1-6
    output = random.randint(1, 6)
    # print output
    print(output)
    run = input("Run again? y/n   ")
else:
    print("Thank you for using PrimeMortal's dice simulator.")
