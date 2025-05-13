# ##Nested if Statements:
# from Conditionals.LogicalOperators import temperature
#
# age =22
# has_id= False
#
# if age >= 18:
#     if has_id:
#         print("You can vote")
#     else:
#         print("You need an ID to vote")
#
# else:
#     print("You are too young to vote")

##Combining Multiple Conditions:

temperature =18
is_raining = True

if temperature >20:
    if not is_raining:
        print("It's a beautiful day for a walk.")
    else:
        print("It's raining, bring an umbrella")
else:
    print ("It's cold, bring a jacket")