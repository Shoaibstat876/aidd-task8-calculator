def get_number(label: str) -> float:
    """Ask the user for a number and convert it to float."""
    try:
        value = float(input(f"Enter {label} number: "))
        return value
    except ValueError:
        print("Error: Please enter a valid numeric value.")
        raise SystemExit(1)


def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float:
    if b == 0:
        print("Error: Cannot divide by zero.")
        raise SystemExit(1)
    return a / b


def main() -> None:
    print("=== Spec-Driven Python CLI Calculator ===")

    # Step 1: Read inputs
    num1 = get_number("the first")
    num2 = get_number("the second")

    # Step 2: Show menu
    print("\nChoose operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    choice = input("Enter choice (1/2/3/4): ").strip()

    # Step 3: Map choice to operation
    if choice == "1":
        operator = "+"
        result = add(num1, num2)
    elif choice == "2":
        operator = "-"
        result = subtract(num1, num2)
    elif choice == "3":
        operator = "*"
        result = multiply(num1, num2)
    elif choice == "4":
        operator = "/"
        result = divide(num1, num2)
    else:
        print("Error: Invalid operation choice.")
        raise SystemExit(1)

    # Step 4: Show result
    print(f"\nResult: {num1} {operator} {num2} = {result}")
    print("\nThank you for using the Spec-Driven Calculator!")


if __name__ == "__main__":
    main()
