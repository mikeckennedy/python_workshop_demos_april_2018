def divide(num, dem):
    if num > 100000000:
        raise Exception("Too big number")

    return num / dem


def main():
    done = False
    while not done:
        try:
            n = int(input("What is the numerator? "))
            d = int(input("What is the denominator? "))

            print(divide(n, d))
            done=True
        except ZeroDivisionError:
            print("Oh, can't divide by zero")
            print("Try again")
        except Exception as x:
            print(f"Whoa, that didn't work: {x}")
            print("Try again")



main()
