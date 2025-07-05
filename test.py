import csv
import pandas as pd
from datetime import datetime

class Expenses:
    def __init__(self):
        self.expenses = []

    def add(self):
        name = input("Name: ")
        price = float(input("Price: "))
        category = input("Category: ")
        date = input("Date (YYYY-MM-DD): ")
        if date == "today":
            date = datetime.today()
        # Append the expense as a dictionary
        self.expenses.append({"Name": name, "Price": price, "Category": category, "Date": date})
        print("Expense added successfully!")

    def view(self):
        if not self.expenses:
            print("No expenses to display.")
        else:
            print("All Expenses:")
            for expense in self.expenses:
                print(expense)

    def delete(self):
        name = input("Enter the name of the expense to delete: ")
        for expense in self.expenses:
            if expense["Name"] == name:
                self.expenses.remove(expense)
                print("Expense deleted successfully!")
                return
        print("Expense not found.")

    def summary(self):
        if not self.expenses:
            print("No expenses to summarize.")
        else:
            total = sum(expense["Price"] for expense in self.expenses)
            print(f"Total expenses: {total}")

    def menu(self):
        while True:
            print("*******************")
            print(" Shopping expenses")
            print("*******************\n\n")
            print("1. Add expense")
            print("2. View all expenses")
            print("3. Delete an expense")
            print("4. Show summary")
            print("5. Exit")
            try:
                pick = int(input("Choose an option: "))
                if pick == 1:
                    self.add()
                elif pick == 2:
                    self.view()
                elif pick == 3:
                    self.delete()
                elif pick == 4:
                    self.summary()
                elif pick == 5:
                    print("Exiting...")
                    break
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

# Main program
if __name__ == "__main__":
    app = Expenses()
    app.menu()

