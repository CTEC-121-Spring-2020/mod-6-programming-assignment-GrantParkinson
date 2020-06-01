# Module 7
#   Programming Assignment 10
#     Prob-3.py

# <Grant Parkinson>


def main():
    # your code here
    sum = 0
    # do not change the while loop definition below
    while True:
        x = float(input('Enter a Number (negative to quit): '))
        if x >= 0:
            sum = sum + x
        else:
            break
    print('The sum is', sum)


main()
