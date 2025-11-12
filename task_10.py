lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))
start, end = map(int, input().split())

elements_to_move = lst1[start - 1:end][::-1]
lst2.extend(elements_to_move)
lst1 = lst1[:start - 1] + lst1[end:]

print(lst1, lst2, sep='\n')