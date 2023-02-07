import random

def main():
    x = input("I'm thinking of a number between 1 - 10, can you guess it?")
    num = random.randint(1, 10)
    if x == num:
       print(num)
       print("Good job, you got it")
    else:
       print(num)
       print("Nope")

if __name__ == "__main__":
    main()
