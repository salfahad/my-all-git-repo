##Lab 4: Using continue in Loops

##Skipping Even Numbers:

for i in range(11):
    if i % 6 ==0:
        continue
    print(i)

##Skipping Specific Conditions:

numbers = [1, 2, 3, 4, 5, 6,16]

for number in numbers:
    if number == 6:
        continue
    print(number)