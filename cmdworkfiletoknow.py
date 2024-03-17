import sys

# try passing the arguements as string 
print("Number of arguements",len(sys.argv))
print("The Command Line arguements :",sys.argv)


# sum of the arguements
arguements = sys.argv
sum = 0
for arg in arguements:
    try:
        number = int(arg)
        sum = sum + number
    except Exception:
        print("Bad Input")
print("The amount is",sum)