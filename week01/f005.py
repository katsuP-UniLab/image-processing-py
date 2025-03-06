def main():
    total = 0

    while True:
        try:
            inp = int(input("Enter a number (Enter 0 to exit) : "))

            if inp == 0:
                break

            total += inp
        except ValueError:
            print("The input is not a number! Try again..")

    print(f"The total of value is {total}")
