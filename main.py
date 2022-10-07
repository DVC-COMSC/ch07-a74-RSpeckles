

numbers = [5, 20, 30, 30, 50]
delval = int(input('Enter the deletion value: '))

#flag variable to determine if a number has been removed from the list
flag = 0

#Runs through the list and tries to remove the given value
#if it finds the given value, the value is removed and flag is set to 1
#if no values are found, the loop is broken
for i in range(len(numbers), 0, -1):
    try:
        numbers.remove(delval)
        flag = 1
    except ValueError:
        break

#if no numbers have been removed from the list, the list is cleared
if flag == 0:
    numbers = []


print(numbers)
