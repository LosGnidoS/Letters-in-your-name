#!/usr/bin/python3 
#Made by Kirill Shvedov

my_name = "kirill"
x = "second_half"
alphabet = [1,2,3,4,5,6,7,8,9,10, 
11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26] #numbers of letters in the alphabet


name_leters = list(my_name)
#name_leters.append("k")
#name_leters.append("i")
#name_leters.append("r")
#name_leters.append("i")
#name_leters.append("l")
#name_leters.append("l")

name_leters[0] = alphabet[10]

print(alphabet[10])

if name_leters[0] >= 14:
	print('''First letter of my name 
goes to the x of the alphabet.''')

else:
	print('''First letter of my name 
goes to the 1 half of the alphabet.''')
 