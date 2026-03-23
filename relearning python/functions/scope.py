#codes in global scope cannot use local variables
# def spam():
#     eggs = 'sss'
# spam()
# print(eggs) #returned nameError eggs is not defined

#codes that are in local scope cannot use variables from other local scope
# def spam():
#     eggs = 'SPAMSPAM'
#     bacon()
#     print(eggs)

# def bacon():
#     ham = 'hamham'
#     eggs = 'BACONBACON'

# spam() #this prints out SPAMSPAM

#codes that are in local scope can access global variables
