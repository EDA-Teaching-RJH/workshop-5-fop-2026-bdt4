#Statement of requirements:
#The code accepts only 5p, 10p, 20p, 50p and will ask for a valid coin if any other coin is entered
#My code however crashes when any string is entered, I need to make it so that it will not crash when this happens for reliability
coin = [5, 10, 20, 50]
value = 150 #value assigned to coffee

print ("Coins only. Coins accepted: 50p, 20p, 10p, 5p")

while value > 0:
    try:
        coffee_prompt = (int(input("Please insert a coin")))
        if coffee_prompt in coin:
            value -= coffee_prompt
            print("Value left:", value)
    except:
        print("Coin not accepted")
        continue
    


