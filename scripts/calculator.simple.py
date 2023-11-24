#Loop Function
while True:
    # Starting information
    print("Welcome to this simple calculator with simple functions, these include:")
    print("• Addition (a)")
    print("• Subtraction (s)")
    print("• Multiplication (m)")
    print("• Division (d)")
    print("• Exit (e)")

    # Input
    Symbol = input('What Symbol do you want to pick?: ').lower()

    # Choosing Symbols
    if Symbol == 'a':
        Verification_Addition = input('Are you sure? Y/N: ')
        if Verification_Addition.lower() == 'y':
            print('Ok!')
        else:
           exit()
    elif Symbol == 's':
        Verification_Subtraction = input('Are you sure? Y/N: ')
        if Verification_Subtraction.lower() == 'y':
            print('Ok!')
        else:
            exit()
    elif Symbol == 'm':
        Verification_Subtraction = input('Are you sure? Y/N: ')
        if Verification_Subtraction.lower() == 'y':
            print('Ok!')
        else:
            exit()
    elif Symbol == 'd':
        Verification_Subtraction = input('Are you sure? Y/N: ')
        if Verification_Subtraction.lower() == 'y':
            print('Ok!')
        else:
            exit()
    elif Symbol == 'e':
        exit('Exiting the Calculator')



    # Initilising Numbers
    Num1 = None
    Num2 = None

    # Input of Numbers
    while True:
        while True:
            if Symbol == 'a':
                try:
                    Num1 = float(input('What would you like your first number to be?: '))
                    break
                except ValueError:
                    print('Syntax Error... Enter a real number')
            elif Symbol == 's':
                    try:
                        Num1 = float(input('What would you like your first number to be?: '))
                        break
                    except ValueError:
                        print('Syntax Error... Enter a real number')
            elif Symbol == 'm':
                try:
                    Num1 = float(input('What would you like your first number to be?: '))
                    break
                except ValueError:
                    print('Syntax Error... Enter a real number')
            elif Symbol == 'd':
                try:
                    Num1 = float(input('What would you like your first number to be?: '))
                    break
                except ValueError:
                        print('Syntax Error... Enter a real number')
        while True:
            if Symbol =='a':
                try:
                    Num2 = float(input('What would you like you second number to be?: '))
                    break
                except ValueError:
                    print('Syntax Error... Enter a number')
            elif Symbol =='s':
                try:
                    Num2 = float(input('What would you like you second number to be?: '))
                    break
                except ValueError:
                    print('Syntax Error... Enter a number')
            elif Symbol =='m':
                try:
                    Num2 = float(input('What would you like you second number to be?: '))
                    break
                except ValueError:
                    print('Syntax Error... Enter a number')
            elif Symbol == 'd':
                try:
                    Num2 = float(input('What would you like your second number to be?: '))
                    break
                except ValueError:
                    print('Syntax Error... Enter a real number')
    
        # Showcase
        if Symbol == 'a':        
            print('This is what your expression looks like so far ' + str(Num1) + ' + ' + str(Num2))
        elif Symbol == 's':
            print('This is what your expression looks like so far ' + str(Num1) + ' - ' + str(Num2))
        elif Symbol == 'm':
            print('This is what your expression looks like so far ' + str(Num1) + ' x ' + str(Num2))
        elif Symbol == 'd':
            print('This is what your expression looks like so far ' + str(Num1) + ' / ' + str(Num2))
    
        Verification = input('Are you sure you want this? Y/N: ')
        if Verification.lower() == 'y':
            
                # Final Output
                if Symbol == 'a':
                    print('Your Answer is ' + str(Num1 + Num2))
                    break
                elif Symbol == 's':
                    print('Your Answer is ' + str(Num1 - Num2))
                    break
                elif Symbol == 'm':
                    print('Your Answer is ' + str(Num1 * Num2))
                    break
                elif Symbol == 'd':
                    print('Your Answer is ' + str(Num1 / Num2))
                    break