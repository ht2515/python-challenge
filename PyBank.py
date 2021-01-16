import pandas as pd 
import os

data = pd.read_csv(r'C:\Users\Dan\Desktop\Upenn Data\Python\HW\03-Python_Homework_Instructions_PyBank_Resources_budget_data.csv')
data.dropna(inplace = True)

total_months = data['Date'].count()
total = data['Profit/Losses'].sum()

data['shifted Profit/Losses'] = data['Profit/Losses'].shift(1)
data['difference'] = data['Profit/Losses'] - data['shifted Profit/Losses']
change_total = data['difference'].sum()
avg_change = change_total/(total_months - 1)

ls_max = data.loc[data['difference'].idxmax()]
ls_min = data.loc[data['difference'].idxmin()]

print('Financial Analysis')
print('---------------------------')
print(f'Total Months: {total_months}\nTotal: ${total}\nAverage Change: ${round(avg_change,2)}')
print(f'Greatest Increase in Profits: {ls_max[0]} (${int(ls_max[-1])})')
print(f'Greatest Decrease in Profits: {ls_min[0]} (${int(ls_min[-1])})')




