print("hello welcome to the otp generator")
# imports random
import random as r
import string
length = 4
OTP = ''
characters = string.digits  #THIS STRING ADDS NUMBERS BEFORE THE OTP
print(characters)
 
for i in range(length):
    OTP = OTP + r.choice(characters)


print("OTP:" , OTP) 

print("YOUR OTP IS GENERATED THANK YOU")
