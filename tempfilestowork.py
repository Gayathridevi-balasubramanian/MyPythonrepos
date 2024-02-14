import tempfile

# create a temporary file
t = tempfile.TemporaryFile()
# write to a temporary file
t.write(b"Save this specification :567483")

t.seek(0)

print(t.read())
# close a temporary file 
t.close()

