voted = {}


def check_voter(name):
    if voted.get(name):
        print("Kick them out.")
    else:
        voted[name] = True
        print("Let them vote!")


check_voter("Apples")
check_voter("Bananas")
check_voter("Avacados")
print(voted)
