# Guidelines: Minimum 12 characters,
# combination of lower/upper characters,
# includes at least one number
# and one special character.
from analyse import length


def getpass():
    sc = 0
    password = str(input("Please enter a password \n"))
    if password == "":
        print("You have not entered a password. Have a think about a safe password and try again.")
    else:
        sc += 1
        length(password, sc)


if __name__ == "__main__":
    getpass()
