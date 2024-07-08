mytext = input("hey there,please enter your information!! ")
try:
    with open('gfg.txt', 'w') as gfg:
	    gfg.write(mytext)
except Exception as e:
	print("There is a Problem", str(e))
