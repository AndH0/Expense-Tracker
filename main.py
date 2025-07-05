import csv
import pandas as pd
from datetime import datetime
import logging

logging.basicConfig(level=logging.INFO, filename="log.log", filemode="w", format="%(asctime)s - %(levelname) - %(message)s")

logger = logging.getLogger("To-Do")
handler = logging.FileHandler("log.loger")
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)

logger.addHandler(handler)

def show_menu():
    print("==========")
    print("To-Do list")
    print("==========")
    print("\n1. Add task"
          "\n2. View tasks"
          "\n3. Mark as done"
          "\n4. Delete task"
          "\n5. Edit task"
          "\n6. Exit")

def add():
    task = input("Task : ")
    datum = input("Due date (YYYY-MM-DD: ")
    priority = input("Priority low/medium/high: ").lower()
    datetime.strptime(datum, "%Y-%m-%d")

    with open("task.csv", "r") as f:
        reader = csv.reader(f)
        rows = list(reader)
        new_id = len(rows)
        with open("task.csv","a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([new_id,datetime.strptime(datum,"%Y-%m-%d").date(), task, "Incomplete", priority])


    print("Task added")

def view():
    print("1. Show all"
          "\n2. Show overdue"
          "\n3. Show not completed")
    choice = int(input())
    logger.info("User checking tasks")

    with open("task.csv", "r") as file:
        try:
            df = pd.read_csv("task.csv", header=None)
            df.columns = ["ID", "Due", "Task", "Status", "Priority"]
            if choice == 1:
                # Sort by priority
                priority_map = {"high": 0, "medium": 1, "low": 2}
                df["priority_sort"] = df["Priority"].map(priority_map)
                df = df.sort_values(by="priority_sort")

                print("\nYour tasks:")
                for i, row in df.iterrows():
                    print(f"ID: {row[0]} | Due: {row[1]} | Task: {row[2]} | Status: {row[3]} | Priority: {row[4]}")

            elif choice == 2:
                today = datetime.today().date()
                df["Due"] = pd.to_datetime(df["Due"]).dt.date
                df = df[(df["Due"] < today) & (df["Status"].str.lower() != "finished")]
                print("\nYour tasks:")
                for i, row in df.iterrows():
                    print(f"ID: {row[0]} | Due: {row[1]} | Task: {row[2]} | Status: {row[3]} | Priority: {row[4]}")
            elif choice == 3:
                df = df[df["Status"].str.lower() != "finished"]
                print("\nYour tasks:")
                for i, row in df.iterrows():
                    print(f"ID: {row[0]} | Due: {row[1]} | Task: {row[2]} | Status: {row[3]} | Priority: {row[4]}")
            st = df["Status"].value_counts()
            pr = df["Priority"].value_counts()
            num = sum(1 for line in file)
            print(st)
            print(pr)
            print(f"Number of tasks : {num}")
        except FileNotFoundError:
            print("task.csv not found.")


def mark():
    # Read the CSV with no headers
    df = pd.read_csv("task.csv", header=None, index_col=False)

    # Display tasks with index numbers
    print("Your tasks:")
    for i, row in df.iterrows():
        print(f"{i}. Due : {row[1]} - {row[2]} - Status: {row[3]}")

    # Ask user which task to mark as finished
    task_index = int(input("Enter the number of the task you've completed: "))

    # Update the status
    df.at[task_index, 3] = "finished"

    # Save back to CSV
    df.to_csv("task.csv", header=False, index=False)

    print("Task marked as finished!")

def delete():
    df = pd.read_csv("task.csv", header=None)

    # Display all tasks with row numbers
    for i, row in df.iterrows():
        print(f"{i}. Due: {row[1]} - Task: {row[2]} - Status: {row[3]}")

    index = int(input("Enter the number of the task to delete: "))
    df = df.drop(index)  # Drop by row number

    df.to_csv("task.csv", index=False, header=False)
    print("Task deleted.")

def edit():
    df = pd.read_csv("task.csv", header=None, index_col=False)
    #df.columns = ["ID", "Due", "Task", "Status", "Priority"]
    for i, row in df.iterrows():
        print(f"{i}. Due: {row[1]} - Task: {row[2]} - Status: {row[3]}")

    num = int(input("ID of the task:"))
    group = input("Do you want to change - Task/Status/Due/Priority : ")
    change = input("Change to :")

    if group == "Due":
        group = 1
    elif group == "Task":
        group = 2
    elif group == "Status":
        group = 3
    elif group == "Priority":
        group = 4
    # Update the status
    df.at[num, group] = change
    df.to_csv("task.csv", index=False, header=False)
    print("Task updated")


while True:
    show_menu()

    choice = int(input(">"))

    if choice == 1:
        add()
    elif choice == 2:
        view()
    elif choice == 3:
        mark()
    elif choice == 4:
        delete()
    elif choice == 5:
        edit()
    elif choice == 6:
        print("Bye!")
        break
    else:
        print("Invalid choice")
