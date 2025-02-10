#Expense Pie Chart Project
import matplotlib.pyplot as plt

def main():
      expenses = {}

      while True:
            expenseName = input("Enter the name of the expense (or 'done' to finish): ")
            if expenseName == 'done':
                  break

            expenseAmount = float(input("Enter the amount for "+expenseName+" : "))
            expenses[expenseName] = expenseAmount
      plotExpenses(expenses)

def plotExpenses(expenses):
      labels = list(expenses.keys())
      values = list(expenses.values())

      plt.figure(figsize=(10, 7))
      plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=140)
      plt.axis('equal')
      plt.title("Expense Breakdown")
      plt.show()

if __name__ == '__main__':
      main()