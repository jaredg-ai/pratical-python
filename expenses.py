expenses = [10.50, 8, 5, 15, 20, 5, 3]
sum = 0

for x in expenses:
    sum = sum + x
#doing it this way, using a coma, you don't have to convert sum into a string.
#the sep='' will get rid of the empty space between the $ and the sum.
print("You spent $", sum, " on lunch this week.", sep='')


#you can also skip the loop and just use sum and give it a variable
expenses = [10.50, 8, 5, 15, 20, 5, 3]
total = sum(expenses)

print("You spent $", total, " on lunch this week.", sep='')

#this will let the user enter 7 seperate expenses in to the empty list and return the sum.
total = 0
expenses = []
for i in range(7):
    expenses.append(float(input("enter expense:")))

total = sum(expenses)

print("You sent $", total, sep='')



#you can also make it so that the user can put in as many expenses as they want rather than just 7
total = 0 
expenses = []
#this will ask the user to enter how expenses they have.
num_expenses = int(input("enter # of expenses:"))
#here they can enter the expenses
for i in range(num_expenses):
    expenses.append(float(input("Enter an expense:")))

total = sum(expenses)

print("You spent $", total, sep='')