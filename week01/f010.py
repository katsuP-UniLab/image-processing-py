from week01.f009 import mult, subt, summ, divis


def main():
    no1 = int(input("Enter 1st Number : "))
    no2 = int(input("Enter 2nd Number : "))

    print("")
    print("")

    print(summ(no1, no2))
    print(subt(no1, no2))
    print(mult(no1, no2))

    if no2 != 0:
        print(divis(no1, no2))
    else:
        print("divided by 0")
