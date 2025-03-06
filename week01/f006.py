def main():
    try:
        n = int(input("ใส่เลขแม่สูตรคูณ : "))

        for i in range(0, 12):
            print(f"\n{n} x {i+1} = {n * (i + 1)}")

    except ValueError:
        print("Invalid Input")
