myfile = open("atart.txt","r")


#reading a line at a time
print("My one line : "+ myfile.readline())
myfile.seek(0)

# iterating through the each line of the line
for line in myfile:
    newScore = line.replace("BBB","BGD")
    print(newScore)
myfile.close()