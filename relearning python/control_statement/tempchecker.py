# print('Enter C or F to indicate Celsius or Fahrenheit:')
# scale = input()
# print('Enter the number of degrees:')
# degrees = input()
# if scale == 'C':
#     degrees = int(degrees)
#     if degrees >= 16 and degrees <= 38:
#         print('Safe')
#     else:
#         print('Dangerous')
# elif scale == 'F':
#     degrees = float(degrees)
#     if degrees >= 60.8 and degrees <= 100.4:
#         print('Safe')
#     else:
#         print('Dangerous')
# suggested code

print("Enter C or F to indicate Celsius or Farenheit:")
scale = input()
print("Enter the number of degrees: ")
degrees = float(input())
# if degrees >= 16 and degrees <=38 or degrees >=60.8 and degrees <= 100.4:
if (scale == 'C' and degrees >= 16 and degrees <=38) or (scale == 'F' and degrees >=60.8 and degrees <= 100.4):
    print('Safe')
else:
    print('Dangerous')