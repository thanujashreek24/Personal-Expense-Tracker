import csv
import os

Data="tracker.csv"

def openfile():
    if not os.path.exists(Data):
        with open(Data,mode='w',newline="") as file:
            writer=csv.DictWriter(file,fieldnames=["Date","Amount","Category","Description"])
            writer.writeheader()

def add_expense():
    date=input("Enter the date (YYYY-MM-DD):")
    amount=int(input("Enter the amount:"))
    category=input("Enter the category(e.g ,Food,Bills,Transport,Utilities):")
    description=input("Enter the description of expense spent:")

    with open(Data,mode='a',newline="")as file:
        writer=csv.DictWriter(file,fieldnames=["Date","Amount","Category","Description"])
        writer.writerow({"Date":date,"Amount":amount,"Category":category,"Description":description})
    print(f"Expense on {date} added successfully!!!!!")


def view_expenses():
    with open(Data,mode='r')as file:
        reader=csv.DictReader(file)
        expense=list(reader)
        if expense:
            for row in expense:
                print(row)
        else:
            print("No expenses added yet...")

             
def update_expense():
    view_expenses()
    date=input("Enter the date to be updated (YYYY-MM-DD):")
    updated=[]
    found=False

    with open(Data,mode='r')as file:
        reader=csv.DictReader(file)
        for row in reader:
            if row["Date"]==date:
                found=True
                row["Amount"]=int(input("Enter the amount :"))
                row["Category"]=input("Enter the category :")
                row["Description"]=input("Enter the description :")
            updated.append(row)
    if found:
        with open(Data,mode='w',newline="")as file:
            writer=csv.DictWriter(file,fieldnames=["Date","Amount","Category","Description"])
            writer.writeheader()
            writer.writerows(updated)
        print(f"Expense on date {date} updated Successfully")
    else:
        print("Expense not found")


def delete_expense():
    view_expenses()
    date=input("Enter the date for expense to be deleted (YYYY-MM-DD):")
    found=False
    deleted=[]
    with open(Data,mode="r")as file:
        reader=csv.DictReader(file)
        for row in reader:
            if row["Date"]==date:
                found =True
                continue
            deleted.append(row)
    if found:
        with open(Data,mode='w',newline='')as file:
            writer=csv.DictWriter(file,fieldnames=["Date","Amount","Category","Description"])
            writer.writeheader()
            writer.writerows(deleted)
        print(f"Expense on {date}is deleted successfully")
    else:
        print("Expense not found")
    

def generate_summary():
    category_totals = {}
    target_date = input("Enter the date (YYYY-MM-DD) to summarize expenses: ")
    
    with open(Data, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["Date"] == target_date:  
                category = row["Category"]
                amount = float(row["Amount"])
                category_totals[category] = category_totals.get(category, 0) + amount
    
    if category_totals:
        print(f"\nExpense Summary for {target_date}:")
        for category, total in category_totals.items():
            print(f"{category}: Rupees {total:.2f}")
    else:
        print(f"No expenses recorded for {target_date}.")

def main():
    openfile()
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Update Expense")
        print("4. Delete Expense")
        print("5. Generate Summary")
        print("6. Exit")

        choice =input("enter the choice")
        if choice=="1":
            add_expense()
        elif choice=="2":
            view_expenses()
        elif choice=="3":
            update_expense()
        elif choice =="4":
            delete_expense()
        elif choice=="5":
            generate_summary()
        elif choice=="6":
            print("Goodbye!!")
            break
        else:
            print("invalid choice")

if __name__ == "__main__":
    main()
        




    




    


