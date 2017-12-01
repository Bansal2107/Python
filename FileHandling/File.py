file=open("D:\\akash.txt","r+")

file.write("Hello My Name is Akash Bansal")
file.seek(0)
print(file.read())
file.write("Yay !!! Successfully Read !!!!!!")
file.seek(0)
print(file.read())
file.close()