# read numbers count
numbers_count = int(input())

counter = 1
biggest_number = 0
while counter <= numbers_count:
    current_number = int(input())
    if counter == 1:
        #print('Stored first number')
        biggest_number = current_number

    elif current_number >= biggest_number:
        biggest_number = current_number

    counter += 1

print(biggest_number)
