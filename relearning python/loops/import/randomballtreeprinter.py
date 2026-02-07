import random
#using for loop to create the christmas tree with balls
# print("Enter the size of the tree")
# tree_size = int(input())
# indent = tree_size - 1
# currentoddnumber = 1
# for i in range(tree_size):
#     branch = ""
#     for i in range(currentoddnumber):
#         ballspace = random.randint(1,4)
#         if ballspace == 1:
#             branch += "o"
#         else:
#             branch += "^"
#     print(" "* indent + branch)
#     currentoddnumber += 2
#     indent -= 1
#     i += 1
# stump = tree_size - 1
# print(" " * stump + "#")
# print(" " * stump + "#")

#using while loop to create a christmas tree with balls
print("Enter the size of the tree")
tree_size = int(input())
indent = tree_size - 1
currentoddnumber = 1
i = 0
while i < tree_size:
    branch = ""
    j = 0
    while j < currentoddnumber:
        ballspace = random.randint(1,4)
        if ballspace == 1:
            branch += "o"
        else:
            branch += "^"
        j += 1
    print(" " * indent + branch)
    currentoddnumber += 2
    indent -= 1
    i += 1
stump = tree_size - 1
print(" " * stump + "#")
print(" " * stump + "#")