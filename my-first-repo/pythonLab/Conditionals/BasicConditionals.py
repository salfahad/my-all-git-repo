#Lab 1: Basic Conditionals with if, elif, and else

## 1.Basic if Statement:

# age = 18
# if  age >= 18:
#     print("You are an adult.")


##Using if, elif, and else:
# age = 60
# if  age < 18:
#     ("You are a minor.")
#
# elif  18 <= age <= 60:
#     print("You are an adult.")
#
# else: print("You are a senior citizen.")
#passMark is 60. if scored 60 to 80 is A+ and less than 60 is fail
score = int(input("Enter your score: "))
if  score < 60:
    print("fail")

elif 60  <= score < 80:
    print ("pass")

else: print ("A+")