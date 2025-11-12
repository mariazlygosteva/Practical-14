lst = list(map(int, input().split()))
command = input().strip()

direction = command[0]
steps = int(command[1:])

match direction.upper():
    case 'R':
        steps = steps % len(lst)
        lst = lst[-steps:] + lst[:-steps]
    case 'L':
        steps = steps % len(lst)
        lst = lst[steps:] + lst[:steps]

print(lst)