# python has function for creating, reading, updating, & deleting files.

# create a file

myfilee = open("MyFile.txt","w")  # w used for opening 

# Get some info

print("Name :", myfilee.name)
print("Is clossed :", myfilee.closed)
print("opening mode :", myfilee.mode)

# Write to file

myfilee.write("hi my name is harsh dwivedi")
myfilee.write(" and i am 16 years old.")
myfilee.close()

# Append to file

myfilee = open(" myFile.txt","a")  # a used for adding or appending data.
myfilee.write("and i am studing BSC CS.")
myfilee.close()

# Read file

myfilee = open("MyFile.txt","r+")  # r+ used for reading
text = myfilee.read(60)
print(text)
