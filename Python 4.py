expenses = []

def add_expense():
    name = input("Enter Expense: ")
    while True:
        try:
            amount = float(input("Amount: ₹"))
            if amount <= 0:
                print("Amount should be positive.")
            else:
                expenses.append({"name": name, "amount": amount})
                print("Expense Added Successfully!")
                break
        except ValueError:
            print("Invalid amount. Please enter a number.")

def view_expenses():
    if not expenses:
        print("No expenses recorded yet.")
    else:
        print("Expenses:")
        for i, e in enumerate(expenses, start=1):
            print(f"{i}. {e['name']}: ₹{e['amount']}")

def calculate_total():
    total = sum(e['amount'] for e in expenses)
    print(f"Total Expenses: ₹{total:.2f}")

def delete_expense():
    view_expenses()
    if expenses:
        try:
            choice = int(input("Enter expense number to delete: ")) - 1
            if 0 <= choice < len(expenses):
                del expenses[choice]
                print("Expense deleted.")
            else:
                print("Invalid choice.")
        except ValueError:
            print("Invalid input.")

def main():
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Spending")
        print("4. Delete Expense")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            calculate_total()
        elif choice == '4':
            delete_expense()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()