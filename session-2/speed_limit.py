n = int(input())
list_of_journey = []
while n != -1:
    current_list = []
    for i in range(n):
        x, y = input().split()
        current_list.append([int(x), int(y)])
    list_of_journey.append(current_list)
    n = int(input())
        
# print(list_of_journey)
for l in list_of_journey:
    curr = 0
    summ = 0
    for x in l:
        summ += x[0] * (x[1] - curr)
        curr = x[1]
    print("{} miles".format(summ))
