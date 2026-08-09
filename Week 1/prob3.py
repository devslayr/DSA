# s = str(input())

# if s == s[::-1]:
#     print("Yes")
# else:
#     print("No")


# s = str(input())
# is_panlindrome = True

# for i in range(0, int(len(s) / 2)):
#     if s.count(s[i]) % 2 != 0:
#         is_panlindrome = False
#         break

# if len(s) % 2 != 0:
#     if s.count(s[int(len(s) / 2)]) == 2:
#          is_panlindrome = False

# if is_panlindrome:
#     print("Yes")
# else:
#     print("No")


s = str(input())

odd_count = 0
print(set(s))

for char in set(s):
    print(f"Character {char} appears {s.count(char)} times")
    if s.count(char) % 2 !=0:
        odd_count += 1

if odd_count <= 1:
    print("Yes")
else:
    print("No")