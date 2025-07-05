import csv
import pandas as pd
from datetime import datetime

def show_menu():
    print("\n===To-Do List===")
    print("1. Add task")
    print("2. Show tasks")
    print("3. Mark as completed")
    print("4. Delete task")
    print("5. Exit")

def add():
    task = input("Task:")
    datum = input("Enter due date (YYYY-MM-DD): ")
    datetime.strptime(datum,"%Y-%m-%d")
    finished = False


    with open("todo.csv","a",newline="") as file:
        writer = csv.writer(file)
        writer.writerow([datetime.strptime(datum,"%Y-%m-%d").date(), task, "false" ])

    print("Task added")

def show():
    with open("todo.csv", "r") as file:
        reader = csv.reader(file)
        print("\nYour tasks:")


        for row in reader:
            # Load CSV
            df = pd.read_csv("todo.csv", header=None)

            # Convert column 0 to datetime
            df[0] = pd.to_datetime(df[0], format='mixed', dayfirst=False, errors='coerce')


            # Sort by date (ascending = from earliest to latest)
            df = df.sort_values(by=0)
            print((f"Due : {row[0]} | Task : {row[1]} | Completed : {row[2]}" ))

def mark():
    # Read the CSV with no headers
    df = pd.read_csv("todo.csv", header=None)

    # Display tasks with index numbers
    print("Your tasks:")
    for i, row in df.iterrows():
        print(f"{i}. Due : {row[0]} - {row[1]} - Status: {row[2]}")

    # Ask user which task to mark as finished
    task_index = int(input("Enter the number of the task you've completed: "))

    # Update the status
    df.at[task_index, 2] = "finished"

    # Save back to CSV
    df.to_csv("todo.csv", header=False, index=False)

    print("Task marked as finished!")

def delete():
    delete = input("Name of task to delete: ")
    try:
        data = pd.read_csv("todo.csv", header=None)
        data = data[data[1] != delete]
        data.to_csv("todo.csv", index=False, header=False)
        print(f"Task '{delete}' was deleted from the list.")

    except FileNotFoundError:
        print("Error: The file 'expense.csv' does not exist.")
    except UnicodeDecodeError as e:
        print(f"Error decoding the file: {e}")


def overdue():
    today = datetime.today().date()
    with open("todo.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            due_date = datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S").date()
            if due_date < today:
                print((f"Due : {row[0]} | Task : {row[1]} | Completed : {row[2]}"))

while True:
    show_menu()
    choice = input("Choice :")

    if choice == "1":
        add()
    elif choice == "2":
        show()
    elif choice == "3":
        mark()
    elif choice == "4":
        delete()
    elif choice == "5":
        overdue()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice")