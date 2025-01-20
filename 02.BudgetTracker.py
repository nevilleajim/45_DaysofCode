# A budget tracker is a tool that helps you manage you finances by tracking your income and expenses
def main():
      print("-------------BUDGET TRACKER------------")
      income = float(input("Enter your total income: "))
      expenses = {}

      while True:
            expenseName = input("Enter your expense name (or 'done' to finish): ")

            if expenseName.lower() == 'done':
                  break

            expenseAmount = float(input("Enter amount for "+ expenseName + " : "))
            expenses[expenseName] = expenseAmount

      # Calculating total expenses, surplus and deficit
      totalExpenses = sum(expenses.values())
      surplus_or_dificit = income - totalExpenses

      print("\n Budget Summary")
      print("------------------")
      print("Total income: $"+str(round(income, 2)))
      print("Totsl Expense: $"+str(round(totalExpenses, 2)))
      print("\nExpenses Breakdown") 

      for name, amount in expenses.items():
            print(" "+name+" :$"+str(amount))
      
      print("Surplus/Deficit: $"+str(round(surplus_or_dificit, 2)))

if __name__ == "__main__":
      main()