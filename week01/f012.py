from week01.f011 import mult_table


def main():
    while True:
        try:
            n = int(input("ใส่เลขแม่สูตรคูณ : "))

            if n == 0:
                print("end of program")
                break
            else:
                mult_table(n)

        except ValueError:
            print("Invalid input.. Try again.")
        except TypeError:
            print("TypeError")
