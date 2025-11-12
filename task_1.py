numbers = [int(input()) for i in range(10)]
new_list = [numbers[j - 1] + numbers[j + 1] for j in range(8)]
print(new_list)