import zipfile

# open and list
zip = zipfile.ZipFile('wishlist.zip','r')
print(zip.namelist())

# getting the metedata of the zip folder 
for meta in zip.infolist():
    print(meta)

info = zip.getinfo("wishlist.txt")
print(info)

# to access the files in the folder
print(zip.read("wishlist.txt"))
with zip.open("wishlist.txt") as f:
    print(f.read())

# closing the zip file
zip.close()