import json  # Importing JSON library to handle reading and writing data in JSON format


def add_expense(expenses, description, amount):
    """Adds a new expense entry to the expenses list."""
    expenses.append({"description": description, "amount": amount})
    print(f"Expense '{description}' of amount {amount} added.")


def get_total_expenses(expenses):
    """Calculates the total amount spent based on all recorded expenses."""
    return sum(expense['amount'] for expense in expenses)


def get_balance(budget, expenses):
    """Calculates the remaining budget after subtracting total expenses."""
    return budget - get_total_expenses(expenses)


def show_budget_details(budget, expenses):
    """Displays the total budget, all recorded expenses, total spent, and remaining balance."""
    print(f"\nTotal Budget: {budget}")
    print("Expenses:")
    for expense in expenses:
        print(f" - {expense['description']}: {expense['amount']}")
    total_expenses = get_total_expenses(expenses)
    print(f"Total Expenses: {total_expenses}")
    print(f"Remaining Budget: {get_balance(budget, expenses)}")


def save_budget_data(filepath, initial_budget, expenses):
    """Saves the initial budget and expenses into a JSON file for future reference."""
    data = {
        "initial_budget": initial_budget,
        "expenses": expenses,
    }
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)


def main():
    """Main function to run the Budget Tracking System."""
    print("Welcome to the Budget Tracking System")
    # Ask user for initial budget
    initial_budget = float(input("Enter the initial budget: "))
    budget = initial_budget
    expenses = []  # Initialize an empty list to store expenses

    # Main loop for user interaction
    while True:
        print("\nMenu:")
        print("1. Add an expense")
        print("2. View expenses")
        print("3. Exit")
        choice = input("Enter your choice (1, 2, 3): ")

        if choice == '1':
            # Add a new expense
            description = input("Enter expense description: ")
            amount = float(input("Enter the amount: "))
            add_expense(expenses, description, amount)

        elif choice == '2':
            # Show current budget details and list of expenses
            show_budget_details(budget, expenses)

        elif choice == '3':
            # Exit the program
            print("Exiting the program. Goodbye!")
            break

        else:
            # Handle invalid user input
            print("Invalid choice. Please try again.")


# Run the main function if this script is executed
if __name__ == "__main__":
    main()
