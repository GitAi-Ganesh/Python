#here we will know about what are string and how they can be used 

a = 'abcdefghikl'            #single quoted string
b = "Ganesh"            #double quoted string
c = '''Ganesh'''        #triple quoted string


#String Slicing

# for using slicing we use this method (nameshot= name[index_start:index_end])

print( a [0:4])
print( a [1:]) #ending blank means last character
print( a [:4]) #starting blank means starting character

#output : Gane

name2 = a [0:3:2]
print (name2)