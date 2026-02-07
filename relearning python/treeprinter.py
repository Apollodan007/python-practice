# using for loop
# print("Enter the tree size")
# tree_size = int(input(''))
# currentoddnumber = 1
# indent = tree_size -1
# for i in range(tree_size):
#     print(' ' * indent + '^' * currentoddnumber)
#     currentoddnumber += 2
#     indent -= 1
# stump = tree_size - 1
# print(' ' * stump + '#')
# print(' ' * stump + '#')

#using while loop
print("Enter the size of the tree")
tree_size = int(input())
currentoddnumber = 1
indent = tree_size - 1
i = 1
while i < (tree_size + 1):
    print(" "*indent + ("^")*currentoddnumber)
    currentoddnumber += 2
    indent -= 1
    i += 1
stump = tree_size - 1
print(" "*stump + "#")
print(" "*stump + "#")