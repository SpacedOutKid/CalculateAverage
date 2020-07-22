#Simple program to calculate the average faster
numberOfItems = eval(input('How many items are there: '))
items = 0
total = 0
while items != numberOfItems:
    numbersToCalculate = eval(input("Enter the number you wish to calculate: "))
    total = total + numbersToCalculate
    items +=1
averageOfNumbers = total / items
print(f'Your total of the {items} is {total} and your average is {averageOfNumbers}')