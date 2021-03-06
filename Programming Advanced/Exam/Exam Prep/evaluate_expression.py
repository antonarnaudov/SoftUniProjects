from collections import deque
from math import floor

expression = deque(input().split())

saved_numbers = []
while True:
    current_element = expression.popleft()

    if current_element in '-+/*':
        result = floor(eval(current_element.join(saved_numbers)))
        expression.appendleft(str(result))
        saved_numbers = []

        if len(expression) == 1:
            break
    else:
        saved_numbers.append(current_element)
print(expression[0])


# from collections import deque
# from math import floor
#
# string = deque(input().split())
#
# result = []
#
# while string:
#     x = string.popleft()
#     if x not in '*+-/':
#         result.append(x)
#     else:
#         result = [str(floor(eval(x.join(result))))]
#
# print(*result)
