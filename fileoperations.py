myFile = open("atart.txt","w")

#properties of the file
print(myFile.name)
print(myFile.mode)

# write to a file
myFile.write("GBJ : 100 \nkHD : 99 \nBBB : 89 ")
myFile.close()

# read a file
myFile = open("atart.txt","r")
print("reading ... \n"+myFile.read()+"\n")
print("reading only first ten characters\n")
myFile.seek(0)         # seek function allows the pointer to start from the 0 th positions
print("reading again ... \n"+myFile.read(10))
print("reading again ... \n"+myFile.read(10))

myFile.close()