#if - else statement

marks= input("Enter marks: ")
if marks == "10":
    print("you will get a phone")

else:
    print("you will not get a phone")

    print("thank you")


# Convert input to integer once at the beginning
marks = int(input("Enter marks: "))

# ---------- if-elif-else statement ----------
# Check the highest range first so it doesn’t get caught by a lower one
if marks >= 91:
    print("You can go to Goa for a massage")
elif marks >= 85:
    print("You can go on a trip")
elif marks >= 80:
    print("You will get a phone")
else:
    print("You will not get a phone for 1 month")
print("Thank you")   # This line runs regardless (executes after the whole block)

# ---------- nested if statement ----------
if marks >= 80:
    print("You will get a phone")
    if marks >= 85:          # additional check inside the first true block
        print("You can go on a trip too")
else:
    print("You will not get a phone for 1 month")
    print("Thank you")

# ---------- shorthand if statement ----------
if marks >= 80: print("You will get a phone")

#shorthand if else statement

marks=80

print("you will go into kathmandu to visit") if(marks>=90) else print("you will not go into kathmandu to visit")





