password = input('Enter valid password ')
hasDigit = False
hasLetter = False
hasSpecialChar = False
if len(password) == 8:
    for letter in password:
        if letter.isdigit():
            hasDigit = True
        if letter == '#' or letter == '@' or letter == '$' or letter == '%':
            hasSpecialChar = True
        if letter.isalpha():
            hasLetter = True
    if hasDigit == False or hasLetter == False or hasSpecialChar == False:
        print("Wrong password. include alpha, digit and special character")
    else:
        print("Accecptable")
else:
    print("Wrong password. Length should be 8")