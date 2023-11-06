"""
### Usage
tracker.py addExpense {Date} {Value}
    ex: tracker addExpense 31/08/1999 -14.55
    ex: tracker addExpense 24/07/2022 55.00
tracker.py addCategory={Wanted Category}
    ex: tracker addCategory PIX
tracker.py delExpense {Number ID}
    ex: tracker delExpense 2
tracker.py delCategory {Number ID}
    ex: tracker delCategory 2
tracker.py displayBalance
tracker.py displayExpense
"""

from rich.console import Console
from rich.table import Table
import sys
import trackerDB

def getBalance():
    return trackerDB.selectAll("balance")[0][0]

def addExpense(date, category, value):
    balance = getBalance() + float(value)
       
    trackerDB.updateBalance(balance)
    
    obj = {
        "date": date,
        "category": category,
        "value": value,
        "balance": balance,
    }
    trackerDB.insertInTracker(obj)

def getCategory(number):
    category = trackerDB.selectAll("category")[number - 1][1]
    return category
def getCategoryDisplay():
    categoryStr = ""
    categoryList = trackerDB.selectAll("category")
    for i in range(0, len(categoryList)):
        categoryStr += f"{i + 1} - {categoryList[i][1]}\n"
    return categoryStr



args = sys.argv[1:]

if args[0] == "addExpense":
    categoryDisplay = getCategoryDisplay()
    categoryNum = input(f"Select the category \n\n{categoryDisplay}\n->")

    category = trackerDB.selectAll("category")[int(categoryNum) - 1][1]

    addExpense(args[1], category, args[2])
elif args[0] == "addCategory":
    try:
        trackerDB.insertCategory(args[1])
    except IndexError as e:
        print("You need to type the name of the category")
        sys.exit()
elif args[0] == "delExpense":
    expenseLen = len(trackerDB.selectAll("tracker"))
    if int(args[1]) <= 0 or int(args[1]) > expenseLen:
        print("This expense don\'t exist ")
        sys.exit()
    trackerDB.deleteRow("tracker", args[1])
elif args[0] == "delCategory":
    categoryLen = len(trackerDB.selectAll("category"))
    if int(args[1]) <= 0 or int(args[1]) > categoryLen:
        print("This category don\'t exist ")
        sys.exit()
    trackerDB.deleteRow("category", args[1])
elif args[0] == "displayBalance":
    print(trackerDB.selectAll('balance')[0][0])
elif args[0] == "displayExpense":
    trackerList = trackerDB.selectAll('tracker')
    table = Table(title="Expense Tracker")
    headers = ["id", "date", "category", "value", "balance"]

    for header in headers:
        table.add_column(header, style="magenta")

    for row in trackerList:
        idTracker, date, category, value, balance = row
        table.add_row(str(idTracker), date, category, str(value), str(balance))
    console = Console()
    console.print(table)
else:
    print("Invalid command!")
    print("You can use only this options: addCategory, delExpense, delCategory, displayBalance and displayExpense")