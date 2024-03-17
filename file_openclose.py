f = open('ex.csv','r')
print(f)

f.readline()
f.readlines()


f  = open('ex.csv','r')
for line in f.readlines():
    print(line)

f = open('ex.csv','r')
for line in f.readlines():
    print(line.strip())

#############
#writing lines
f = open('ex1.csv','w')
print(f)

f.write('Line1\n')
f.write('Line2\n')

f.close()

################
f = open('ex1.csv','a')
f.write('Line3\n')
f.write('Line4\n')
f.close()



with open('ex1.csv','a') as f:
    f.write('Some stuff')
    f.write('Some more stuff')



