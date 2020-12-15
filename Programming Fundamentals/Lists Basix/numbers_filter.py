n = int(input())
numbers_list = []
filtered = []

for _ in range(n):
    current_num = int(input())
    numbers_list.append(current_num)

command = input()

if command == 'even':
    for number in numbers_list:
        if number % 2 == 0:
            filtered.append(number)

elif command == 'odd':
    for number in numbers_list:
        if number % 2 != 0:
            filtered.append(number)

elif command == 'negative':
    for number in numbers_list:
        if number < 0:
            filtered.append(number)

elif command == 'positive':
    for number in numbers_list:
        if number >= 0:
            filtered.append(number)

print(filtered)
