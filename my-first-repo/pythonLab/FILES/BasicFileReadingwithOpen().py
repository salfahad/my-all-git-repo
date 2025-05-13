
##Lab 1: Basic File Reading with open()

#Reading a File Line by Line:

file = open("sample.txt", "r")
for line in file:
    print(line.strip())

file.close()

##Reading All Lines at Once:

file = open("sample.txt", "r")
content = file.read()
print(content)
file.close()