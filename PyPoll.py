import pandas as pd 
import csv
import collections

data = pd.read_csv(r'C:\Users\Dan\Desktop\Upenn Data\Python\HW\03-Python_Homework_Instructions_PyPoll_Resources_election_data.csv')
data.dropna(inplace = True)

total_voters = data['Voter ID'].count()

Khan = 0
Correy = 0
Li = 0
O = 0
for name in data['Candidate']:
    if name == 'Khan':
        Khan += 1
    elif name == 'Correy':
        Correy += 1
    elif name == 'Li':
        Li += 1 
    elif name == "O'Tooley":
        O += 1
def percentage(a, b):
    return format(a / b * 100, '.3f')
percentage_K = f'{percentage(Khan,total_voters)}%'
percentage_C = f'{percentage(Correy,total_voters)}%'
percentage_L = f'{percentage(Li,total_voters)}%'
percentage_O = f'{percentage(O,total_voters)}%'

x=None
lst = [Khan,'Khan',Correy,'Correy',Li,'Li',O,'O']
winner = max(Khan,Correy,Li,O)
for i in range (0,len(lst)):
    if winner == lst[i]:
        x = lst[i+1]
        i += 2

print(f'Election Results\n---------------\nTotal Votes: {total_voters}\n---------------')
print(f'Khan: {percentage_K} ({Khan})')
print(f'Correy: {percentage_C} ({Correy})')
print(f'Li: {percentage_L} ({Li})')
print(f"O'Tooley: {percentage_O} ({O})")
print(f'---------------\nWinner: {x}\n---------------')



