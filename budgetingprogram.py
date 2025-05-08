import matplotlib.pyplot as plt

def menu():
    print("Budgeting Program")
    print("------------------")

    expenses = {}

    while True:
        category = input("Input a new expense category or type DONE: ")
        if category.upper() == "DONE":
            break

        while True:
            try:
                cost = int(input(f"Input the cost of '{category}': "))
                if cost < 0:
                    print("Please enter a non-negative number.")
                    continue
                break
            except ValueError:
                print("Please enter a valid whole dollar amount.")

        if category in expenses:
            expenses[category] += cost
        else:
            expenses[category] = cost

    if not expenses:
        print("No expenses entered.")
        return

    categories = list(expenses.keys())
    costs = list(expenses.values())

    plt.pie(costs, labels=categories, autopct="%1.1f%%")
    plt.title("Budgeting Program")
    plt.show()
    
menu()
