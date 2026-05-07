#wap to check a number is positive
import math

num=input("enter the number")
if num>"0":
    print("enterend number is positive")

else:
    print("enterend number is negative")
#wap to check a number is odd or even

number=int(input("enter the number"))
if number%2==0:
    print("enterend number is even")
else:
    print("enterend number is odd")


#wap to calculate area

# rad=input("enter radius of circle")
# area = math.pi*rad**2
# print("area of circle is ",area)
#
# #wap to check wheather the enter letter is vowel or not
# letter=input("enter letter")
# if (letter in "aeiou") or (letter in "AEIOU"):
#     print("enterend letter is vowel")
# else:
#     print("letter is not vowel")

#wap to check if a number is single digit number,2 digit number and so on upto 5 digits.

numberr=int(input("enter the number upto 5 digits:  "))

if numberr>=0 and numberr<=9:
    print("enterend number is single digit")
elif numberr>=10 and numberr<=99:
    print("enterend number is double digit")
elif numberr>=100 and numberr<=999:
    print("enterend number is triple digit")
elif numberr>=1000 and numberr<=9999:
    print("enterend number is 4 digit number")
elif numberr>=10000 and numberr<=99999:
    print("enterend number is 5 digit number"
          )
