# # complexity = O(n)
# def most_frequent_course(courses):
#     code = []
#     max = 0

#     for c in courses:
#         code.append(c[0])

#     for i in code:
#         if code.count(i) > max:
#             max = code.count(i)

#     for j in code:
#         if code.count(j) == max:
#             return j



# # complexity = O(n)
# # def most_frequent_course(courses):
# #     counts = {}

# #     for course in courses:
# #         code = course[0]

# #         if code not in counts:
# #             counts[code] = 0
# #             print(counts)

# #         counts[code] += 1
# #         print(counts)

# #     most_frequent = courses[0][0]

# #     for course in courses:
# #         code = course[0]

# #         if counts[code] > counts[most_frequent]:
# #             most_frequent = code

# #     return most_frequent



# # courses = [
# #     ("COSC2469", "Algorithms & Analysis"),
# #     ("ISYS2099", "Database Applications"),
# #     ("COSC2469", "Algorithms & Analysis"),
# #     ("COSC2769", "Full Stack Development")
# # ]

# courses = [
# ("ISYS2099", "Database Applications"),
# ("COSC2469", "Algorithms & Analysis"),
# ("COSC2469", "Algorithms & Analysis"),
# ("ISYS2099", "Database Applications")
# ]

# # courses = [
# #     ("A", "Course A"),
# #     ("B", "Course B"),
# #     ("A", "Course A"),
# #     ("B", "Course B")
# # ]

# print(most_frequent_course(courses))


lst = [1, 0, 2, 7]

for idx, value in enumerate(lst):
    print(idx, value)