def ex04():
    while True:
        inp = int(input("Enter a number (even to display, odd to exit) : "))

        if inp % 2 > 0:
            print("Odd number is entered.. Program exited..")
            break
        else:
            print(f"input number is {inp}")
            print("")
