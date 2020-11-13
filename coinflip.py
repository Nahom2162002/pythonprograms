import random

def main():
    userguess = input("Let's do a coin flip, heads or tails?")
    flip = random.randint(1, 10)
    if flip >= 1 and flip <= 5:
        result = "heads"
    else:
        result = "tails"
    correct = False
    while correct == False:

       if userguess == result:
           correct = True
           print(result)
           print("Good job, you got it")
       else:
           correct = False
           print(result)
           print("Nope, it was ", end = "")
           print(result)

if __name__ == "__main__":
    main()