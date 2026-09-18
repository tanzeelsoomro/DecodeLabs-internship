def display_header():
    print("Expense Tracker.")

def get_expense():
    while True:
        try:
            expense = float(input("Enter Expense Amount:"))
            
            if expense < 0:
                print("Expense cannot be negative.")
                continue
                
            return expense
            
        except ValueError:
            print("Invalid Input! Enter a Valid Amount.")

def display_summary(expenses, total):
    print("\n Summary.")
    
    if not expenses:
        print("No Expenses Were Entered.")
    else:
        print("Your Expenses:")
        
        for expense in expenses:
            print(f"Expenses: {expense}")
            
        print("-" * 40)
        print("Expense Count:", len(expenses))
        print("Total Spent:", total)
        
        average = total / len(expenses)
        print("Average Expense:", average)
        
    print("Thank You For Using Expense Tracker.")

def main():
    total = 0
    expenses = []
    
    display_header()
    
    while True:
        expense = get_expense()
        
        if expense == 0:
            break
            
        total += expense
        expenses.append(expense)
        
        print("Expense Added:", expense)
        print("Current Total:", total)
        
    display_summary(expenses, total)

main()