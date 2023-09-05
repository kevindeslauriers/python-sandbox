from prettytable import PrettyTable

table = PrettyTable(["Name", "Age", "City"])

table.add_row(["Alice", 30, "New York"])
table.add_row(["Bob", 25, "Los Angeles"])
table.add_row(["Charlie", 35, "Chicago"])

print(table)

print()

#using pandas - has row numbers
import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [30, 25, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}

df = pd.DataFrame(data)

# Print the DataFrame
print(df)