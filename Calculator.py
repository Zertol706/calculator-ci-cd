def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def main():
    print("Calculator")

    try:
        a = float(input("First number: "))
        operation = input("Operation (+ or -): ")
        b = float(input("Second number: "))

        if operation == "+":
            print("Result:", add(a, b))
        elif operation == "-":
            print("Result:", subtract(a, b))
        else:
            print("Invalid operation")

    except ValueError:
        print("Invalid number")


if __name__ == "__main__":
    main()
   