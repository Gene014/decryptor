#Calma, Eugene Marie S.'
#BSCPE_1-4
#OOP Laboratory Exercise Number 2 Problem 2 (Decryption)

# input or insert your text here
input_str = input("Hi, Good day! Please insert your text here. ")
output_str = ""
# check and change every character to their corresponding variable
for i in range (len(input_str)):
     #   if *, change to a
    if input_str[i] == "*":
        output_str += "a"
    else: output_str += input_str[i]
print(output_str)
