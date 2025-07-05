import csv
import pandas as pd
import matplotlib as plt
class Items:

    all = []

    def __init__(self, name : str, quantity : int):
        self.name = name
        self.quantity = quantity

        Items.all.append(self)

    @classmethod
    def writecsv(cls):
        name = input("Enter product: ")
        quantity = input("Enter quantity: ")

        if(name !="x" or quantity != "x"):
            while(name !="x" or quantity != "x"):
                with open('products.csv', 'a') as f:
                    writer = csv.writer(f)
                    writer.writerow([name, quantity])

                name = input("Enter product: ")
                quantity = input("Enter quantity: ")





    @classmethod
    def opencsv(cls):
        with open('products.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

            x = []
            y = []

            plots = csv.reader(f, delimiter = ",")

            for row in plots:
                x.append(row[0])
                y.append(row[1])
        plt.bar(x,y, color = "r", width = 0.72, label = "price")
        plt.xlabel("product")
        plt.ylabel("price")
        plt.title("Shopping")
        plt.legend()
        plt.show()
        for item in items:
            print(item)


    @classmethod
    def deletecsv(cls):
        delete = input("Name of product to delete: ")
        try:
            # Load the CSV file, specifying encoding
            df = pd.read_csv('products.csv', encoding='ISO-8859-1')  # Adjust encoding if needed

            # Filter out the row with the name to delete
            df = df[df['name'] != delete]

            # Save the updated DataFrame back to the CSV
            df.to_csv('products.csv', index=False, encoding='ISO-8859-1')
            print(f"Product '{delete}' deleted successfully!")
        except FileNotFoundError:
            print("Error: The file 'products.csv' does not exist.")
        except KeyError:
            print("Error: The CSV file does not contain a 'name' column.")
        except UnicodeDecodeError as e:
            print(f"Error decoding the file: {e}")


Items.writecsv()
Items.opencsv()
Items.deletecsv()
Items.opencsv()
