import random
import string
import secrets
def Generator(passwordLength):
    # input validation
    if passwordLength < 0:
        print("Password length should be a non-zero positive number")
    # necessary data
    lower_caseAlphabets= string.ascii_lowercase
    upper_caseAlphabets= string.ascii_uppercase
    numericalData= string.digits
    specialCharacters= string.punctuation
    # options for users
    userChoice= int(input("1. Weak Password(Only Lowercase)\n2. Medium Password(Lowercase, Uppercase, and Digits)\n3. Strong Password(Lowercase, Uppercase, Digits, and Special Characters)\n"))
    if userChoice == 1:
        userPassword= ""
        for iter in range(passwordLength): # generate password of desired length with all lowercase letters
            userPassword+= ''.join(secrets.choice(lower_caseAlphabets))
        print("Password:",userPassword)
    elif userChoice == 2:
        userPassword= ""
        for iter in range(passwordLength): # generate password of desired length with lower, upper case letters and digits
            userPassword+= ''.join(secrets.choice(lower_caseAlphabets + upper_caseAlphabets + numericalData))
        print("Password:",userPassword)
    elif userChoice == 3:
        userPassword= ""
        for iter in range(passwordLength): # generate password of desired length with lower, upper case letters,digits and special characters
            userPassword+= ''.join(secrets.choice(lower_caseAlphabets + upper_caseAlphabets + numericalData + specialCharacters))
        print("Password:",userPassword)
def main():
    print("Automated Password Generator\n---------------------------")
    inputLength= int(input("Please enter password length: "))
    Generator(inputLength)
if __name__ == "__main__":
    main()