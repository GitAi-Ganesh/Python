# Write a program to fill in a letter template given below with name and date.
letter = '''Dear <|Name|>,
You are selected!
<|Date|>
'''
print(letter.replace("<|Name|>","Ganesh Salunke") .replace("<|Date|>","13 november 2025"))