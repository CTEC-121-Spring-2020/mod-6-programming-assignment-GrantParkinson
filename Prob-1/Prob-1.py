# Module 7
#   Programming Assignment 10
#     Prob-1.py

# <Grant Parkinson>


def main():
    sum = 0.0
    count = 0
    x = float(input('Enter a Number (negative to quit): '))
    while x >= 0:
        sum = sum + x
        count = count + 1
        x = float(input('Enter a Number (negative to quit): '))
    print('\n The sum of the numbers is', sum)


main()
