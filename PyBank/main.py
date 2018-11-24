import os
import csv

budget_csv = os.path.join('..', 'Resources', 'budget_data.csv')

total_months = []
total_profit = []
monthly_change = []

with open(budget_csv, newline="", encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    for row in csvreader:
        total_months.append(row[0])
        total_profit.append(int(row[1]))

    for i in range(len(total_profit)-1):
        monthly_change.append(total_profit[i+1]-total_profit[i])

    max_profit_increase = max(monthly_change)
    max_profit_decrease = min(monthly_change)

    max_month_increase = monthly_change.index(max(monthly_change)) + 1
    max_month_decrease = monthly_change.index(min(monthly_change)) + 1

    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {len(total_months)}")
    print(f"Total: ${sum(total_profit)}")
    print(f"Average Monthly Change: ${round(sum(monthly_change)/len(monthly_change),2)}")
    print(f"Greatest Increase in Profits: {total_months[max_month_increase]} (${str(max_profit_increase)})")
    print(f"Greatest Decrease in Profits: {total_months[max_month_decrease]} (${str(max_profit_decrease)})")

    output_csv = os.path.join("budget_file.csv")

    with open(output_csv, 'w') as file:
        file.write("Financial Analysis\n")
        file.write("----------------------------\n")
        file.write(f"Total Months: {len(total_months)}\n")
        file.write(f"Total: ${sum(total_profit)}\n")
        file.write(f"Average Monthly Change: ${round(sum(monthly_change)/len(monthly_change),2)}\n")
        file.write(f"Greatest Increase in Profits: {total_months[max_month_increase]} (${str(max_profit_increase)})\n")
        file.write(f"Greatest Decrease in Profits: {total_months[max_month_decrease]} (${str(max_profit_decrease)})\n")
