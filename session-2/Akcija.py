def minimum_cost(numbers):
    minimum_sum = 0
    list_of_groups = [numbers[i:i+3] for i in range(0, len(numbers), 3)]
    for group in list_of_groups:
        if len(group) == 1:
            minimum_sum += group[0]
        else:
            minimum_sum += group[0] + group[1]
    return minimum_sum
n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))
numbers.sort(reverse=True)
print(minimum_cost(numbers))