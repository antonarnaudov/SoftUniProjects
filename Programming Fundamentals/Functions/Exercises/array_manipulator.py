numbers = list(map(int, input().split(' ')))


def exchange(idx):
    global numbers
    if idx < 0 or idx >= len(numbers):
        print('Invalid index')
    else:
        numbers = numbers[idx + 1:] + numbers[: idx + 1]


def max_even_or_odd(command):
    global numbers

    if command == 'even':
        if len([x for x in numbers if x % 2 == 0]) == 0:
            print('No matches')
            return
        best_number = [x for x in numbers if x % 2 == 0][0]
    else:
        if len([x for x in numbers if x % 2 == 1]) == 0:
            print('No matches')
            return
        best_number = [x for x in numbers if x % 2 == 1][0]

        best_index = 0

    for i in range(len(numbers)):
        current = numbers[i]
        if command == 'even':
            if current >= best_number and current % 2 == 0:
                best_number = current
                best_index = i
        else:
            if current >= best_number and current % 2 == 1:
                best_number = current
                best_index = i
    print(best_index)


def min_even_or_odd(command):
    global numbers

    if command == 'even':
        if len([x for x in numbers if x % 2 == 0]) == 0:
            print('No matches')
            return
        best_number = [x for x in numbers if x % 2 == 0][0]
    else:
        if len([x for x in numbers if x % 2 == 1]) == 0:
            print('No matches')
            return
        best_number = [x for x in numbers if x % 2 == 1][0]

        best_index = 0

    for i in range(len(numbers)):
        current = numbers[i]

        if command == 'even':
            if current <= best_number and current % 2 == 0:
                best_number = current
                best_index = i
            else:
                if current <= best_number and current % 2 == 1:
                    best_number = current
                    best_index = i
        print(best_index)


def firs_even_or_odd(count, command):
    global numbers

    result = []
    if count > len(numbers):
        print('Invalid count')
        return

    for num in numbers:
        if len(result) == count:
            break
        if command == 'even':
            if num % 2 == 0:
                result.append(num)
        else:
            if num % 2 == 1:
                result.append(num)
    print(result)


def last_even_or_odd(count, command):
    global numbers

    result = []
    if count > len(numbers):
        print('Invalid count')
        return

    reversed_nums = list(reversed(numbers))
    for num in numbers:
        if len(result) == count:
            break
        if command == 'even':
            if num % 2 == 0:
                result.append(num)
        else:
            if num % 2 == 1:
                result.append(num)
    print(list(reversed(result)))


command = input()

while command != 'end':
    tokens = command.split()

    if tokens[0] == 'exchange':
        number = int(tokens[1])
        exchange(number)
    elif tokens[0] == 'max':
        max_even_or_odd(tokens[1])
    elif tokens[0] == 'min':
        min_even_or_odd(tokens[1])
    elif tokens[0] == 'first':
        count = int(tokens[1])
        firs_even_or_odd(count, tokens[2])
    elif tokens[0] == 'last':
        count = int(tokens[1])
        last_even_or_odd(count, tokens[2])
    command = input()

print(numbers)
