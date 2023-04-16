#Calma, Eugene Marie S.'
#BSCPE_1-4
#OOP Laboratory Exercise Number 2 Problem 2 (Decryption)

# input or insert your text here
input_str = input("\n\33[33mHi, Good day! Please insert your text here.\33[0m ")
output_str = ""
# check and change every character to their corresponding variable
for i in range (len(input_str)):
#   if *, change to a
    if input_str[i] == "*":
        output_str += "a"
#   if &, change to e
    elif input_str[i] == "&":
        output_str += "e"
#   if #, change to i
    elif input_str[i] == "#":
        output_str += "i"
#   if +, change to o
    elif input_str[i] == "+":
        output_str += "o"  
#   if !, change to u
    elif input_str[i] == "!":
        output_str += "u"
    else: output_str += input_str[i]
# print your output
print("\n\33[1mYour decrypted message is " ,(output_str))
