import csv
import pandas as pd
from datetime import datetime, timedelta

def menu():
    print("Expense tracker")
    print("1. Add expense")
    print("2. View expenses")
    print("3. Delete expenses")
    print("4. Show summary")
    print("5. Show insights")
    print("6. Exit")


def add():
    name = input("Product :")
    price = float(input("Price :"))
    category = input("Category :")

    with open("expense.csv", "r") as f:
        reader = csv.reader(f)
        rows = list(reader)
        new_id = len(rows)

        with open("expense.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([new_id, name, price, category, datetime.today().date()])
    print("Expense added")
def view():
    df = pd.read_csv("expense.csv")
    df.columns = ["ID", "Name",  "Price", "Category", "Date"]

    print("1. View all")
    print("2. View by category")
    print("3. View by date")
    choice = int(input("-"))

    if choice == 1:
        for i, row in df.iterrows():
            print(f"ID : {row[0]} | Name: {row[1]} | Price: {row[2]} | Category: {row[3]} | Date: {row[4]}")

    elif choice == 2:
        df = df.sort_values(by=["Category", "Price"])
        for i, row in df.iterrows():
            print(f"ID : {row[0]} | Name: {row[1]} | Price: {row[2]} | Category: {row[3]} | Date: {row[4]}")
    elif choice == 3:
        date_b = int(input("How many weeks?"))
        date_before = datetime.today().date() - timedelta(days=7*date_b)
        found = False
        for i, row in df.iterrows():
            passedDate = datetime.strptime(row[4],'%Y-%m-%d').date()
            if passedDate >= date_before:
                print(f"ID : {row[0]} | Name: {row[1]} | Price: {row[2]} | Category: {row[3]} | Date: {row[4]}")
                found = True
        if not found:
            print(f"No expenses since {date_before}")
    else:
        print("Invalid choice")

def summary():
    df = pd.read_csv("expense.csv", header=None)
    df.columns = ["ID", "Name",  "Price", "Category", "Date"]

    print("1. All")
    print("2. By category")
    print("3. By date")
    choice = int(input("-"))

    if choice == 1:
        total = df["Price"].sum()
        print(f"Total spent - {total}€")
    elif choice == 2:
        by_cat = df.groupby("Category")["Price"].sum().sort_values(ascending=False)
        print(by_cat)
    elif choice == 3:
        by_date = df.groupby("Date")["Price"].sum().sort_index()
        print(by_date)



def delete():
    df = pd.read_csv("expense.csv")
    for i, row in df.iterrows():
        print(f"ID : {row[0]} | Name: {row[1]} | Price: {row[2]} | Category: {row[3]} | Date: {row[4]}")
    index = int(input("Number to delete:"))
    df = df.drop(index)
    df.to_csv("expense.csv", index=False, header=False)
    print("Expense deleted.")

def show():
    df = pd.read_csv("expense.csv")
    df.columns = ["ID", "Name", "Price", "Category", "Date"]
    print("1. Most expensive item")
    print("2. Most expensive category")
    print("3. Average spending")

    choice = int(input("-"))
    if choice == 1:
        most_it = df.sort_values(by="Price", ascending=False).head(1)
        print("Most expensive item : ")
        print(most_it[["Name", "Price", "Category", "Date"]].to_string(index=False))
    elif choice == 2:
        m = df.groupby("Category")["Price"].sum()
        most_cat = m.sort_values(ascending=False).head(1)
        print(f"Most expensive category :")
        print(most_cat.to_string(index=False))
    elif choice == 3:
        avg_expense = df["Price"].mean()
        print(f"Average expense : {avg_expense}€ ")
    else:
        print("Invalid choice")