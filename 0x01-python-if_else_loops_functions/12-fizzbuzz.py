#!/usr/bin/python3
def fizzbuzz():
    for i in range (0, 100):
        if (i % 15):
            print("FizzBuzz ")
        else:
            if (i % 3):
                print("Fizz ")
        else:
            if (i % 5):
                print("Buzz ")
        else:
            print(i," ")
