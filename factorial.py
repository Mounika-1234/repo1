def factorial(number):
    print("to find")
    print("To find factorial of a number")
    if number < 0:
        print('Invalid entry! Cannot find factorial of a negative number')
    if number == 0 or number == 1:
        return 1
    else:
        return number * factorial(number - 1)

if __name__ == '__main__':
    userInput = int(input('Enter the Number to find the factorial of: '))
    print(factorial(userInput))
