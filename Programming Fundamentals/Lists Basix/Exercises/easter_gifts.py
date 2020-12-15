gifts = input().split(' ')

command = input()

while command != 'No Money':
    tokens = command.split(' ')

    if tokens[0] == 'OutOfStock':
        gift = tokens[1]
        for i in range(len(gifts)):
            if gifts[i] == gift:
                gifts[i] = 'None'

    elif tokens[0] == 'Required':
        idx = int(tokens[2])
        if 0 <= idx < len(gifts):
            gifts[idx] = tokens[1]

    elif tokens[0] == 'JustInCase':
        gifts[-1] = tokens[1]

    command = input()

for gift in gifts:
    if gift == 'None':
        gifts.remove(gift)

print(' '.join(gifts))