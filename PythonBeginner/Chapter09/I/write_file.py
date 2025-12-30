new= "this is a file that is created for write purpose"

f = open("tetxt.txt","w")
f.write(new)
f.close
print("successfully created the file and write")