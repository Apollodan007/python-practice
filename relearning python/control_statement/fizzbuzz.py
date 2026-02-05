print("Enter an integer value")
user_input = int(input())

if (user_input % 3 == 0) and (user_input % 5 == 0):
    print("Fizz Buzz")
elif user_input % 3 == 0:
    print("Fizz")
elif user_input % 5 == 0:
    print("Buzz")

else:
    print(user_input)