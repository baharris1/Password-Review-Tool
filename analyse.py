import re


def length(pwd, score):
    x = 12
    num = len(pwd)
    diff = x - num

    if num < 12:
        print(f"Characters: {num}")
        caps(pwd, score)
    else:
        print(f"Characters: {num}")
        score += 1
        caps(pwd, score)


def caps(pwd, score):
    capnum = sum(1 for c in pwd if c.isupper())  # Count number of capital letters

    if capnum == 0:
        print(f"Capital Letters: {capnum}")
        numbers(pwd, score)
    else:
        print(f"Capital Letters: {capnum}")
        score += 1
        numbers(pwd, score)


def numbers(pwd, score):
    num = sum((1 for n in pwd if n.isdigit()))
    if num == 0:
        print(f"Numbers: {num}")
        special(pwd, score)
    else:
        print(f"Numbers: {num}")
        score += 1
        special(pwd, score)


def special(pwd, score):
    char = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    count = sum(1 for c in pwd if char.search(c))
    if count == 0:
        print(f"Special Characters: {count}")
    else:
        print(f"Special Characters: {count}")
        score += 1
    print(f"Password Score: {score}/5")
        if score < 5:
        option = input(
            "Would you like some tips on how to create a stronger password (y/n)?\n"
        )
        option = option.lower()
        if option == 'y':
            tips(pwd)
        else:
            exit()


def tips(pwd):
    if len(pwd) < 12:
        print("Making your password at least 12 characters long would be more secure.")

    capnum = sum(1 for c in pwd if c.isupper())
    if capnum == 0:
        print("Using at least one capital letter would make your password more secure.")

    num = sum((1 for n in pwd if n.isdigit()))
    if num == 0:
        print("Using at least one number would make your password more secure.")

    char = re.compile("[@_!#$%^&*()<>?/\|}{~:]")
    count = sum(1 for c in pwd if char.search(c))
    if count == 0:
        print("Using at least one special character would make your password more secure.")
