p = int(input())

lst = []

for i in range(p):
    lst.append(input())

solve = 0

for i in lst:
    count = 0
    for char in i:
        if char != " ":
            count += int(char)
            if count == 2:
                solve += 1
                break

print(solve)
# print(lst)