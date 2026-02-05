variable_name = input ("Insert the name of your variable in camel case") #Ask user for input of camel case
output = "" #storing the input for later 

for char in variable_name: 
    if char.isupper():
        output += "_" + char.lower()
    else:
         output += char 
         
#If there is an uppercase letter, we input an underscore and change the next letter to lowercase
#Probably not the way you wanted me to do it, but I had no clue and had to search the internet for help

print(output)

